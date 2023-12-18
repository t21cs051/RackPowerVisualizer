from django.urls import path
from .views import RackList,RackAddView, RackShowView,RackEditView,RackDeleteView
from .views import UpsList, UpsAddView, UpsShowView, UpsEditView, UpsDeleteView
from .views import PowerSystemList, PowerSystemAddView, PowerSystemShowView
from apps.master.views import PowerSystemEditView, PowerSystemDeleteView, PowerSystemEditView, PowerSystemDeleteView

app_name = "master"

urlpatterns = [
    path('rack/', RackList.as_view(), name='rack'),
    path('rack_add/', RackAddView.as_view(), name='rack_add'),
    path('rack_show/', RackShowView.as_view(), name='rack_show'),
    path('rack_edit/<int:id>/', RackEditView.as_view(), name='rack_edit'),
    path('rack_delete/<int:id>/', RackDeleteView.as_view(), name='rack_delete'),
    path('ups/', UpsList.as_view(), name='ups'),
    path('ups_add/', UpsAddView.as_view(), name='ups_add'),
    path('ups_show/', UpsShowView.as_view(), name='ups_show'),
    path('ups_edit/<int:id>/', UpsEditView.as_view(), name='ups_edit'),
    path('ups_delete/<int:id>/', UpsDeleteView.as_view(), name='ups_delete'),
    path('power_system/', PowerSystemList.as_view(), name='power_system'),
    path('power_system_add/', PowerSystemAddView.as_view(), name='power_system_add'),
    path('power_system_show/', PowerSystemShowView.as_view(), name='power_system_show'),
    path('power_system_edit/<int:id>/', PowerSystemEditView.as_view(), name='power_system_edit'),
    path('power_system_delete/<int:id>/', PowerSystemDeleteView.as_view(), name='power_system_delete'),
]