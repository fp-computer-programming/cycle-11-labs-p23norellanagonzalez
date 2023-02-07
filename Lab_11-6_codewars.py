# author NDO 02/06/23

# Simple reversed parenthesis 

# create a function that finds the length of the string and returns that it is not possible if the number of parenthesis are odd
def solve(s):
    if len(s) %2: return -1
    # The height and counter represent the "(" and ')' which indicates that if we have a bigger number of either they would have to be reversed to pair 
    height = 0 ; counter = 0 
    # the x represents the variable for the parenthesis which helps to indicate the number of pairs required 
    for x in s: 
        if x == '(' : 
            height += 1 
        else:
            height -= 1 
        if height < 0 :
            counter += 1 
            height += 2 
    #Once the amount of parenthesis has been found half of it would be the amount of pairs that can be formed after reversal 
    return counter + height // 2 
