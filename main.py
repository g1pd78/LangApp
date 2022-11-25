import argparse
import lang
import cardClass
from bot import handlers
import telegram.ext as tg_ext


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--key', type=str, required=True)
	return parser.parse_args()


def main()->None:
	args = parse_args()
	#lang.search(args.key)

	deck = cardClass.CardDeck()
	application = tg_ext.Application.builder().token(args.key).build()
	#deck1.addCard('school', 'English')
	#print(deck1.cardList[0].wordList[0])
	handlers.setup_handlers(application, deck)
	application.run_polling()


if __name__ == "__main__":
	main()
