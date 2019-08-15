from django.urls import path, include
from .views import EmployeeViewSet
from rest_framework import routers

routes = routers.DefaultRouter()
routes.register('', EmployeeViewSet)

urlpatterns = [
    path('', include(routes.urls), name='employee_list'),

]
