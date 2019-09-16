from django.urls import path, include
from .views import EmployeeViewSet, login_view, logout_view
from rest_framework import routers

routes = routers.DefaultRouter()
routes.register('', EmployeeViewSet)

urlpatterns = [
    path('details/', include(routes.urls), name='employee_list'),
    path('auth/login', login_view.as_view(), name='auth login'),
    path('auth/logout', logout_view.as_view(), name='auth logout'),

]
