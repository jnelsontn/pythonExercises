zoo = tuple()
zoo = ('Dog', 'Cat', 'Lion', 'Zebra', 'Human', 'Gorilla')

x = zoo.index('Dog')
#print(x)

(Dog, Cat, Lion, Zebra, Human, Gorilla) = zoo
#print(Cat)

zoo = list(zoo)
zoo.extend(['Ant', 'Elephant', 'Tiger'])

zoo = tuple(zoo)
