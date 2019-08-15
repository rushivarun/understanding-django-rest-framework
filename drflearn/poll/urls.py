from django.urls import path, include
from .views import poll, poll_details, PollAPIView, PollDetailView, PollListView

urlpatterns = [
    path('', poll, name='poll'),
    path('<int:id>/', poll_details, name='poll_details'),
    path('class_based/', PollAPIView.as_view(), name='poll_class_based_view'),
    path('class_based/<int:id>/', PollDetailView.as_view(),
         name='pol_based'),
    path('generic_view/', PollListView.as_view(), name='poll_list_view'),
    path('generic_view/<int:id>/', PollListView.as_view(), name='polssl_list_view'),

]
