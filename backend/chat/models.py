from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from  django.dispatch import receiver
from django.core.exceptions import ValidationError


class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_as_user1', default=1)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_as_user2', default=1)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.user1} - {self.user2}"
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            existing_chat = Chat.objects.filter(user1=self.user1, user2=self.user2)
            if existing_chat.exists():
                raise ValidationError("Já existe um chat")
        super().save(*args, **kwargs)

        


class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE, related_name="message_sender", null=False)
    message_sender = models.ForeignKey(User,related_name="message_sender",  on_delete=models.CASCADE, default=1)
    message_receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE, default=1)
    content = models.TextField(null=True)

    def __str__(self):
         return str(self.chat.pk)







# @receiver(pre_save, sender=Message)
# def get_sender(sender, instance, **kwargs):
#     if not instance.message_sender:
#         instance.message_sender = instance.message_sender