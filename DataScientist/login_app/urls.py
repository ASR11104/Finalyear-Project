from django.conf.urls import url
from login_app import views


# SET THE NAMESPACE!
app_name = 'login_app'

urlpatterns=[
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^loginindex/',views.loginindex,name='loginindex'),
]
