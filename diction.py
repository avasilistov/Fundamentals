alien_o = {'color': 'green', 'points': 5}
print(alien_o['color'])
print(alien_o['points'])
alien_o['x_position'] = 'uuu'
alien_o['y_position'] = 'ttt'
print(alien_o)
del alien_o['points']
print(alien_o)
print(alien_o.get('points', 'No point value assigned'))
for k, v in alien_o.items():
    print(k, v)
for k in sorted(alien_o.keys()):
    print(alien_o[k])
for v in sorted(alien_o.values()):
    print(v)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    for k in alien.keys():
        print(alien.get(k))

prompt = 'Say somthing.. '
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)


