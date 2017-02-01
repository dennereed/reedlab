from django.db import models

CHARTYPE_CHOICES = (('UM', 'Unordered Multistate'), ('OM', 'Ordered Multistate'), ('IN', 'Integer'),
                    ('RN', 'Real Number'), ('TE', 'Text'))
ELEMENT_CHOICES = (('U', 'Upper Jaw'), ('L', 'Lower Jaw'), ('B', 'Both'))


class Character(models.Model):
    cid = models.AutoField(primary_key=True)
    char_name = models.CharField(max_length=50, default='', null=False)
    unit = models.CharField(max_length=5, null=True)
    notes = models.TextField(null=True)
    char_type = models.CharField(max_length=5, default='UM', null=False, choices=CHARTYPE_CHOICES)
    mandatory = models.NullBooleanField(default=False)
    multistate_type = models.IntegerField(default=1, null=False)
    reliability = models.IntegerField(default=5)
    availability = models.IntegerField(default=5)
    fuzziness = models.DecimalField(decimal_places=5, max_digits=20, default=0, null=False)
    fuzzinessis_percent = models.NullBooleanField(default=False)
    key_states = models.CharField(max_length=5, null=True)
    char_heading = models.IntegerField(null=True)
    heading_link = models.IntegerField(null=True)
    char_wording = models.TextField(null=True)
    char_wording2 = models.TextField(null=True)
    unit_is_prefix = models.NullBooleanField(default=False)
    format_string = models.TextField(null=True)
    paragraph_link = models.IntegerField(null=True)
    sentence_link = models.IntegerField(null=True)
    comma_link = models.IntegerField(null=True)
    special_link = models.IntegerField(null=True)
    special_element = models.IntegerField(null=True)
    usecomma2 = models.NullBooleanField(default=False)
    omit_final_comma = models.NullBooleanField(default=False)
    omit_values = models.NullBooleanField(default=False)
    emphasize = models.NullBooleanField(default=False)
    omit_period = models.NullBooleanField(default=False)
    num_states = models.IntegerField(default=2, null=True)
    char_ref = models.IntegerField(null=True)
    element = models.CharField(max_length=4,  default='U', null=True, choices=ELEMENT_CHOICES)
    disabled = models.NullBooleanField(default=False, null=False)

    def __unicode__(self):
        return self.char_name


class CharacterState(models.Model):
    cid = models.ForeignKey(Character)
    cs = models.CharField(max_length=30, null=False)
    char_state_name = models.CharField(max_length=100, null=False)
    notes = models.TextField(null=True)
    state_wording = models.CharField(max_length=10, null=True)
    state_format_string = models.CharField(max_length=10, null=True)
    implicit = models.BooleanField(default=False)
    use_edit = models.NullBooleanField(default=True)
    use_identify = models.NullBooleanField(default=False)
    use_description = models.NullBooleanField(default=False)
    use_phylo = models.NullBooleanField(default=False)
    use_other = models.NullBooleanField(default=False)
    min_value = models.DecimalField(decimal_places=5, max_digits=20, default=0, null=False)
    max_value = models.DecimalField(decimal_places=5, max_digits=20, default=0, null=False)

    def __unicode__(self):
        return self.char_state_name


class Species(models.Model):
    genus_name = models.CharField(max_length=50, null=False)
    trivial_name =  models.CharField(max_length=50, null=False)
    common_name = models.CharField(max_length=50, null=True)
    type_citation = models.TextField(null=True)
    type_location_id = models.IntegerField(null=True)
    type_specimen_no = models.CharField(max_length=100, null=True)
    generic_type = models.NullBooleanField()
    genus_citation = models.TextField(null=True)
    taxonomic_order = models.CharField(max_length=50, null=True)
    taxonomic_family = models.CharField(max_length=50, null=True)
    taxonomic_subfamily = models.CharField(max_length=50, null=True)
    notes = models.TextField(null=True)
    extant = models.NullBooleanField()

    def __unicode__(self):
        return self.genus_name + ' ' + self.trivial_name


class Item(models.Model):
    item_name = models.CharField(max_length=100, null=False)
    item_wording = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    abundance = models.IntegerField(null=True, blank=True)
    collection_unit = models.CharField(max_length=50, null=True, blank=True)
    lit_ref = models.CharField(max_length=100, null=True, blank=True)
    lit_key = models.IntegerField(null=True, blank=True)
    lit_ref_detail = models.TextField(null=True, blank=True)
    collection_code = models.CharField(max_length=15, null=True, blank=True)
    specimen_no = models.CharField(max_length=20, null=True, blank=True)
    species = models.ForeignKey(Species)
    taxonomic_order = models.CharField(max_length=50, null=True, blank=True)
    disabled = models.NullBooleanField(default=False)

    def __unicode__(self):
        return self.item_name


class Description(models.Model):
    item = models.ForeignKey(Item)
    character = models.ForeignKey(Character)
    modifier = models.CharField(max_length=10, null=True, blank=True)
    char_state = models.CharField(max_length=10, null=True, blank=True)
    x = models.DecimalField(decimal_places=5, max_digits=20, default=0, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(default=0, null=True, blank=True)

    def __unicode__(self):
        return self.item.__unicode__()+'['+self.character.__unicode__()+', '+self.char_state+']'


class ItemImage(models.Model):
    item = models.ForeignKey(Item)
    image = models.ImageField(upload_to='Item_Images')
    description = models.TextField(null=True, blank=True)
