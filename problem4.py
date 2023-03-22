# Copyright 2023 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# (Outputs the solution 906609)

def check_palindrome(str1):
    if (str1 == str1[::-1]):
        return True
    else:
        return False

if __name__ == "__main__":
    largest_palindrome = 1
    
    for x in range(1,1000):
        for y in range(1,1000):
            if (check_palindrome(str(x * y)) == True):
                if ((x * y) > largest_palindrome):
                    largest_palindrome=(x * y)
                    
 print(str(largest_palindrome))
