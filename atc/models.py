from django.db import models
from datetime import date

# General purpose classes


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LogType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LogField(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EventID(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return self.id


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reference(models.Model):
    url = models.URLField()

    def __str__(self):
        return str(self.url)


# Strict ATC classes


class LoggingPolicy(models.Model):

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

    event_id = models.ForeignKey(
        EventID,
        verbose_name="Event ID(s)",
        on_delete=models.SET_NULL,
        null=True
    )

    reference = models.ForeignKey(
        Reference,
        verbose_name="Reference(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    config = models.TextField(
        verbose_name="Configuration"
    )

    def __str__(self):
        return self.title


class DataNeeded(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    logging_policy = models.ForeignKey(
        LoggingPolicy,
        verbose_name="Logging Policy(ies)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="loggin_policy"
    )

    reference = models.ForeignKey(
        Reference,
        verbose_name="Reference(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    category = models.OneToOneField(
        Category,
        verbose_name="Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="category"
    )

    platform = models.OneToOneField(
        Platform,
        verbose_name="Platform",
        on_delete=models.SET_NULL,
        null=True,
        related_name="platform"
    )

    log_type = models.OneToOneField(
        LogType,
        verbose_name="Log Type",
        on_delete=models.SET_NULL,
        null=True,
        related_name="log_type"
    )

    channel = models.OneToOneField(
        Channel,
        verbose_name="Channel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="channel"
    )

    provider = models.OneToOneField(
        Provider,
        verbose_name="Provider",
        on_delete=models.SET_NULL,
        null=True,
        related_name="provider"
    )

    log_field = models.OneToOneField(
        LogField,
        verbose_name="Log Field(s)",
        on_delete=models.SET_NULL,
        null=True,
        related_name="log_field"
    )

    sample = models.TextField(
        verbose_name="Sample"
    )

    def __str__(self):
        return self.title


class Enrichment(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    data_needed = models.ForeignKey(
        DataNeeded,
        verbose_name="Data Needed",
        on_delete=models.SET_NULL,
        null=True,
        related_name='data_needed'
    )

    data_to_enrich = models.ForeignKey(
        DataNeeded,
        verbose_name="Data to Enrich",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='data_to_enrich'
    )

    requirement = models.ForeignKey(
        "self",
        verbose_name="Requirement(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    reference = models.ForeignKey(
        Reference,
        verbose_name="Reference(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    new_field = models.ForeignKey(
        LogField,
        verbose_name="New field(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
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

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    reference = models.ForeignKey(
        Reference,
        verbose_name="Reference(s)",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="reference"
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


class DetectionRules(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    def __str__(self):
        return self.title
