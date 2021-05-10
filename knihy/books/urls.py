from django.urls import path
from . import views

urlpatterns = [
    path('', views.KnihyHomeView.as_view(), name='index'),
    path('list', views.KnihyListView.as_view(), name='list'),
    path('detail/<int:pk>', views.KnihyDetailView.as_view(), name='detail'),
]
