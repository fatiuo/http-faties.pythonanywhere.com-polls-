from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('ear/',views.ear,name='ear'),
    path('khodemeni/',views.khodemeni,name='khodemeni'),
    path('tanafos/',views.tanafos,name='tanafos'),
    path('quaresh/',views.quaresh,name='quaresh'),
    path('galu/',views.galu,name='galu'),
    path('falaj/',views.falaj,name='falaj'),
    #path('results/<int:question_id>/', views.results, name='results'),
]