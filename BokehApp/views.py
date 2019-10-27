from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    first_graph = "Oya"
    return HttpResponse(first_graph)