#Author: Sean Salafia 9/21/22

x = int (input('Input score to see if you should give up on your dreams!'))


if x <= 8: 
    print('Give up on your dreams')
elif x <=11:
    print('Nice try! You got bronze')
elif x <=14:
    print('Almost! You got silver!')
else:
    print('Congrats! You got gold!')