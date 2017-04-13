import sys

global arg

class LootBag:

	def add_to_bag(self, toy, name):
		kids_set = set()
		with open('logs/' + name + '.log', 'a+') as child_list:
			child_list.write('{0}\n'.format(str(toy)))

		#each time we add, we should add to a set of allkids.log'
		with open('logs/allkids.log', 'a+') as list_of_kids:
			for x in list_of_kids:
				kids_set.add(x)
			kids_set.add(name)
		with open('logs/allkids.log', 'r+') as new_list_of_kids:
			for x in kids_set:
				new_list_of_kids.write('{}\n'.format(x))

		delivery = dict()
		with open('logs/delivery.log', 'r+') as delivery_log:
			delivery = { 'name': name, 'delivered': False }
			delivery_log.write('{0}'.format(delivery))

	def remove_toy_from_child(self, name, toy):
		toylist = list()

		with open('logs/' + name + '.log', 'r') as child_list:
			for x in child_list:
				toylist.append(x[:-1])

			if toy not in toylist:
				print('Not in Bag: ' + toy)
			elif toy in toylist:
				#print('Removed from Bag: ' + toy)
				toylist.remove(toy)

		with open('logs/' + name + '.log', 'w') as new_list:
			for x in toylist:
			 	new_list.write('{}\n'.format(x))
		# print('Bag of Toys is Now: ' + str(toylist))

	def list_kids(self):
		allchildren = list()
		with open('logs/allkids.log', 'r') as list_kids:
			for x in list_kids:
				allchildren.append(x[:-1])
		return allchildren

	def list_toys_for_child(self, name):
		childtoys = list()
		with open('logs/' + name + '.log') as child_list:
			for x in child_list:
				childtoys.append(x[:-1])
		return childtoys

	# get_single_child(name) - see if toys are delivered, dict
	# deliver_toys_to_child(name) - set toys to delivered
	def get_single_child(self, name):
		child_dict = dict()
		with open('logs/delivery.log', 'r') as delivery_list:
			for line in delivery_list:
				child_dict = eval(line)
			return child_dict # needed?

	def deliver_toys_to_child(self, name):
		return {
			'delivered': True
		}

	# if __name__ == '__main__':

	# 	arg = sys.argv[1]
	# 	# name = sys.argv[2]
	# 	#toy = sys.argv[3]

	# 	if arg == 'add':
	# 		# toy, name
	# 		add_to_bag(sys.argv[2], sys.argv[3])
	# 	elif arg == 'remove':
	# 		# name, toy
	# 		remove_toy_from_child(sys.argv[2], sys.argv[3])
	# 	elif arg == 'ls':
	# 		list_toys_for_child(sys.argv[2])
	# 	elif arg == 'delivered':
	# 		delivered_toys(name)

