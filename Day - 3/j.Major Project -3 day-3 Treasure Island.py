#Project for Treasure Island Program by choosing the path and then finally the correct door.

print('''
   \.   \.      __,-"-.__      ./   ./
           \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
            \`.  \_`-''      _,="=._      ``-'_/  .'/
             \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
          \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
           \`-'  /    `-._  "       "  _.-'    \  `-'/
           /)   (         \    ,-.    /         )   (\
        ,-'"     `-.       \  /   \  /       .-'     "`-,
      ,'_._         `-.____/ /  _  \ \____.-'         _._`,
     /,'   `.                \_/ \_/                .'   `,\
    /'       )                  _            Krogg (       `\
            /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
           / ,-'        \/|`|`|`|'|'|'|\/        `-, \
          /,'             | | | | | | |             `,\
         /'               ` | | | | | '               `\
                            ` | | | '
                              ` | '

''')

print('Welcome to Tresure Island.')
print('Your mission is to find the treasure.')
path  = input('You are at a crossroad, Where do you want to go ?Type "left" or "right"').lower()

if path=='left':
    path2 = input('you have come to a lake .There is an island in the middle of the lake.Type "wait" to wait for the boat! or "swim" to  swim across the lake').lower()
    if path2=='wait':
        path3 = input('you are arrived at the island unharmed. There is a house of 3 doors.One red,One yellow and One blue.Which color do you choose?').lower()
        if path3 == 'red':
            print("It's a room full of fire.Game Over!")
        elif path3 == 'yellow':
            print("You found the treasure! You Own!")
        elif path3 == 'red':
            print("You entered room of beasts.Game Over!")
        else:
            print('You choose a door that does not exists!')
    else:
        print('you are attacked by angry trout.Game Over!')
else:
    print('Game Over')




