

def main():
    height = int(input("Enter a box height (between 3 and 10): "))
    while not 3 <= height <= 10:
        height = int(input("Number is out of bounds: Try again: "))
    width = int(input("Enter a box width (between 6 and 20): "))
    while not 6 <= width <= 20 or height > width:
        height = int(input("Number is out of bounds: Try again: "))
    num = height
    avg = height
    count = 0
    print(f"The integers from {height} to {width} are:")
    for i in range(width-height+1):
        print(num,end=" ")
        num += 1
        avg += num
        count += 1
    print() 
    avg = avg/count
    print(f"and the average of those numbers is {avg}.")

    for i in range(width):
        print("*",end="")
    print()
    for i in range(height-2):
        print("*",end="")
        for i in range(width-2):
            print(" ",end="")
        print("*")
    
    for i in range(width):
        print("*",end="")


#delete this line
    # add your code here - suggested parts added

    # Part 1 - get user input

    # Part 2a - print numbers

    # Part 2b - calculate and print average of the numbers


    # Part 3 - print the hollow box


    # Part 4 - print the triangular shape

if __name__ == '__main__':
    main() # don't change this
