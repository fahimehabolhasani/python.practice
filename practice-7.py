def chess_board(r,c):
    for row in range(r):
         board = ""
         for column in range(c):
            if r % 2 == 0:
                board += "#*"
            else:
                board += "*#"
         print(board)


n =int( input("enter number of rows:"))
m=int(input("enter number of columns:"))

# print("\n")
chess_board(n,m)