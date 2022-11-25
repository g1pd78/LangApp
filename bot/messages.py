import telegram as tg
import telegram.ext as tg_ext
import config

class Base:
    def start(self) -> str:
        raise NotImplemented
    def help(self) -> str:
        raise NotImplemented


class Worder(Base):
    def start(self) -> str:
        return config.startMsg

    def help(self) -> str:
        return config.helpMsg

    def add(self) -> str:
        pass


def get_messages(user: tg.User) -> Base:
    return Worder()