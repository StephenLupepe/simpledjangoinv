from django.urls import path
from . import views
from .views import AddItemView, ItemUpdateView,ItemDeleteView, ItemDetailView

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", AddItemView.as_view(), name="add-item"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("item/<int:pk>/update", ItemUpdateView.as_view(), name="item-update"),
    path("item/<int:pk>/delete", ItemDeleteView.as_view(), name="item-delete"),
]