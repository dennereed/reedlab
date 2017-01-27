from django.db import models

CHARTYPE_CHOICES = (('UM', 'Unordered Multistate'), ('OM', 'Ordered Multistate'), ('IN', 'Integer'),
                    ('RN', 'Real Number'), ('TE', 'Text'))
ELEMENT_CHOICES = (('U', 'Upper Jaw'), ('L', 'Lower Jaw'), ('B', 'Both'))


class Character(models.Model):
    cid = models.AutoField(primary_key=True)
    charname = models.CharField(max_length=50, default='', null=False)
    unit = models.CharField(max_length=5, null=True)
    notes = models.TextField(null=True)
    chartype = models.CharField(max_length=5, default='UM', null=False, choices=CHARTYPE_CHOICES)
    mandatory = models.NullBooleanField(default=False)
    multistatetype = models.IntegerField(default=1, null=False)
    reliability = models.IntegerField(default=5)
    availability = models.IntegerField(default=5)
    fuzziness = models.DecimalField(decimal_places=5, max_digits=20, default=0, null=False)
    fuzzinessispercent = models.NullBooleanField(default=False)
    keystates = models.CharField(max_length=5, null=True)
    charheading = models.IntegerField(null=True)
    headinglink = models.IntegerField(null=True)
    charwording = models.TextField(null=True)
    charwording2 = models.TextField(null=True)
    unitisprefix = models.NullBooleanField(default=False)
    formatstring = models.TextField(null=True)
    paragraphlink = models.IntegerField(null=True)
    sentencelink = models.IntegerField(null=True)
    commalink = models.IntegerField(null=True)
    speciallink = models.IntegerField(null=True)
    specialelement = models.IntegerField(null=True)
    usecomma2 = models.NullBooleanField(default=False)
    omitfinalcomma = models.NullBooleanField(default=False)
    omitvalues = models.NullBooleanField(default=False)
    emphasize = models.NullBooleanField(default=False)
    omitperiod = models.NullBooleanField(default=False)
    numstates = models.IntegerField(default=2, null=True)
    charref = models.IntegerField(null=True)
    element = models.CharField(max_length=4,  default='U', null=True)
    disabled = models.NullBooleanField(default=False, null=False)

    def __unicode__(self):
        return self.charname

