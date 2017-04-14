import pickle
import sys

class Margaret(object):

	def __init__(self):
		self.messages = dict()
		self.margaret = list()

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

	def run(self):
		try:
			self.margaret = self.messages['Margaret']
		except KeyError:
			self.messages['Margaret'] = list()
			self.margaret = self.messages['Margaret']

		self.margaret.append(sys.argv[1:])
		self.messages['Margaret'] = self.margaret
		self.serialize()
		print(self.messages)
		
margaret = Margaret()
margaret.run()