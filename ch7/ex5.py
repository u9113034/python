# ex5.py
players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
while players:
    index_player=players.pop()
    if index_player[1] < 200:
        continue
    print(index_player)
    

