# Copyright 2023 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Find the difference between "the sum of the squares of the first one hundred natural numbers" and "the square of the sum of the first one hundred natural numbers".
#
# (outputs the solution 25164150)

a = 0
b = 0
for x in range (1,101):
    a = a + (x ** 2)
    b = b + x
b = b ** 2
print(str(b - a))
