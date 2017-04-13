import unittest
#from lootbag import *
from lootbagclass import *

# python -m unittest discover -s . -p test_*.py -v

class TestBagOLoot(unittest.TestCase):

	@classmethod # unittest sees classmethod so it ignores from testing
	def setUpClass(self):
		self.bag = LootBag()

	def test_add_toy_to_bag(self):
		
		self.bag.add_to_bag('Ball', 'Bob')
		vincent_toys = self.bag.list_toys_for_child('Bob')

		self.assertIn('Ball', vincent_toys)

	def test_remove_toy_from_child(self):
		toy = 'Slinky'
		self.assertIn('Vincent', self.bag.list_kids())

		self.bag.add_to_bag(toy, 'Vincent')
		self.bag.remove_toy_from_child('Vincent', toy)
		vincent_toys = self.bag.list_toys_for_child('Vincent')

		self.assertNotIn(toy, vincent_toys)

	def test_list_of_good_kids(self):
		toy = 'Silly Putty'
		self.bag.add_to_bag(toy, 'Vincent')
		good_kids = self.bag.list_kids()

		self.assertIn('Vincent', good_kids)

	def test_toys_in_bag_for_specific_child(self):
		toy = 'Slime'
		self.bag.add_to_bag(toy, 'Mikey')
		vincent_toys = self.bag.list_toys_for_child('Mikey')
		good_kids = self.bag.list_kids()

		self.assertIn(toy, vincent_toys)

	def test_child_toys_are_delivered(self):
		toy = 'Unicorn'
		self.bag.add_to_bag(toy, 'Vincent')
		vincent = self.bag.get_single_child('Vincent')

		self.assertFalse(vincent['delivered'])

		vincent = self.bag.deliver_toys_to_child('Vincent')
		self.assertTrue(vincent['delivered'])






