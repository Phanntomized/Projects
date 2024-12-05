'''
In this problem you will write a function named isInteger that determines whether or not the characters in a string 
represent a valid integer. You will return True if it is an integer and False if it does not.

When determining if a string represents an integer you should ignore any leading or trailing white space. 
Once this white space is ignored, a string represents an integer if its length is at least one and it only contains digits, 
or if its first character is either + or - and the first character is followed by one or more characters, all of which are 
digits. You cannot use the built-in isdigit(), isnumeric(), isalnum(), isdecimal(), etc. functions. I want you to use in. 
You also cannot use lists, arrays, or any other tools we have not learned yet. Call the parameter “_users_stirng_” and 
allow the first character to be ‘&’ as well

Write at least 5 good test cases for this program that test various cases that would return True or False and your 
function returns the correct values.

'''

def isInteger(users_string):
    blank = 0
    if len(users_string) == 0:
        return False
    for i in range(len(users_string)):
        if users_string[i] == " ":
            blank += 1
        else:
            break
    if users_string[blank] in "+-&1234567890":
        blank += 1
        for i in range(len(users_string)):
            if users_string[i] in " -+&1234567890":
                continue
            else:
                return False
        return True
    else:
        return False
    
        
print(isInteger(""))