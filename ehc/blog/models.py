from django.db import models
class SiteUser(models.Model):
    username = models.CharField(max_length=50 )
    password = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)  # Add PhoneNumber field
    
    def __str__(self):
        return str(self.username)


class Ticket(models.Model):
    ticket_maker = models.CharField(max_length=50, null=True)
    ticket_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True)
    ticket = models.CharField(max_length=1024, null=True)
    file = models.FileField(upload_to='ticket_files/', null=True, blank=True)
    closed = models.BooleanField(default=False)
    answer = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return str(self.ticket_maker) + " - " + self.name

    def save(self, *args, **kwargs):
        if self.answer is not None:
            self.closed = True
        super().save(*args, **kwargs)

class Message(models.Model):
    MessageSender = models.CharField(max_length=50, null=True)
    Message_date = models.DateTimeField(auto_now_add=True)
    Message = models.CharField(max_length=1024, null=True)
    Response = models.CharField(max_length=1024, null=True)
    file = models.FileField(upload_to='ticket_files/', null=True, blank=True)
    def __str__(self):
        return str(self.MessageSender)
    
class feedback(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    feedback = models.CharField(max_length=1024, null=True)
    def __str__(self):
        return str(self.username)
    