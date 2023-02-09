# Author NDO 02/08/23

# Sudoku Board Validator

# Create a funciton that validates any sudoku board 
class Solution(object):
   def isValidSudoku(self, board):
      """
      :type board: List[List[str]]
      :rtype: bool
      """
      # create a loop that accounts for the placement of number 1-9 across the columns and rows of the board
      for i in range(9):
         row = {}
         column = {}
         block = {}
         row_cube = 3 * (i//3)
         column_cube = 3 * (i%3)
         for j in range(9):
            if board[i][j]!='.' and board[i][j] in row:
               return False
         row[board[i][j]] = 1
         if board[j][i]!='.' and board[j][i] in column:
            return False
         column[board[j][i]] = 1
         rc= row_cube+j//3
         cc = column_cube + j%3
         if board[rc][cc] in block and board[rc][cc]!='.':
            return False
         block[board[rc][cc]]=1
      return True
      # return if the board is either valid or invalid with true or false statements 
ob1 = Solution()
      #printed example of valid sudoku board 
print(ob1.isValidSudoku([
   ["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]]))


# Pure odd digit primes 
# create a function that accounts for primes numbers in the sequence 
def is_prime(n):
    return n > 1 and all(n % i for i in range(3, int(n**0.5)+1, 2))
# create a function that accounts for odd numbers in the sequence 
def only_odd_digits(n):
    return all(int(x) % 2 for x in str(n))
# create a  function that accounts for the next prime number in the sequence 
def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n
# created a function that selectively returns the pure odd primes digits in any sequence 
def only_oddDigPrimes(n):
    res = [i for i in range(n+1) if is_prime(i) and only_odd_digits(i)]
    while True:
        n = next_prime(n)
        if only_odd_digits(n):
            return [len(res), res[-1], n]

# [number pure odd digit primes bellow n,
# largest pure odd digit prime smaller than n,
# smallest pure odd digit prime higher than n]


q = only_oddDigPrimes(20), [7, 19, 31]
q
q = only_oddDigPrimes(40), [9, 37, 53]
q
q = only_oddDigPrimes(55), [10, 53, 59]
q
q = only_oddDigPrimes(60), [11, 59, 71]
q

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

# Even Fibonacci Sum 
def fib(n):
    '''
    Generate next term in Fibonacci sequence.
    Append next term to list.
    Return list of Fibonacci terms.
    '''
    a,b = 1,1
    while b <= n:
        a,b = b,a+b
        fib_sequence.append(a)
    return fib_sequence

def find_even_terms(n):
    '''
    Loop through elements in list to find even terms.
    Keep running total of even terms.
    Return sum of even terms.
    '''
    sum_even_terms = 0
    for n in fib_sequence:
        if n % 2 == 0:
            print (n)
            sum_even_terms = sum_even_terms + n
    return sum_even_terms

fib_sequence = []
x = fib(4000000)
print ("Sum of even Fibonacci terms: ") + str(find_even_terms(x))