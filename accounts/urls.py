from django.conf.urls import url
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth import logout

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name="logout"),
]
