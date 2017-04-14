import pickle
import sys

class Mary(object):

	def __init__(self):
		self.messages = dict()
		self.mary = list()

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
			self.mary = self.messages['Mary']
		except KeyError:
			self.messages['Mary'] = list()
			self.mary = self.messages['Mary']

		self.mary.append(sys.argv[1:])
		self.messages['Mary'] = self.mary
		self.serialize()
		print(self.messages)
		
mary = Mary()
mary.run()