from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import ldsmtweet.views


urlpatterns = [
    path("", ldsmtweet.views.index, name="index"),
    path("admin/", admin.site.urls),
]
