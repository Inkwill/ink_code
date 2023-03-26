from StudyPython import lexicon

class ParserError(Exception):
	"""docstring for ParserError"""
	pass
		


class Sentence(object):
	"""parse a list of words to a Sentence"""
	def __init__(self, content):
		super(Sentence, self).__init__()
		self.content = content
		self.words = lexicon.scan(content)
		for word in self.words:
			if word[0] in ('stop'):
				self.words.remove(word)

		index = self.peek_subject()
		self.subject = self.words[index] if index != None else ('noun','player')
		self.index_subject = index

		index = self.peek_verb()
		self.verb = self.words[index] if index != None else ('erro','nothing to do')
		self.index_verb = index

		index = self.peek_object()
		self.object = self.words[index] if index != None else ('erro','player')
		self.index_object = index

	def peek(words):
		return words[0][0] if words else None

	def peek_subject(self):
		"""peek the subject index:
		1. the first word is verb, return player
		2. the word before first verb is noun, return the word
		3. the word before first verb is other, """
		index_verb = self.peek_verb()
		if index_verb != None and index_verb > 0 and self.words[index_verb -1][0] == 'noun':
			return index_verb -1
		else:
			return None

	def peek_verb(self):
		"""peek the first verb index"""
		for i in range(0,len(self.words)):
			if self.words[i][0] == 'verb':
				return i
		return None

	def peek_object(self):
		"""peek the object index:
		1. the word after first verb is noun or direction,return the index
		"""
		index_verb = self.peek_verb()
		if index_verb != None and index_verb < len(self.words)-1 and self.words[index_verb +1][0] in ('noun','direction'):
			return index_verb +1
		else:
			return None

