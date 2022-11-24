import telegram as tg
import telegram.ext as tg_ext


class Base:
    def start(self) -> str:
        raise NotImplemented
    def help(self) -> str:
        raise NotImplemented


class Worder(Base):
    def start(self) -> str:
        return "asd"
    def help(self) -> str:
        return "asdasdasdsa"




def get_messages(user: tg.User) -> Base:
    return Worder()