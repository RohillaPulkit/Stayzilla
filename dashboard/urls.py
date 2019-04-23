from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import get_chart_data, get_table_data
app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    # path('data', views.get_data, name="data"),
    path('chart/data', get_chart_data, name="chart_data"),
    path('dashboardTable/data', get_table_data, name="table_data"),

]

