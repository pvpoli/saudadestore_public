from django.contrib import admin
from .models import Title, Photos, HomepagePhotos,HomepagePhotosMobile,QuemSomos,AlforrecaTexto,AlforrecaImagens,ComoChegar

class PhotoHomepageAdmin(admin.ModelAdmin):
    list_display = ('photos_name', 'image_tag')

class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ('text_quemsomos', 'image_tag')

class AlforrecaAdmin(admin.ModelAdmin):
    list_display = ('text_alforreca', 'image_tag')

# Register your models here.
admin.site.register(Title)
admin.site.register(Photos,PhotoHomepageAdmin)
admin.site.register(HomepagePhotos,PhotoHomepageAdmin)
admin.site.register(HomepagePhotosMobile,PhotoHomepageAdmin)
admin.site.register(QuemSomos,QuemSomosAdmin)
admin.site.register(AlforrecaTexto,AlforrecaAdmin)
admin.site.register(AlforrecaImagens,PhotoHomepageAdmin)
admin.site.register(ComoChegar)
