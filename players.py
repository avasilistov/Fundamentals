players = ['charls', 'martina', 'frlorce', 'michael', 'elly']
print(players[0:3])
print(players[:2])
print(players[3:])
print(players[:])
print(players[-3:])
for player in players[:3]:
    print(player.title())
new_players = players[:]
print(new_players)