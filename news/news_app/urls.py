from django.urls import path, include
from .views import ShowNew, Index

urlpatterns = [
    path('', Index.as_view(), name='index-name'),
    path('new/<int:id_new>', ShowNew.as_view(), name="new-name")
    ]