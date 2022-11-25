import telegram as tg
import telegram.ext as tg_ext
import config

class Base:
    def start(self) -> str:
        raise NotImplemented
    def help(self) -> str:
        raise NotImplemented
    def add(self) -> str:
        raise NotImplemented
    def setLangs(self) -> str:
        raise NotImplemented
    def textInput(self) -> str:
        raise NotImplemented


class Worder(Base):
    def start(self) -> str:
        return config.startMsg

    def help(self) -> str:
        return config.helpMsg

    def add(self) -> str:
        # make true some var or what
        # print info bout input format 
        # nums of langs
        # end of input by some sign 
        return "Input Started"

    def setLangs(self) -> str:

        return "Setup Languages"

    def textInput(self, text: str) -> str:
        pass
    


def get_messages(user: tg.User) -> Base:
    return Worder()