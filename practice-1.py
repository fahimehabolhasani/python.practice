side_1 =int(input('enter a number as triangle side:'))

side_2 =int(input('enter a number as triangle side:'))

side_3 =int(input('enter a number as triangle side:'))

if side_1<side_2+side_3 and side_2<side_1+side_3 and side_3<side_1+side_2:
    print('you can have a triangle')

else:
    print('enter another number the triangle is not drawn')