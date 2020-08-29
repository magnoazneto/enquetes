from django.db import models

# Create your models here.
   

class Enquete(object):
    def __init__(self, id=0, texto='', data_publicacao=''):
        self.id = id
        self.texto = texto
        self.data_publicacao = data_publicacao


