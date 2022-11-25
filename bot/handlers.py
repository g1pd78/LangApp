import abc ###
import telegram as tg
import telegram.ext as tg_ext
import typing as tp
from bot import messages
import cardClass

class BaseHandler():
    def __init__(self):
        self.user: tp.Optional[tg.User] = None

    async def __call__(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        self.messages = messages.get_messages(self.user)
        await self.handle(update, context)

    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplemented

class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.messages.start())


class HelpHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.messages.help())


class AddHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.messages.add())


class SetUpLangHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.messages.setLangs())


class TextInputHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            self.messages.echo(update.message.text)
        )


def setup_handlers(application: tg_ext.Application):
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))
    application.add_handler(tg_ext.CommandHandler('add', addHandler()))
    application.add_handler(tg_ext.CommandHandler('add', SetUpLangHandler()))
    application.add_handler(
        tg_ext.MessageHandler(
            tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, TextInputHandler()
        )
    )