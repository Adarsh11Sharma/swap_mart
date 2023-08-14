from django.contrib import admin

# Register your models here.
from .models import Exchange_Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Exchange_Room)
admin.site.register(Topic)
admin.site.register(Message)