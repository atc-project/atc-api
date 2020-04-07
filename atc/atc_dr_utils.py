from atc.models import DetectionRule, DataNeeded, LogField
from yaml import load_all, FullLoader
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

mitre_tactics_list = [
    'initial_access',
    'execution',
    'persistence',
    'privilege_escalation',
    'defense_evasion',
    'credential_access',
    'discovery',
    'lateral_movement',
    'collection',
    'command_and_control',
    'exfiltration',
    'impact',
]

mitre_techniques_regex = 'attack\.t\d{4}'

process_creation_config = [
    {
        "EventID": 4688,
        "product": "windows",
        "service": "security"
    },
    {
        "EventID": 10,
        "product": "windows",
        "service": "sysmon"
    },
]


def fill_DN(detection_rule: DetectionRule) -> DetectionRule:

    rule = load_all(detection_rule.raw_rule, Loader=FullLoader)
    [rule] = [x for x in rule]

    # contains a list of lists of fields
    field_list = []
    # contains a list of EventIDs (integeres)
    event_ids = []

    logsources = []

    ##########################
    # Fill three above lists #
    ##########################

    for item in rule:
        if item.get("logsource"):
            logsrc = item.get("logsource")
            lg_dict = {}
            if logsrc.get("product"):
                lg_dict["product"] = logsrc.get("product")
            if logsrc.get("service"):
                lg_dict["service"] = logsrc.get("service")
            if logsrc.get("category"):
                lg_dict["category"] = logsrc.get("category")
                if logsrc.get("category") == "process_creation":
                    if 1 not in event_ids:
                        event_ids.append(1)
                    if 4688 not in event_ids:
                        event_ids.append(4688)
            if lg_dict:
                logsources.append(lg_dict)
                del lg_dict

        if not item.get("detection"):
            continue
        temp_field_list = []
        for condition in item.get("detection").keys():
            if condition == "condition":
                # this does not contain any fields from logs so skip
                continue

            if not isinstance(item["detection"].get(condition), dict):
                # something unexpected or just straight list of values
                # so skip
                continue

            for fieldname in item["detection"][condition].keys():
                # add a fieldname to field_list
                temp_field_list.append(fieldname)

                # check if maybe the field holds event IDs
                if fieldname.lower() in [
                    "event_id",
                    "event_ids",
                    "eventid",
                    "eventids"
                ]:
                    # if this is a list of values..
                    if isinstance(item["detection"][condition][fieldname],
                                  list):
                        for value in item["detection"][condition][fieldname]:
                            try:
                                event_ids.append(int(value))
                            except ValueError:
                                pass

                    # if this is a single value..
                    elif isinstance(item["detection"][condition][fieldname],
                                    str):
                        try:
                            event_ids.append(
                                int(item["detection"][condition][fieldname])
                            )
                        except ValueError:
                            pass
                    # or maybe it's natively an int..
                    elif isinstance(item["detection"][condition][fieldname],
                                    int):
                        try:
                            event_ids.append(
                                item["detection"][condition][fieldname]
                            )
                        except ValueError:
                            pass
        field_list.append(temp_field_list)
    # if "JRAT" in detection_rule.title:
    #     print(field_list)
    #     print(event_ids)
    #     print(logsources)
    ########################
    # Find according DNs   #
    ########################

    # find by EventID (easy)
    for logsrc in logsources:
        for event_id in event_ids:
            if not logsrc.get("product"):
                break
            if logsrc.get("category"):
                for pc_lgsrc in process_creation_config:
                    try:
                        # icontains => case-insensitive contains
                        data_needed_list = DataNeeded.objects.filter(
                            eventID=pc_lgsrc.get("EventID"),
                            platform__name__icontains=pc_lgsrc.get("product"),
                            provider__name__icontains=pc_lgsrc.get("service"),
                        )
                    except ObjectDoesNotExist:
                        data_needed_list = None
            else:
                try:
                    # icontains => case-insensitive contains
                    data_needed_list = DataNeeded.objects.filter(
                        eventID=event_id,
                        platform__name__icontains=logsrc.get("product"),
                        provider__name__icontains=logsrc.get("service"),
                    )
                except ObjectDoesNotExist:
                    data_needed_list = None
                except ValueError:
                    # Probably missing service field
                    continue

            if data_needed_list:
                for data_needed in data_needed_list:

                    # we do not have to care about duplicates
                    # django will handle that
                    detection_rule.data_needed.add(data_needed.id)

    # find by set of fields (all fields have to match)
    for field_set in field_list:
        translated_list = []

        # translate field names to IDs
        for field in field_set:
            try:
                translated_list.append(LogField.objects.get(name=field))
            except ObjectDoesNotExist:
                pass

        # find all DNs with at least one field in the provided list
        # filter to leave only those with all the fields matched
        results = DataNeeded.objects.filter(
            fields__in=translated_list).annotate(
            num_fields=Count('fields')).filter(
            num_fields=len(translated_list)
        )

        if results:
            # result is a DataNeeded object
            for result in results:
                #
                # https://youtu.be/0p_1QSUsbsM
                #

                for logsrc in logsources:

                    if result.eventID.values() \
                            and result.eventID.values(
                    )[0]["id"] not in event_ids:
                        continue

                    # Init values
                    product_check = False
                    service_check = False

                    # If there is a product defined in DR logsource
                    # and it matches DN platform..
                    if logsrc.get("product") \
                            and logsrc.get(
                                "product") in str(result.platform).lower():
                        product_check = True

                    # If the product check was passed
                    # and DR logsource had service defined
                    # and it matches DN service..
                    if product_check and logsrc.get("service") \
                            and logsrc.get(
                                "service") in str(result.provider).lower():
                        service_check = True

                    # This is dirty workaround
                    # There will be FPs for sure
                    #
                    # If service_check already not passed
                    # and DR logsource has category
                    # and category is process_creation
                    # set service_check to True
                    if not service_check and logsrc.get("category") \
                            and logsrc.get(
                                "category").lower() in result.title.lower():
                        service_check = True

                    # If both checks are passed, add DN and break the loop
                    if service_check and product_check:
                        detection_rule.data_needed.add(result.id)
                        break
