from enum import unique
from tabnanny import verbose
from django.db import models


class TelegramUsers(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    full_name = models.CharField(max_length = 255, verbose_name="TO'LIQ ISM")
    phone_number = models.CharField(max_length = 255, unique=True, blank=True, null=True)
    username = models.CharField(max_length = 255, blank=True, null=True)
    score = models.IntegerField(default=5, verbose_name="BALL")
    joined_date = models.DateField(auto_now_add=True, verbose_name="QO'SHILGAN VAQTI")

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = "Telegram obunachilar"
        verbose_name_plural = "Telegram obunachilar"


class InvitedUsers(models.Model):
    user_offered = models.ForeignKey(TelegramUsers, related_name='offered', verbose_name="Taklif qilgan", on_delete=models.CASCADE)
    user_invited = models.ForeignKey(TelegramUsers, related_name="invited", verbose_name="Taklif qilingan", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return self.user_offered.full_name
    
    class Meta:
        verbose_name = "Taklif qilingan obunachilar"
        verbose_name_plural = "Taklif qilingan obunachilar"


class Channels(models.Model):
    username = models.CharField(max_length=255)
    invite_link = models.CharField(max_length=255, verbose_name="TASHRIF LINKI")
    status = models.BooleanField(verbose_name="HOLATI")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="QO'SHILGAN VAQTI")

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Kanallar"
        verbose_name_plural = "Kanallar"