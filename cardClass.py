import config

class Word:
	def __init__(self, word: str, lang: str):
		self.word = word
		# self.srcImage = ...
		self.context = list() # strs
		self.language = '' # key
		self.gotImage = False

	def __str__(self):
		print(self.word)
		for c in self.context:
			print(c)
		return ''


	def requestContext(self):
		print("Input context:")
		text = input()
		if text != '':
			self.context.append(text)
			self.requestContext()
		else:
			return

	def requestImage(self):
		pass



class Card:
	def __init__(self):
		self.wordList = []
		self.confirmed = False 
		self.comment = None


	def addWord(self, word, lang):
		newWord = Word(word, lang)
		if not newWord in self.wordList:
			self.wordList.append(newWord)
			newWord.requestContext()


	def addComment(self, text):
		self.comment = text
	
	def removeWordFromDeck():
		pass
		


class CardDeck:
	def __init__(self):
		self.cardList = list()
		
	
	def addCard(self, word, curLang):
		card = Card()
		if self.checkValidness(word, curLang):
			self.cardList.append(card)
			########### lang setup
			for language in config.languageList:
				card.addWord(word, language)
			card.addComment('')




	def checkValidness(self, word, lang):
		if lang and lang in config.languageList and\
			word:
			return True
		return False