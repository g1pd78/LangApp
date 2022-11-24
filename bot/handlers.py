import abc ###
import telegram as tg
import telegram.ext as tg_ext
import typing as tp


class BaseHandler:
    def __init__(self):
        self.user = tp.Optional[tg.User] = None

    async def __call__(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        self.messages = messages.get_messages(self.user)
        await self.handler(update, context)

    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplemented

class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.message.start())


class HelpHandler(BaseHandler):
    async def handle(self, update: tg.Update, 
        context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.message.help())


def setup_handlers(application: tg_ext.Application):
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))