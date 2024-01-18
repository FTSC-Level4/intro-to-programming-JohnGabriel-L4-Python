# This is the first version that runs the if block 
alien_color = 'green'

if alien_color == 'green':
    print('You have gained 5 points for shooting the green alien!')

if alien_color > 'green':
    print('You have gained 10 points for shooting a non green alien!')

#second version with else
if alien_color == 'green':
    print('You have gained 5 points for shooting a green the alien!')
else:
    print('You have gained 10 points for shooting a non green alien!')
