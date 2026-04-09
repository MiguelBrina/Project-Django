from django.http import HttpResponse
def home(request):
    return HttpResponse("hello world") 

def sobre(request):
    return HttpResponse("Página Sobre")

def autor(request):
    return HttpResponse("Página do Autor")

def noticias(request):
    return HttpResponse("Página de Notícias")

def empresa(request):
    return HttpResponse("Página da Empresa")