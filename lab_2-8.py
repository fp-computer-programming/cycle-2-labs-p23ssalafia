#Author: Sean Salafia 9/21/22

x = int (input('Input score to see if you should give up on your dreams!'))


if x <= 8: 
    print('Give up on your dreams')
else:
    if x <= 11:
        print('Almost! You got a bronze medal!')
    else:
        if x <= 14:
            print('Next time! You got a silver medal!')
        else: 
            print('Congrats! You won gold!')