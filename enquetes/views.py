from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil
from enquetes.models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')

def exibir(request, perfil_id):
    perfil = Perfil()
    if perfil_id == 1:
        perfil = Perfil(perfil_id, 'Elvis', 'elvis@gmail.com',
                '8699999-9999', 'IFPI')
    if perfil_id == 2:
        perfil = Perfil(perfil_id, 'Lucas', 'lucas@gmail.com',
                '8698888-8888', 'UFPI')
    return render(request, 'perfil.html', {'perfil': perfil})

def get_enquete(request, enquete_id):
    enquete = Enquete.objects.get(id=enquete_id)
    return render(request, 'enquete.html', {'enquete': enquete})
    
   
 