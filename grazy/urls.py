from django.urls import path
from grazy import views
urlpatterns = [
    path('test/',views.test_view_hello, name='test-hello'),
    path('test/',views.test_view_bye, name='test-bye'),
    path('test/',views.test_view, name='test-view'), 
    path('test/<int:number>',views.catch_number_view, name="catch-number"),
    path('/test/<str:string>',views.catch_string_view, name="catch-string"),
]
