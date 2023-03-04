#Treasure map in Python

row1 =['🐞','🐞','🐞']
row2 =['🐞','🐞','🐞']
row3 =['🐞','🐞','🐞']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

position=input('Enter your position two digit number:')

hor = int(position[0])
ver = int(position[1])

map[hor -1][ver - 1] ='🔥'
print(f'{row1}\n{row2}\n{row3}')
