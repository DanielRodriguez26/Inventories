from django.urls import path

from .views import  ImportCSV

urlpatterns = [
    #path('logout', UserLogout.as_view()),
    path('import_csv', ImportCSV.as_view()),
]
