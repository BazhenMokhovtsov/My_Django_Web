from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:new_id>', views.single_new, name='single_new'),
    path('comment-delete/today/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
