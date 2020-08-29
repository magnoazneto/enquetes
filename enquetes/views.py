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
    enquete = Enquete()
    if enquete_id == 1:
        print('here')
        enquete = Enquete(enquete_id, 'Qual o framework web mais famoso da stack javascript?',
                            '12-02-2020')
    if enquete_id == 2:
        enquete = Enquete(enquete_id, 'Qual o framework para desenvolvimento híbrido mais recente da google?',
                            '15-06-2020')
    if enquete_id == 3:
        enquete = Enquete(enquete_id, 'Onde você mora?',
                            '19-08-2020')
    print(enquete.texto)
    return render(request, 'enquete.html', {'enquete': enquete})