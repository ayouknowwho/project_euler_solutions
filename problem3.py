# Copyright 2023 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# (outputs the solution 6857)

def findSmallestPrimeDivisor(dividend):
    currentSmallestPrimeDivisor=1
    for x in range (2,dividend):
        if (dividend%x == 0):
            currentSmallestPrimeDivisor=x
            break
    return currentSmallestPrimeDivisor

if __name__ == "__main__":
    a = 600851475143
    b = 1
 
    while (a > b):
        b = findSmallestPrimeDivisor(a)
        if (b == 1):
            break

        while (a%b == 0):
            a = (int(a / b))
  
 print('largest prime factor ' + str(a))
