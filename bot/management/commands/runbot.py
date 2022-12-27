from django.core.management import BaseCommand
from bot.tg import tg_client
from bot.tg.bot import TgBot

# from todolist.bot.tg import tg_client
# from todolist.bot.tg.bot import TgBot


class Command(BaseCommand):
    help = "Get message from tg bot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = tg_client

    def handle(self, *args, **options):
        tg_bot = TgBot(tg_client=self.tg_client)
        tg_bot.run()
