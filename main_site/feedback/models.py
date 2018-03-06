from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return "Пользователь %s %s %s" % (self.name, self.email, self.text)

    class Meta:
        verbose_name = 'Собшение'
        verbose_name_plural = 'A lot of messages'