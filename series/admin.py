from django.contrib import admin

from series.models import serie, seasonDetail, episodeDetail

# Register your models here.
admin.site.register(serie)
admin.site.register(seasonDetail)
admin.site.register(episodeDetail)