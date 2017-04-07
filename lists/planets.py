planet_list = ["Mercury", "Mars"]
planet_list.append('Jupiter')
planet_list.append('Saturn')

last_two_planets = list()
last_two_planets = ['Neptune', 'Pluto']

planet_list.extend(last_two_planets)

planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
# planet_list.append('Pluto')

x = slice(0, 4)
rocky_planets = planet_list[x]
#print(rocky_planets)

del planet_list[7]
#print(planet_list)

spaceships = tuple()
spaceships = [ (['Ship1', 'Mercury']), (['Ship2', 'Venus']), (['Ship3', 'Earth']), (['Ship4', 'Mars']), (['Ship5', 'Jupiter']), (['Ship5', 'Pluto']) ] 
#print(spaceships)

for planet in planet_list:
	print(planet)
	for spaceship in spaceships:
		if spaceship[1] == planet:
			print(spaceship[0])
			print('----------')


