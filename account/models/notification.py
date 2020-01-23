from django.db import models

TYPE = (
    ('challenge', 'desafio'),
)


class Notification(models.Model):
    sender = models.ForeignKey('account.user', related_name='+', on_delete=models.CASCADE)
    receiver = models.ForeignKey('account.user', related_name='+', on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
    type = models.CharField(max_length=30, choices=TYPE, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"