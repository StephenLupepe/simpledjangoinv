from django.urls import path
from .views import ApiItemList, ApiItemDetail

urlpatterns = [
    path('list/', ApiItemList.as_view()),
    path('list/<int:pk>', ApiItemDetail.as_view()),
]