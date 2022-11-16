class Card:
	def __init__(self):
		self.words = []
		self.contextExamples = defaultdict(list) # для каждого слова может быть несколько примеров контекста
		self.confirmed = False



class CardDeck:
	def __init__(slef):
		languages = defaultdict()
