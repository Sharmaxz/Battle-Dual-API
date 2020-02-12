from django.db import models


class Item(models.Model):
    type = models.BooleanField()

    def __str__(self):
        if self.type:
            return 'O'
        else:
            return 'X'


    class Meta:
        verbose_name = "Item "
        verbose_name_plural = "Items"
