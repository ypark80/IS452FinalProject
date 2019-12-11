import numpy as np
import random as rn
from graphics import *
import copy
import math


# Create the empty Sudoku puzzle
def template():
    template = []
    temp = []

    for i in range(9):
        for j in range(9):
            # print(i)´
            temp.append(0)
        if len(temp) == 9:
            template.append(temp)
            temp = []
    # print(template)
    return template


# Check if all cells are filled
def fullTemplate(temp):
    for row in range(len(temp)):
        for col in range(len(temp)):
            if temp[row][col] == 0:
                return False
    return True


# Define the 3 by 3 blocks in each template
def blockDef(temp):
    block = {}

    # Each block is created as a dictionary to reference easily in the later function blockNumber
    # I am not familiar with numpy, so I had to convert the 2D array to numpy and back to 2D array

    for row in range(len(temp)):
        for col in range(len(temp)):

            if row < 3:
                if col < 3:
                    temp = np.array(temp)
                    block[1] = temp[0:3, 0:3]
                elif col < 6:
                    temp = np.array(temp)
                    block[2] = temp[0:3, 3:6]
                else:
                    temp = np.array(temp)
                    block[3] = temp[0:3, 6:9]
            elif row < 6:
                if col < 3:
                    temp = np.array(temp)
                    block[4] = temp[3:6, 0:3]
                elif col < 6:
                    temp = np.array(temp)
                    block[5] = temp[3:6, 3:6]
                else:
                    temp = np.array(temp)
                    block[6] = temp[3:6, 6:9]
            else:
                if col < 3:
                    temp = np.array(temp)
                    block[7] = temp[6:9, 0:3]
                elif col < 6:
                    temp = np.array(temp)
                    block[8] = temp[6:9, 3:6]
                else:
                    temp = np.array(temp)
                    block[9] = temp[6:9, 6:9]

    return block


# Define the block number (left-right, top-bottom) based on row and column values
def blockNumber(row, col):
    number = 0
    if row < 3:
        if col < 3:
            number = 1
        elif col < 6:
            number = 2
        else:
            number = 3
    elif row < 6:
        if col < 3:
            number = 4
        elif col < 6:
            number = 5
        else:
            number = 6
    else:
        if col < 3:
            number = 7
        elif col < 6:
            number = 8
        else:
            number = 9

    return number


# Generate solutions of Sudoku
def solution(temp):
    for i in range(0, 81):
        row = i // 9
        col = i % 9

        # First check if the cell is empty
        if temp[row][col] == 0:
            rn.shuffle(numbers)

            # go through the numbers in the list
            for num in numbers:

                # Check that number is not used in the row
                if not (num in temp[row]):

                    # Check that number is not used in the column
                    if not num in (
                            temp[0][col], temp[1][col], temp[2][col], temp[3][col], temp[4][col], temp[5][col],
                            temp[6][col],
                            temp[7][col], temp[8][col]):

                        # Define the block based on the previous function
                        block = blockDef(temp)
                        j = blockNumber(row, col)

                        # Check that number is not used in the block
                        if num not in block[j]:
                            temp[row][col] = num

                            # Check if the template is full
                            if fullTemplate(temp):
                                return True

                            # If template is not full, it will repeate the above steps
                            else:
                                if solution(temp):
                                    return True
            break
    # If the number is not filled, then it will assign the value as 0
    temp[row][col] = 0


# Create the graphics for Sudoku
def graphicSudoku(temp):
    # Create the window for Sudoku
    win = GraphWin("Sudoku", 600, 600)
    win.setBackground("white")

    # Print messages in the window for warning
    important = Text(Point(300, 50), "*IMPORTANT*\nIf you click the screen it will quit")
    important.setTextColor("#8C1F1F")
    important.setSize(15)
    important.draw(win)

    i = 0
    j = 0

    # Draw vertical line with bold line to identify 3 by 3 block
    for p in range(3, 13):
        line = Line(Point(75 + i, 75), Point(75 + i, 75 + 450))
        if p % 3 == 0:
            line.setFill("#D95959")
            line.setWidth(3)
        else:
            line.setFill("#D99E91")
            line.setWidth(2)
        line.draw(win)
        i += 50

    i = 0
    j = 0

    # Draw horizontal line with bold line to identify 3 by 3 block
    for p in range(3, 13):
        line = Line(Point(75, 75 + i), Point(75 + 450, 75 + i))
        if p % 3 == 0:
            line.setFill("#D95959")
            line.setWidth(3)
        else:
            line.setFill("#D99E91")
            line.setWidth(2)
        line.draw(win)
        i += 50

    x = 0
    y = 0

    # Fill in each cell with number based on template
    for row in range(len(temp)):
        for col in range(len(temp)):
            prompt = Text(Point(100 + x, 100 + y), temp[row][col])
            prompt.setSize(30)
            prompt.setTextColor("#A66253")
            prompt.draw(win)
            x += 50
        x = 0
        y += 50

    # Wait for the mouse go to the window to quit
    win.getMouse()
    win.close()

