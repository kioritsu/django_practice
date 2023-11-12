from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('', views.TopView.as_view(), name='home'),
    path('money', views.MoneyView.as_view(), name='money'),
    path('add_category', views.AddCategoryView.as_view(), name='add_category'),
    path('calendar', views.calendar, name='calendar'),
    
]