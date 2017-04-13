import pickle
import sys

class Mary(object):

	def __init__(self):
		self.messages = list()

		try:
			self.messages = self.deserialize()
		except FileNotFoundError:
			pass

	def serialize(self):
		with open('messages', 'wb+') as f:
			pickle.dump(self.messages, f)

	def deserialize(self):
		try:
			with open('messages', 'rb+') as f:
				self.messages = pickle.load(f)
		except EOFError:
			pass

		return self.messages

	def list_messages(self):
		for key, note in enumerate(self.messages):
			print(str(key) + " : " + str(note))

	def runme(self):
		self.messages.append(sys.argv[1:])
		self.serialize()
		self.list_messages()
		
mary = Mary()
mary.runme()