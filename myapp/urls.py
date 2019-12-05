from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippet', views.SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api', views.api_root, name='api_root'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),
         name='highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)