from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField(verbose_name="id чата")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="id пользователя")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, null=True, verbose_name="Пользователь",)
    verification_code = models.CharField(max_length=10, null=True, verbose_name="Код верификации")

    def generate_verification_code(self) -> str:
        code = get_random_string(10)
        self.verification_code = code
        self.save()
        return code
