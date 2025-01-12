'''

    2D Map Visualizer by Dyo.ed

    This code transforms your 2D Array into a
    more readable Grids.

    -----------------------------------------------------

    INSTRUCTION:
    - Coordinates are written as [Yaxis][Xaxis]
    - Jagged Array does not work
    - Separate Tab Text accepts One-Dimensional Array

    HOW TO USE:
    drawMap(map, position, direction)   -       Visualize the 2D Array into recognizable Grids
        [ map ]                         -       Accepts 2D Array with values 0, 1, and 2
                                                    0 - Blocked Paths
                                                    1 - Open Paths
                                                    2 - Goal/s
        [ position ]                    -       Accepts One-Dimensional Array currentPosition[ Y, X ]
                                                    Y - Y Axis (Vertical)
                                                    X - X Axis (Horizontal)
        [ direction ]                   -       Accepts one lowercase strings ('up', 'down', 'left, 'right')

    toggleSeparateBar()                 -      To enable/disable the separate bar which can display texts.

    changeIndentation(amount)           -      Adjust Indent from Left Window to the Grid Visualization
                                                    [ amount ]    -   Accepts integer value

    changeIndentSB(amount)               -      Adjust Indent from Grid Visualization to Separate Tab
                                                    [ amount ]    -   Accepts integer value

    addTextSB(array)                     -      Add Text to be displayed in the Separate Tab
                                                    [ array ]     -   Accepts One-Dimensional Array preferable Strings

    changeGoalSymbol(text)               -      Replace the Goal Symbol with your liking
                                                    [ text ]     -    Accepts String preferable one Character only

'''

class Setup:
    colorGreen  =    '\033[32m'
    colorBlue   =    '\033[34m'
    colorRed    =    '\033[31m'
    colorReset  =    '\033[0m'

    textSB      =    [f'Sample Text #{i+1}' for i in range(5)]
    separateBar =    False
    goalSymbol  =    '🏳'
    indentSB    =    3
    indexSB     =    0
    indent      =    2


    def toggleSeparateBar():        Setup.separateBar   =   not Setup.separateBar
    def changeIndentation(amount):  Setup.indent        =   amount
    def changeIndentSB(amount):     Setup.indentSB      =   amount
    def addTextSB(array):           Setup.textSB        =   array
    def changeGoalSymbol(text):     Setup.goalSymbol    =   text


def drawMap(mazeMap, currentPosition, directionFacing):

    rows, columns = len(mazeMap), len(mazeMap[0]) if mazeMap else 0
    Setup.indexSB = 0

    for Yaxis in range(rows):
        print("\n" + "\t" * Setup.indent + "+-------" * columns, end="+")
        if Setup.separateBar: separateTab()
         
        for columnSeparator in range(3):
            print("\n" + "\t" * Setup.indent, end="")

            for Xaxis in range(columns + 1):
                print(end="|")

                for columnSpacing in range(7):
                    if Xaxis != columns and mazeMap[Yaxis][Xaxis] == 0:
                        print({(1, 0): "\\", (5, 0): "/", (3, 1): "X", (1, 2): "/", (5, 2): "\\"}
                              .get((columnSpacing, columnSeparator), " "), end="")
                        
                    elif columnSpacing == 3 and columnSeparator == 1 and Xaxis != columns:
                        print(f"{Setup.colorGreen}{'↑←↓→'[['up', 'left', 'down', 'right'].index(directionFacing)]}{Setup.colorReset}" 
                        if Yaxis == currentPosition[0] and Xaxis == currentPosition[1]
                        else (f"{Setup.colorGreen}{Setup.goalSymbol}{Setup.colorReset}" if mazeMap[Yaxis][Xaxis] == 2
                        else " "), end="")

                    else: print(" ", end="")

            if Setup.separateBar: separateTab(True)

    print("\n" + "\t" * Setup.indent + "+-------" * columns, end="+")
    if Setup.separateBar: separateTab()

def separateTab(toggle=False):
    print("\t" * (Setup.indentSB - 1 if toggle else Setup.indentSB), end="|\t")

    print("Separate Tab Title" if Setup.indexSB == 0 else (Setup.textSB[Setup.indexSB-2] 
    if Setup.indexSB > 1 and len(Setup.textSB) > Setup.indexSB-2 else ""), end="")
    Setup.indexSB += 1
