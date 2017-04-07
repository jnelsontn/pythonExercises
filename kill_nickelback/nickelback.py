# Example set
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Nickelback', 'RockStar'),
    ('Fleetwood Mac', 'Rhiannon'),
    ('Third Eye Blind', 'Semi-Charmed Life'),
    ('Fleetwood Mac', 'Little Lies'),
    ('Nickelback', 'Too Bad'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

good_songs = { key + ' - ' + value for (key, value) in songs if key is not 'Nickelback' }

# for key, value in songs:
# 	if key is not 'Nickelback':
# 		good_songs.append(key + " - " + value)

print(good_songs)