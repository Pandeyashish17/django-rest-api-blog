from django.contrib import admin
from .models import article,author,categories,tag
from django.contrib.auth.models import Group
# Register your models here.


class RichTextEditorAdmin(admin.ModelAdmin):
     class Media:
         css= {
            "all":("css/main.css",)
         }

         js=("js/app.js",)




admin.site.register(author)
admin.site.register(article,RichTextEditorAdmin)
admin.site.unregister(Group)
admin.site.register(categories)
admin.site.register(tag)