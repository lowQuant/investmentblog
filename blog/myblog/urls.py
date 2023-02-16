from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('article/<int:pk>',views.article_detail_view,name='article-detail'),
    path('blog/post', views.AddPostView.as_view(), name='post'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove',views.DeletePostView.as_view(), name='delete-post'),
    path('blog/category/<str:cat>/',views.CategoryView, name='category'),
    # path('register/', views.UserRegisterView.as_view(),name='register'),
]


urlpatterns += staticfiles_urlpatterns()
