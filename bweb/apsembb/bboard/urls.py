from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView
from . import views

app_name = 'bboard'
urlpatterns = [
    path('', RedirectView.as_view(url='/forum/')),
    path('accounts/', include('django.contrib.auth.urls')),   
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('forum/', views.ForumView.as_view(), name='forum'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),  
    path('postComment', views.postComment, name='postComment'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('loginUser', views.loginUser, name='loginUser'),
    ]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)