#date: 24/10/2019
#name: sasha kuechenmeister
#student id: c18404082
#titel: labtest 1
#programmes description: Pascal Triangle Program

#global variables
replay = "y"
answer = "nNyY"
yes_answer = "yY"
no_answer = "nN"

while replay in yes_answer: #runs program until user chooses to exit

    def make_new_row(old_row):
        if old_row == 0:
            return [1]
        else:
            N = make_new_row(old_row-1)
            return [1] + [N[i] + N[i+1] for i in range(old_row-1)] + [1]

    def TrianglePascal(old_row):  #creates a triangle of n number of rows
        triangle = []
        for i in range(old_row):
            triangle.append(make_new_row(i))
        return triangle

    if __name__ == '__main__': #prints the pascal triangle
        user_input = int(input("enter desired size of triangle: ")) #asks user to enter size of triangle
        for i in TrianglePascal(user_input): #outputs one line at a time
            print(i)

    replay = input("would you like to enter a new size for the triangle? y/n") #Asks user if they wish to enter a new number or exit the program
    while replay in answer:
        if replay in no_answer:
            break
        else:
            break
    while replay not in answer: #if user enters an invalid character
        print("y to play again, n to exit")
        replay = input("play again? y/n")