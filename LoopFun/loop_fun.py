

def main():
    height = int(input("Enter a box height (between 3 and 10): "))
    while not 3 <= height <= 10:
        height = int(input("Number is out of bounds: Try again: "))
    width = int(input("Enter a box width (between 6 and 20): "))
    while not 6 <= width <= 20 or height > width:
        height = int(input("Number is out of bounds: Try again: "))
    print()
    num = height
    avg = 0
    count = 0
    print(f"The integers from {height} to {width} are:")
    for i in range(width-height+1):
        print(num,end=" ")
        num += 1
        avg += num - 1
        count += 1
    print() 
    avg = avg/count
    print(f"and the average of those numbers is {avg}.")
    print()
    for i in range(width):
        print("*",end="")
    print()
    for i in range(height-1):
        print("*",end="")
        for i in range(width-2):
            print(" ",end="")
        print("*")
    
    for i in range(width):
        print("*",end="")

    num = 0
    for i in range(height):
        print()
        num += 1
        for i in range(num):
            print("**",end="")

if __name__ == '__main__':
    main() # don't change this
