from matrix_field import MatrixField
from django.db import models

from account.models.user import User


class Hash(models.Model):
    name = 'Hash'
    turn = models.ForeignKey('account.User', on_delete=models.CASCADE)
    turn_label = models.CharField(max_length=255, null=True, blank=True)
    turn_count = models.PositiveIntegerField(default=0)
    matrix = MatrixField(datatype='int', dimensions=(3, 3), default=[[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]])
    is_end = models.BooleanField()
    is_draw = models.BooleanField(null=True)

    class Meta:
        verbose_name = "Jogo da Velha"
        verbose_name_plural = "Jogos da Velha"

    def save(self, *args, **kwargs):
        self.turn_label = User.objects.get(pk=self.turn.id).nickname

        super(Hash, self).save(*args, **kwargs)