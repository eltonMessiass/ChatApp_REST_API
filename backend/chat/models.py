from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from  django.dispatch import receiver
from django.core.exceptions import ValidationError


class Chat(models.Model):
    participants=models.ManyToManyField(User)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participants = self.participants.all()
        # return f"{participants[0]} - {participants[1]}"
        if participants.count() >= 2:
            return f"{participants[0]} - {participants[1]}"
        # Se houver apenas um participante
        elif participants.count() == 1:
            return f"{participants[0]} - "
        # Se não houver participantes
        else:
            return "Sem participantes"
    
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         existing_chat = Chat.objects.filter(participants__in=self.participants.all()).distinct()
    #         if existing_chat.exists() and existing_chat.count() == len(self.participants.all()):
    #             raise ValidationError("Já existe um chat")
    #     super().save(*args, **kwargs)

        


class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE, null=False)
    message_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)




@receiver(pre_save, sender=Message)
def get_sender(sender, instance, **kwargs):
    if not instance.message_sender:
        instance.message_sender = instance.message_sender