from django.urls import path
from .views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('Item/', ItemListCreateAPIView.as_view(), name ='list-create-item'),
    path('Item/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-item'),
    path('Item/comment/', CommentListCreateAPIView.as_view(), name ='list-create-comment'),
    path('Item/comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-comment'),
]
from django.urls import path
from . import views  # Ensure there's no circular import

