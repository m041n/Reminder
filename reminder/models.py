from django.db import models
from account.models import Profile


class Person(models.Model):
    SEND_TYPE = [
        ("EM", "Email"),
        ("PN", "Phone number"),
        ("BO", "Both"),
        ("NO", "None"),
    ]

    user_rel = models.ForeignKey(Profile, on_delete=models.CASCADE, name='person_profile_rel')

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=11, null=True)
    birth_date = models.DateField(null=True)
    notification_time = models.DateField(null=True)
    message = models.TextField(null=True)
    send_message_time = models.DateField(null=True)
    congrats_birth = models.BooleanField(null=True)
    congrats_birth_message = models.TextField(null=True)
    send_type = models.CharField(max_length=3, choices=SEND_TYPE, default="NO")

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.phone_number}"


class Event(models.Model):
    SEND_TYPE = [
        ("EM", "Email"),
        ("PN", "Phone number"),
        ("BO", "Both"),
        ("NO", "None"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    user_rel = models.ForeignKey(Profile, on_delete=models.CASCADE, name='person_profile_rel')
    persons_rel = models.ManyToManyField(Person)

    message = models.TextField()
    send_massage_time =models.DateField()
    send_type = models.CharField(max_length=3, choices=SEND_TYPE, default="NO")