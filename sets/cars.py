showroom = set(['CarModel1', 'CarModel2', 'CarModel3', 'CarModel4'])
showroom.add('CarModel1')
second_showroom = set(['CarModel5', 'CarModel6'])
showroom.update(second_showroom)
showroom.discard('CarModel5')

print('current showroom: {}.'.format(showroom))

junkyard = set(['Junk1', 'Junk2', 'Junk3', 'Junk4', 'Junk5', 'CarModel2', 'CarModel3'])

y = showroom.intersection(junkyard)
# print('intersection: {}.'.format(y))

showroom = showroom.union(junkyard)
print('union method: {}.'.format(showroom))

showroom.discard('Junk1')
showroom.discard('Junk2')
print(showroom)