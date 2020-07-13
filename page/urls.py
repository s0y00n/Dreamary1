from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"), #path는 : 어떤주소/어떤함수 실행/ 뭐라고 부를지) 지정하는 것
    path('introduce/', views.introduce, name="introduce"),
    path('profile/<int:designer_id>', views.detail, name="detail"),
]