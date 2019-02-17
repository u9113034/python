players=['John','Peter','Ivan','Kevin','Jodan']
teams=['Michael','Peter','Curry','Kevin','Jodan']
newteam=players
for player in players:
    for team in teams:
        if player==team:
            newteam.remove(player)

newteam+=teams
print(newteam)