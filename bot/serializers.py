from rest_framework import serializers

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ('verification_code',)
    #     read_only_fields = ('id', 'chat_id', 'user_ud')
    #
    # def update(self, instance, validated_data):
    #     instance = super().update(instance, validated_data)
    #     tg_client.send_message(chat_id=instance.chat_id, text='Успешно')
    #     return instance