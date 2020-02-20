from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

TYPE = (
    ('2', '1x1'),
    ('4', '2x2'),
)

LIMIT = models.Q(app_label='hash', model='hash')


class Room(models.Model):
    name = models.CharField(max_length=35)
    owner = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="owner")
    type = models.CharField(choices=TYPE, max_length=3)
    content_type = models.ForeignKey(ContentType, limit_choices_to=LIMIT, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    game = GenericForeignKey('content_type', 'object_id')

    player_one = models.ForeignKey('account.User', null=True, blank=True, on_delete=models.SET_NULL, related_name="player_one")
    player_two = models.ForeignKey('account.User', null=True, blank=True, on_delete=models.SET_NULL, related_name="player_two")

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.name
