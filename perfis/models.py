from django.db import models

# Create your models here.


class Perfil(object):
    def __init__(self, id=0, nome='', email='',
                    telefone='',
                    nome_empresa=''):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa