
from django.http import HttpResponse

def get_contacts(request):
    return HttpResponse("Контакты: 0 755 168 204")

def get_about(request):
    return HttpResponse("О нас: Мы занимаемся сайтом!")

def catch_string(request, string):
    return HttpResponse(f"Caught string: {string}")
