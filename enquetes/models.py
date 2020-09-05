from django.db import models


class Enquete(models.Model):
    texto = models.CharField(max_length=40)
    data_publicacao = models.DateField(max_length=20)


"""
class Enquete(object):
    def __init__(self, id=0, texto='', data_publicacao=''):
        self.id = id
        self.texto = texto
        self.data_publicacao = data_publicacao
"""


