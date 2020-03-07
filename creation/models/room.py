from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from account.models.user import User
from games.hash.models.hash import Hash

TYPE = (
    ('2', '1x1'),
    ('4', '2x2'),
)

LIMIT = models.Q(app_label='hash', model='hash')


def player_one_label():
    return


class Room(models.Model):
    name = models.CharField(max_length=35)
    type = models.CharField(choices=TYPE, max_length=3)
    game_type = models.ForeignKey(ContentType, limit_choices_to=LIMIT, on_delete=models.CASCADE)
    game_id = models.PositiveIntegerField()
    game = GenericForeignKey('game_type', 'game_id')

    owner = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="owner")
    owner_label = models.CharField(max_length=255, null=True, blank=True)

    player_one = models.ForeignKey('account.User', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="player_one")
    player_one_label = models.CharField(max_length=255, null=True, blank=True)
    player_two = models.ForeignKey('account.User', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="player_two")
    player_two_label = models.CharField(max_length=255, null=True, blank=True)

    turn = models.CharField(max_length=255, null=True, blank=True)
    is_end = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.owner_label = User.objects.get(pk=self.owner.id).nickname
        self.player_one_label = User.objects.get(pk=self.player_one.id).nickname
        self.player_two_label = User.objects.get(pk=self.player_two.id).nickname

        self.turn = Hash.objects.get(pk=self.game_id).turn.nickname
        self.is_end = Hash.objects.get(pk=self.game_id).is_end

        super(Room, self).save(*args, **kwargs)

