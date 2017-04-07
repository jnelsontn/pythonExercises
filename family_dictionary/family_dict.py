my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

for k,v in my_family.items():
    print(v['name'] + "is my " + k + " and is " + str(v['age']) + " years old.")

