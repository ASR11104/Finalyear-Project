from django.conf.urls import url
from datavisualisation_app import views


# SET THE NAMESPACE!
app_name = 'datavisualisation_app'


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    
    url(r'^api/chart/data/$', views.ChartData.as_view()),
   

]