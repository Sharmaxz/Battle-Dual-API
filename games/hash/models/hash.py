from django.db import models
from matrix_field import MatrixField


class Hash(models.Model):
    name = 'Hash'
    turn = models.ForeignKey('account.User', on_delete=models.CASCADE)
    turn_count = models.PositiveIntegerField()
    matrix = MatrixField(datatype='int', dimensions=(3, 3))
    is_end = models.BooleanField()

    class Meta:
        verbose_name = "Jogo da Velha"
        verbose_name_plural = "Jogos da Velha"
