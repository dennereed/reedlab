from django.contrib import admin
from models import Character, CharacterState


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['cid', 'charname', 'unit', 'notes', 'chartype', 'mandatory', 'element', 'disabled']
    list_filter = ['chartype', 'element', 'disabled', 'mandatory']


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterState)
