from django.urls import path
from todo import views

urlpatterns =[
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
]