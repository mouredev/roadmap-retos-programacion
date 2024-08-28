#Define matrix

matrix = [["🐭","⬜️","⬜️","⬜️","⬜️","⬛️"],
          ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️"],
          ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️"],
          ["⬜️","⬜️","⬜️","⬜️","⬛️","⬛️"],
          ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️"],
          ["⬛️","⬜️","⬛️","⬜️","⬜️","🚪"]]


def print_matrix():
    for row in matrix:
        row_string = ""
        for column in row:
            row_string+=column

        print(row_string)

#Mickey's initial position
mickey_pos = [0,0]
prev_value="⬜️"
print_matrix()
while True:
    print("Enter left to move to the left")
    print("Enter right to move to the right")
    print("Enter up to move up")
    print("Enter down to move down")
    print("Enter exit to termiante the program")
    option = str(input("Enter option ")).lower()

    if option == "left":
        if mickey_pos[1] - 1 < 0:
            print("Imposible to move outsite the limits")
        else:
            if matrix[mickey_pos[0]][mickey_pos[1]-1] == "⬛️":
                print("Imposible to move there is an obstacle")
            else:    
                matrix[mickey_pos[0]][mickey_pos[1]] = prev_value
                prev_value = matrix[mickey_pos[0]][mickey_pos[1]-1]
                mickey_pos[1]-=1
                matrix[mickey_pos[0]][mickey_pos[1]]="🐭"
              
    elif option == "right":
        if mickey_pos[1] + 1 > 5:
            print("Imposible to move outsite the limits")
        else:
            if matrix[mickey_pos[0]][mickey_pos[1]+1] == "⬛️":
                print("Imposible to move there is an obstacle")
            else:    
                matrix[mickey_pos[0]][mickey_pos[1]] = prev_value
                prev_value = matrix[mickey_pos[0]][mickey_pos[1]+1]
                mickey_pos[1]+=1
                matrix[mickey_pos[0]][mickey_pos[1]]="🐭"
    elif option == "up":
        if mickey_pos[0] - 1 < 0:
            print("Imposible to move outsite the limits")
        else:
            if matrix[mickey_pos[0]-1][mickey_pos[1]] == "⬛️":
                print("Imposible to move there is an obstacle")
            else:    
                matrix[mickey_pos[0]][mickey_pos[1]] = prev_value
                prev_value = matrix[mickey_pos[0]-1][mickey_pos[1]]
                mickey_pos[0]-=1
                matrix[mickey_pos[0]][mickey_pos[1]]="🐭" 
    elif option == "down":
        if mickey_pos[0] +1 > 5:
            print("Imposible to move outsite the limits")
        else:
            if matrix[mickey_pos[0]+1][mickey_pos[1]] == "⬛️":
                print("Imposible to move there is an obstacle")
            else:    
                matrix[mickey_pos[0]][mickey_pos[1]] = prev_value
                prev_value = matrix[mickey_pos[0]+1][mickey_pos[1]]
                mickey_pos[0]+=1
                matrix[mickey_pos[0]][mickey_pos[1]]="🐭"
    elif option == "exit":
        break
    else:
        print("Incorrect option, please try again")

    #Check if it is the end
    if prev_value == "🚪":
        print("Exit has been found...") 
        break   
    print_matrix()      