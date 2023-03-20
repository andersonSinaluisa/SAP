from django.conf.urls import url
from django.urls import path


from stats.views.stats import StatsView


urlpatterns = [
    path('list', StatsView.as_view(), name="stats"),
]