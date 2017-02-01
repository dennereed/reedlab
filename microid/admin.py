from django.contrib import admin
from models import Character, CharacterState, Item, Description, Species, ItemImage


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['cid', 'char_name', 'unit', 'notes', 'char_type', 'mandatory', 'element', 'disabled']
    list_filter = ['char_type', 'element', 'disabled', 'mandatory']


class DescriptionInline(admin.TabularInline):
    model = Description
    ordering = ['character', 'char_state']
    extra = 1
    classes = ['collapse']


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra =1


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'notes', 'species', 'taxonomic_order']
    list_filter = ['taxonomic_order', 'collection_code']
    inlines = [ItemImageInline, DescriptionInline]
    search_fields = ['item_name', 'item_wording', 'notes', 'collection_code', 'taxonomic_order']

admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterState)
admin.site.register(Item, ItemAdmin)
admin.site.register(Species)
