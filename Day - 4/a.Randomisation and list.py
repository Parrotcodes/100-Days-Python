#Randomisation in python

import random
import modulerandomisationpi

random_num = random.randint(1,10)
print(f'Random Number (1-10):{random_num}')

random_float = random.random()
print(f'Random float value between 0 to 1:{random_float}')

random_float2 = random.random()*5
print(f'Random float value between 0 to 5:{random_float2}')

random_float3 = random.uniform(1,5)
print(f'Random float value between 1 to 5:{random_float3}')

love_score = random.randint(1,100)
print(f'Your love score : {love_score}')

print(f'Module imported value:{modulerandomisationpi.pi}')
