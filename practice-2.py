score_1=float(input('enter score:'))
score_2=float(input('enter score:'))
score_3=float(input('enter score:'))

average=(score_1 + score_2+score_3)/3
if average >= 17 :
    print('student:greate')
elif average <17 and average >12:
    print('student:normal')
elif average <12:
    print('student:fail')
else:
    print('wrong characters ')