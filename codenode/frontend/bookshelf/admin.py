from django.contrib import admin

from codenode.frontend.bookshelf.models import Folder


class FolderAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', )
    search_fields = ('owner__username', 'owner__first_name', 'owner__last_name', 'title')

admin.site.register(Folder, FolderAdmin)

