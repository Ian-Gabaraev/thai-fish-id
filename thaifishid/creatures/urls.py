from django.urls import re_path

from .views import FishFilterView

app_name = 'creatures'

urlpatterns = [
    re_path(
        r'^fish/$',
        FishFilterView.as_view(),
        name="fish"
    ),
]
