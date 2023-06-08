COLUMNS=10
ROWS=10
BLACK="\u25A2"
WHITE="\u25A0"
BOARD = [["" for _ in range(COLUMNS)] for _ in range(ROWS)]

def playAMove():
    coordinates=[0,0]
    while True:
        testInput=input("Please enter position: ")
        testInput=testInput.lower()
        #print(testInput)
        coordinates[0]=ROWS-int(testInput[0])-1
        if (int(testInput[0]) < 1 or int(testInput[0]) > 8):
            print("WRONG INPUT !!")
        else:
            if testInput[1] == "a":
                #print("A tempColumn")
                coordinates[1]=1
                #BOARD[ROWS-int(testInput[0])-1][1]=WHITE
                break
            elif testInput[1] == "b":
                #print("B tempColumn")
                coordinates[1] = 2
                break
            elif testInput[1] == "c":
                #print("c tempColumn")
                coordinates[1] = 3
                break
            elif testInput[1] == "d":
                #print("d tempColumn")
                coordinates[1] = 4
                break
            elif testInput[1] == "e":
                #print("e tempColumn")
                coordinates[1] = 5
                break
            elif testInput[1] == "f":
                #print("f tempColumn")
                coordinates[1] = 6
                break
            elif testInput[1] == "g":
                #print("g tempColumn")
                coordinates[1] = 7
                break
            elif testInput[1] == "h":
                #print("h tempColumn")
                coordinates[1] = 8
                break
            else:
                print("WRONG INPUT!!")
    #print(f"RETURN IS {coordinates}")
    return coordinates

def printMenu():
    print("1) Player vs Player")
    print("2) Player vs Bot (Player starts first)")
    print("3) Player vs Bot (Bot starts first)")
    print("4) EXIT ! ")

def printBoard():

    #Upper BORDER OF ABCDEFGH
    print(f"\t\t{BOARD[0][1]}\t\t{BOARD[0][2]}\t\t{BOARD[0][3]}\t\t{BOARD[0][4]}\t\t{BOARD[0][5]}\t\t{BOARD[0][6]}\t\t{BOARD[0][7]}\t\t{BOARD[0][8]}\t\t{BOARD[0][9]}\t")
    print("\t-----------------------------------------------------------------")

    #ITERATE THROUGH 1 to 8 because first and last rows are for BORDER
    for index, row in enumerate(BOARD[1:9], start=1):
        print(f"{row[0]}\t|\t{row[1]}\t|\t{row[2]}\t|\t{row[3]}\t|\t{row[4]}\t|\t{row[5]}\t|\t{row[6]}\t|\t{row[7]}\t|\t{row[8]}\t|\t{row[9]}\t")
        print("\t-----------------------------------------------------------------")

    # Lower BORDER OF ABCDEFGH
    print(f"\t\t{BOARD[9][1]}\t\t{BOARD[9][2]}\t\t{BOARD[9][3]}\t\t{BOARD[9][4]}\t\t{BOARD[9][5]}\t\t{BOARD[9][6]}\t\t{BOARD[9][7]}\t\t{BOARD[9][8]}\t\t{BOARD[9][9]}\t")


if __name__ == "__main__":

#declaring the border of the board ABDEFGH for upper and lower and 1-8 for left and right A=65 in ascii
    for i in range(ROWS):
        if (i==0 or i==9):
            pass
        else:
            BOARD[0][i]=chr(65+i-1)
            BOARD[9][i]=chr(65+i-1)
            BOARD[ROWS-i-1][0]=i
            BOARD[ROWS-i-1][9]=i



    while True:
        printMenu()
        choice=int(input("Please choose a game mode: "))
        if choice == 1:
            printBoard()
            while True:
                result = playAMove()
                row=result[0]
                column=result[1]
                if BOARD[row][column] != "":
                    print("BAD MOVE!")
                else:
                    if column < 5:
                        for index, tempColumn in enumerate(BOARD[row][1:(column + 1)], start=1):
                            if (tempColumn == "" and index != column) :
                                print("BAD MOVE!")
                                break
                            elif (index == column) :
                                BOARD[row][column] = WHITE
                                printBoard()
                    else:

                        for tempColumn in range(8, (column - 1), -1):
                            #print(tempColumn)
                            if (BOARD[row][tempColumn]== "" and tempColumn != column):
                                print("BAD MOVE!")
                                break
                            elif (tempColumn == column):
                                BOARD[row][column] = WHITE
                                printBoard()



        elif choice == 2:
            printBoard()
            break
        elif choice == 3:
            printBoard()
            break
        elif choice == 4:
            print("CYAA !!!")
            exit()
        else:
            print("Wrong Input!!")



