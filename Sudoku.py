"""
@author: Quynh Le (Hana)
@date: April 1, 2023
"""
print("Let's play Sudoku!")
print("Enter a filename: ")

filename = input()
with open(filename, 'r') as f:
  info = f.readlines()

matrix = []

#Loop through each row in the file and convert to integers
for i in range(len(info)):
  row = info[i].strip().split(" ")
  temp = []
  for j in range(len(row)):
    temp.append(int(row[j]))
  matrix.append(temp)
  

#Find empty cells
def findEmpty(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j)
  return None

  
#Check if a number is in a valid cell
def valid(board, num, pos):
  row = pos[0]
  col = pos[1]

  #Check rows
  for i in range(len(board[0])):
    if board[row][i] == num and col != i:
      return False

  #Check columns
  for i in range(len(board)):
    if board[i][col] == num and row != i:
      return False

  #Check 3x3 grid
  startRowIndex = row // 3
  startColIndex = col // 3
  for i in range(startRowIndex * 3, (startRowIndex * 3) + 3):
    for j in range(startColIndex * 3, (startColIndex * 3) + 3):
      if board[i][j] == num and row != i and col != j:
        return False
  return True


#Solve the Sudoku puzzle recursively using backtracking
def solve(board):
  emptyCell = findEmpty(board)

  if not emptyCell:
    return True
  else:
    row, col = emptyCell

  #Try each number from 1 to 9 in the empty cell
  for num in range(1, 10):
    #If the number is valid for the empty cell, assign it to the cell and recursively solve the board
    if valid(board, num, emptyCell):
      board[row][col] = num
      if solve(board):
        return True
      #If not valid, try the next number
      else:
        board[row][col] = 0

  #If no number solves the board, backtrack to the previous cell and try a different number
  return False

  
#Print the unsolved puzzle and the solution
def printBoard(board):
  if not findEmpty(board):
    print()
    print("The solution: ")
  else:
    print()
    print("The original puzzle: ")

  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("—————————————————————")
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print("| ", end="")
      print(str(board[i][j]) + " ", end="")
    print('')
    
#Main program
printBoard(matrix)
solve(matrix)
printBoard(matrix)
