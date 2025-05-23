'''
1. Set up board and read inputs from files

2. Create game loop

3. Update Board by 1 generation

4. Create cell count variable

5. Ask player which cells they want to add/remove

6. Check for win condition - 0 alive player cells

Functions required:

Print Board
Neighbors
Cell count

While loop ordering:
1. printing Board
2. updating board using Neighbors
3. give cell count
4. ask user which cell they want to add/delete using (x,y coordinate for each action)
5. check for win condition
'''

grid = []

player1Coordinates = open("player1.in", 'r')
player1Coords = []
coordinateList = player1Coordinates.readlines()
for coord in coordinateList:
  coord = [int(x) for x in coord.split()]
  player1Coords.append(coord)

player2Coordinates = open("player2.in", 'r')
player2Coords = []
coordinateList = player2Coordinates.readlines()
for coord in coordinateList:
  coord = [int(x) for x in coord.split()]
  player2Coords.append(coord)


for i in range(10):
  line = []
  for o in range(10):
    line.append(0)
  grid.append(line)

for coord in player1Coords:
  grid[coord[0]][coord[1]] = 1

for coord in player2Coords:
  grid[coord[0]][coord[1]] = 2

def printBoard(board):
  count = 0
  for row in board:
    if count == 0:
       print("  0 1 2 3 4 5 6 7 8 9")
    else:
      print()
    print(count, end = " ")
    count += 1
    for cell in row:
      if cell == 1:
        print("O", end = " ")
      elif cell == 2:
        print("X", end = " ")
      else:
        print("-", end = " ")


def neighbors(grid, alive, i, j):
    #Checking Neighbor count
  neighborCount = 0
  xCount = 0
  oCount = 0
 
  if grid[i-1][j-1] == 1 and i-1 >= 0 and j-1 >= 0:
    neighborCount += 1
    xCount += 1
  elif grid[i-1][j-1] == 2 and i-1 >= 0 and j-1 >= 0:
    neighborCount += 1
    oCount += 1

  if grid[i-1][j] == 1 and i-1 >= 0:
    neighborCount += 1
    xCount += 1
  elif grid[i-1][j] == 2 and i-1 >= 0:
    neighborCount += 1
    oCount += 1
    
  if i-1 >= 0 and j+1 < len(grid[0]) and grid[i-1][j+1] == 1:
    neighborCount += 1
    xCount += 1
  elif i-1 >= 0 and j+1 < len(grid[0]) and grid[i-1][j+1] == 2:
    neighborCount += 1
    oCount += 1
    
  if grid[i][j-1] == 1 and j-1 >= 0:
    neighborCount += 1
    xCount += 1
  elif grid[i][j-1] == 2 and j-1 >= 0:
    neighborCount += 1
    oCount += 1
    
  if j+1 < len(grid[0]) and grid[i][j+1] == 1: 
    neighborCount += 1
    xCount += 1
  elif j+1 < len(grid[0]) and grid[i][j+1] == 2: 
    neighborCount += 1
    oCount += 1
    
  elif j+1 < len(grid[0]) and i+1 < len(grid) and grid[i+1][j+1] == 1:
    neighborCount += 1
    xCount += 1
  if j+1 < len(grid[0]) and i+1 < len(grid) and grid[i+1][j+1] == 2:
    neighborCount += 1
    oCount += 1  
    
  if i+1 < len(grid) and grid[i+1][j] == 1:
    neighborCount += 1
    xCount += 1
  elif i+1 < len(grid) and grid[i+1][j] == 2:
    neighborCount += 1
    oCount += 1    
    
  if i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == 1:
    neighborCount += 1
    xCount += 1
  elif i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == 2:
    neighborCount += 1
    oCount += 1
    
#Rule 1: Checking if the cell will die due to underpopulation
  if neighborCount < 2 and (alive == 1 or alive == 2):
    return 0
    
  # Rule 2: Checking if the cell wil live
  elif neighborCount < 4 and (alive == 1 or alive == 2):
    return alive
  
  # Rule 3: Checking if the cell dies due to overpopulation  
  if alive == 1 or alive == 2:
    return 0
    
  # Rule 4: Checking if a new cell wil be born  
  if alive == 0 and neighborCount == 3:
    if xCount > oCount:
      return 1
    else:
      return 2

def cellCount(grid):
  #returns [xcount, ocount]
  xCount = 0
  oCount = 0
  for row in grid:
    for cell in row:
      if cell == 1:
        xCount += 1
      elif cell == 2:
        oCount += 1
  return [xCount, oCount]

  
#Starting the game

input("Welcome to Conway's 2-Player Game of Life. We start \nwith a 10x10 grid of cells, either alive or dead. \nHere are the rules:\n\t Each player starts with a square. Each turn they \nget to pick a position to grow a cell and pick a \nposition to kill an opponent cell. Each generation \npasses by following these rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:")

printBoard(grid)


input("\n Press Enter to start: ")
playerTurn = True
while True:
  print("\033c")
  newGrid = []
  for i in range(10):
    row = []
    for j in range(10):
      row.append(0)
    newGrid.append(row)

  print("Here's your new grid.")

  for i in range(len(grid)):
    for o in range(len(grid[0])):
      newGrid[i][o] = neighbors(grid,grid[i][o],i,o)
  printBoard(newGrid)
  grid = newGrid
  
  #Counting Cells
  
  score = cellCount(grid)
  print("\nPlayer O has: " + str(score[0]) + " cells alive")
  print("Player X has: " + str(score[1]) + " cells alive")  
  
  #Win Detection
  
  if score[0] == 0 or score[1] == 0:
    break

  
   #Turn Taking mechanism
   
  if playerTurn == True:
    playerTurn = False
    
    print("It's Player X's turn")
    colAdd = input("What is the column of the cell you'd like to add? ")
    rowAdd = input("What is the row of the cell you'd like to add? ")
    
    colDel = input("\nWhat is the column of the cell you'd like to delete? ")
    rowDel = input("What is the row of the cell you'd like to delete? ")
  
    newGrid[int(rowAdd)][int(colAdd)] = 2
    newGrid[int(rowDel)][int(colDel)] = 0
    
  else:
    playerTurn = True
    print("It's Player O's turn")
    colAdd = input("What is the column of the cell you'd like to add? ")
    rowAdd = input("What is the row of the cell you'd like to add? ")
    
    colDel = input("\nWhat is the column of the cell you'd like to delete? ")
    rowDel = input("What is the row of the cell you'd like to delete? ")
    
    grid[int(rowAdd)][int(colAdd)] = 1
    grid[int(rowDel)][int(colDel)] = 0
  
if score[0] > score[1]:
  print("Player O won the game!")
elif score[1] > score[0]:
  print("Player X won the game!")
else:
  print("Tie!")
