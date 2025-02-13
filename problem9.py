# Copyright 2025 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Find the pythagorean triplet for which a + b + c = 1000, and print the product abc.
#
# Prints the solution 31875000

TARGET = 1000

def check_pythagorean(a,b,c):
    if (a < b) and (b < c) and (a**2 + b**2 == c**2):
        return True
    else:
        return False
    
for a in range(0,1000):
    bc_target = TARGET - a
    for b in range(a + 1, bc_target):
        c = bc_target - b
        if check_pythagorean(a, b, c):
            print(a * b * c)
            found = True
            break
    else:
        continue
    break
