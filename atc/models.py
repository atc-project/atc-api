from django.db import models
from datetime import date

# General purpose classes


class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Platform(models.Model):

    class Meta:
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LogType(models.Model):

    class Meta:
        verbose_name = "Log Type"
        verbose_name_plural = "Log Types"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Channel(models.Model):

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Provider(models.Model):

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Volume(models.Model):

    class Meta:
        verbose_name = "Volume"
        verbose_name_plural = "Volumes"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LogField(models.Model):

    class Meta:
        verbose_name = "Log Field"
        verbose_name_plural = "Log Fields"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stage(models.Model):

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EventID(models.Model):

    class Meta:
        verbose_name = "Event ID"
        verbose_name_plural = "Event IDs"

    id = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return str(self.id)


class Tag(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class References(models.Model):

    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "References"

    url = models.URLField()

    def __str__(self):
        return str(self.url)


# Strict ATC classes


class LoggingPolicy(models.Model):

    class Meta:
        verbose_name = "Logging Policy"
        verbose_name_plural = "Logging Policies"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    default = models.CharField(
        max_length=255,
        verbose_name="Default"
    )

    volume = models.ForeignKey(
        Volume,
        verbose_name="Volume",
        on_delete=models.SET_NULL,
        null=True
    )

    eventID = models.ManyToManyField(
        EventID,
        verbose_name="Event ID(s)",
    )

    references = models.ManyToManyField(
        References,
        verbose_name="References(s)",
        blank=True
    )

    configuration = models.TextField(
        verbose_name="Configuration"
    )

    def __str__(self):
        return self.title


class DataNeeded(models.Model):

    class Meta:
        verbose_name = "Data Needed"
        verbose_name_plural = "Data Needed"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    loggingpolicy = models.ManyToManyField(
        LoggingPolicy,
        verbose_name="Logging Policy(ies)",
        blank=True,
        related_name="loggin_policy"
    )

    references = models.ManyToManyField(
        References,
        verbose_name="References(s)",
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="category"
    )

    platform = models.ForeignKey(
        Platform,
        verbose_name="Platform",
        on_delete=models.SET_NULL,
        null=True,
        related_name="platform"
    )

    type = models.ForeignKey(
        LogType,
        verbose_name="Log Type",
        on_delete=models.SET_NULL,
        null=True,
        related_name="type"
    )

    channel = models.ForeignKey(
        Channel,
        verbose_name="Channel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="channel"
    )

    provider = models.ForeignKey(
        Provider,
        verbose_name="Provider",
        on_delete=models.SET_NULL,
        null=True,
        related_name="provider"
    )

    fields = models.ManyToManyField(
        LogField,
        verbose_name="Log Field(s)",
        related_name="fields"
    )

    sample = models.TextField(
        verbose_name="Sample"
    )

    def __str__(self):
        return self.title


class Enrichment(models.Model):

    class Meta:
        verbose_name = "Enrichment"
        verbose_name_plural = "Enrichments"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    data_needed = models.ManyToManyField(
        DataNeeded,
        verbose_name="Data Needed",
        related_name='data_needed'
    )

    data_to_enrich = models.ManyToManyField(
        DataNeeded,
        verbose_name="Data to Enrich",
        blank=True,
        related_name='data_to_enrich'
    )

    requirements = models.ManyToManyField(
        "self",
        verbose_name="Requirement(s)",
        blank=True,
    )

    references = models.ManyToManyField(
        References,
        verbose_name="References(s)",
        blank=True,
    )

    new_fields = models.ManyToManyField(
        LogField,
        verbose_name="New field(s)",
        blank=True,
        related_name="new_field"
    )

    author = models.CharField(
        max_length=255,
        verbose_name="Author"
    )

    config = models.TextField(
        verbose_name="Config"
    )

    def __str__(self):
        return self.title


class ResponseAction(models.Model):

    class Meta:
        verbose_name = "Response Action"
        verbose_name_plural = "Response Actions"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    references = models.ForeignKey(
        References,
        verbose_name="References(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="references"
    )

    author = models.CharField(
        max_length=255,
        verbose_name="Author"
    )

    stage = models.ForeignKey(
        Stage,
        verbose_name="Stage",
        on_delete=models.SET_NULL,
        null=True,
        related_name="stage"
    )

    creation_date = models.DateField(
        default=date.today,
        verbose_name="Creation date"
    )

    linked_ra = models.ForeignKey(
        "self",
        verbose_name="Linked Response Action(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    workflow = models.TextField(
        verbose_name="Workflow"
    )

    def __str__(self):
        return self.title


class ResponsePlaybook(models.Model):

    class Meta:
        verbose_name = "Response Playbook"
        verbose_name_plural = "Response Playbooks"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    tag = models.ForeignKey(
        Tag,
        verbose_name="Tag(s)",
        on_delete=models.SET_NULL,
        null=True
    )

    SEVERITY_CHOIES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    severity = models.CharField(
        max_length=1,
        choices=SEVERITY_CHOIES,
        verbose_name="Severity"
    )

    TLP_CHOIES = [
        ('W', 'White'),
        ('G', 'Green'),
        ('A', 'Amber'),
        ('R', 'Red'),
    ]

    tlp = models.CharField(
        max_length=1,
        choices=TLP_CHOIES,
        verbose_name="TLP"
    )

    PAP_CHOIES = [
        ('W', 'White'),
        ('G', 'Green'),
        ('A', 'Amber'),
        ('R', 'Red'),
    ]

    pap = models.CharField(
        max_length=1,
        choices=PAP_CHOIES,
        verbose_name="PAP"
    )

    author = models.CharField(
        max_length=255,
        verbose_name="Author"
    )

    creation_date = models.DateField(
        default=date.today,
        verbose_name="Creation date"
    )

    identification = models.ForeignKey(
        ResponseAction,
        verbose_name="Identification",
        on_delete=models.SET_NULL,
        null=True,
        related_name="identification"
    )

    containment = models.ForeignKey(
        ResponseAction,
        verbose_name="Containment",
        on_delete=models.SET_NULL,
        null=True,
        related_name="containment"
    )

    eradication = models.ForeignKey(
        ResponseAction,
        verbose_name="Eradication",
        on_delete=models.SET_NULL,
        null=True,
        related_name="eradication"
    )

    recovery = models.ForeignKey(
        ResponseAction,
        verbose_name="Recovery",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recovery"
    )

    lessons_learned = models.ForeignKey(
        ResponseAction,
        verbose_name="Lessons learned",
        on_delete=models.SET_NULL,
        null=True,
        related_name="lessons_learned"
    )

    workflow = models.TextField(
        verbose_name="Workflow"
    )

    def __str__(self):
        return self.title


class DetectionRule(models.Model):

    class Meta:
        verbose_name = "Detection Rule"
        verbose_name_plural = "Detection Rules"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    tag = models.ManyToManyField(
        Tag, blank=True
    )

    data_needed = models.ManyToManyField(
        DataNeeded, blank=True
    )

    severity = models.TextField(
        verbose_name="Severity Level"
    )

    dev_status = models.TextField(
        verbose_name="Development Status"
    )

    references = models.ManyToManyField(
        References,
        verbose_name="References(s)",
        blank=True,
    )

    author = models.CharField(
        max_length=255,
        verbose_name="Author"
    )

    raw_rule = models.TextField(
        verbose_name="Raw rule (JSON)"
    )

    def __str__(self):
        return self.title
