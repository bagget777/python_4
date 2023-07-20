from django.shortcuts import render
from django.http import HttpResponse

# #request = HttpRequest
def test_view(requirements):
    return HttpResponse("Test")

def test_view_hello(requirements):
    return HttpResponse("hello", status=500)

def test_view_bye(requirements):
    return HttpResponse("bye")

#отправляем загаловок
# def test_view(requirements):
    # my_List = [1, 2, "3", 4]
    # return HttpResponse("Test")
#маленький кусок html
# def test_view(requirements):
#     html = "<p>этот текст видишь ты, <i> а этот текст другой</i>.</h1>"
#     return HttpResponse(html)
# def test_view(requirements):
#  html =    """<!DOCTYPE html> 
# <html lang="ru"> 
#    <head> 
#       <meta charset="UTF-8"> 
#       <title>You bro</title> 
#    </head> 
#    <body> 
#       <p> 
#          <b> 
#             Этот текст будет полужирным, <i>а этот — ещё и курсивным</i>. 
#          </b> 
#       </p> 
#    </body> 
# </html>"""
#  return HttpResponse(html)
#заголовок
# def test_view(requirements):
#     my_List = [0, 1, 2, "3", 4]
#     headers = {"Name": "baget"}
#     return HttpResponse(my_List, headers=headers, status=404)

# def test_view(requirements): 1
#     return HttpResponse("Test") 1

def catch_number_view(requests, number):
    return HttpResponse(f"Your number: {number}")

def catch_string_view(requests, string):
    return HttpResponse(f"Your number: {string}")