def solutionGrahpics(puzzle, ans):
    # Create the window for Sudoku
    win = GraphWin("Sudoku", 600, 600)
    win.setBackground("white")

    # Print messages in the window for warning
    important = Text(Point(300, 50), "*IMPORTANT*\nIf you click the screen it will quit")
    important.setTextColor("#8C1F1F")
    important.setSize(15)
    important.draw(win)

    i = 0
    j = 0

    # Draw vertical line with bold line to identify 3 by 3 block
    for p in range(3, 13):
        line = Line(Point(75 + i, 75), Point(75 + i, 75 + 450))
        if p % 3 == 0:
            line.setFill("#D95959")
            line.setWidth(3)
        else:
            line.setFill("#D99E91")
            line.setWidth(2)
        line.draw(win)
        i += 50

    i = 0
    j = 0

    # Draw horizontal line with bold line to identify 3 by 3 block
    for p in range(3, 13):
        line = Line(Point(75, 75 + i), Point(75 + 450, 75 + i))
        if p % 3 == 0:
            line.setFill("#D95959")
            line.setWidth(3)
        else:
            line.setFill("#D99E91")
            line.setWidth(2)
        line.draw(win)
        i += 50

    x = 0
    y = 0

    # Fill in each cell with number based on template
    for row in range(len(ans)):
        for col in range(len(ans)):
            prompt = Text(Point(100 + x, 100 + y), ans[row][col])
            prompt.setSize(30)
            if (puzzle[row][col]==ans[row][col]):
                prompt.setTextColor("#A66253")
            else:
                prompt.setTextColor("#04BFBF")
            prompt.draw(win)
            x += 50
        x = 0
        y += 50

    # Wait for the mouse go to the window to quit
    win.getMouse()
    win.close()


# Remove the value from the ans to create the puzzle
def getPuzzle(temp, level):
    len1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Return different puzzle for difficulty levels
    if level == 'easy':
        x = rn.randint(10, 20)
        for i in range(x):
            row = rn.choice(len1)
            col = rn.choice(len1)
            temp[row][col] = None

    elif level == 'medium':
        x = rn.randint(20, 55)
        for i in range(x):
            row = rn.choice(len1)
            col = rn.choice(len1)
            temp[row][col] = None

    elif level == 'hard':
        x = rn.randint(55, 70)
        for i in range(x):
            row = rn.choice(len1)
            col = rn.choice(len1)
            temp[row][col] = None


# Ask the difficulty level of the game
def getLevel():
    # Get the difficult level from the user
    level = ''

    # Create the window for display
    win = GraphWin("Sudoku", 600, 600)
    win.setBackground("white")

    # Prints the directions for the step
    showLevels = Text(Point(300, 100), "Please choose the difficulty of Sudoku game \n Enter easy, medium or hard")
    showLevels.setSize(20)
    showLevels.setTextColor("#8C1F1F")
    showLevels.draw(win)

    levelEntry = Entry(Point(300, 300), 80)
    levelEntry.setFill("#F28D77")
    levelEntry.draw(win)

    # Click to move on to the next step
    win.getMouse()

    # Save the input text in level, which will be returned for later use
    levelText = levelEntry.getText()
    levelPrint = Text(Point(300, 200), levelText)
    level = levelPrint.getText()

    # if levelEntry.getText() == "easy":
    #     level = 'easy'
    # elif levelEntry.getText() == 'medium':
    #     level = 'medium'
    # elif levelEntry.getText() == 'hard':
    #     level = 'hard'

    # Click will close the window and move on to the next step
    win.getMouse()
    win.close()

    # print(len(level))

    return level


# Ask user whether to see the solution or not
def seeSolution():
    # Create the window for display
    win = GraphWin("Sudoku", 600, 600)
    win.setBackground("white")

    # Prints the directions for the step
    showResponse = Text(Point(300, 100), "Do you want to see the solution?\n Type either 'yes' or 'no' to continue")
    showResponse.setSize(20)
    showResponse.setTextColor("#8C1F1F")
    showResponse.draw(win)

    reseponseEntry = Entry(Point(300, 300), 80)
    reseponseEntry.setFill("#F28D77")
    reseponseEntry.draw(win)

    win.getMouse()

    # Save the input text in level, which will be returned for later use
    responseText = reseponseEntry.getText()
    responsePrint = Text(Point(300, 200), responseText)
    response = responsePrint.getText()

    win.getMouse()
    win.close()

    return response


# Shows ending screen with an image, when the user does not want to see the solution
def ifno():
    level = ''

    win = GraphWin("Sudoku", 600, 600)
    win.setBackground("white")

    endImage = Image(Point(300, 300), "end.gif")
    endImage.draw(win)

    # Click will close the window and move on to the next step
    win.getMouse()
    win.close()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
puzzle = template()
solution(puzzle)

# solution(empty) returns boolean value, and shallow copy will change the value whenever empty is changed
ans = copy.deepcopy(puzzle)

level = getLevel().lower()

levels = ["easy", "medium", "hard"]

# Repeat the getLevel() until level is in the levels list
while (level not in levels):
    getLevel()
    level = getLevel().lower()

getPuzzle(puzzle, level)

# print(puzzle)
# print(ans)

graphicSudoku(puzzle)

response = seeSolution().lower()

# print(len(anchorPoints))
# print(anchorPoints)
# print(len(ans))

yn = ['yes', 'no']

# Check if the user input is either 'yes' or 'no' and repeat until the user type 'yes' or 'no'
while (response not in yn):
    response = seeSolution().lower()

# Shows solution of the puzzle, with different color for the missing number
if response.lower() == 'yes':
    solutionGrahpics(puzzle,ans)
    ifno()

# Does not show the solution and only shows the image
else:
    ifno()

quit()
