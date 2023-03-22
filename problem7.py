# Copyright 2023 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# What is the 10 001st prime number?
#
# Prints the solution 104743

current_integer = 3
primes_found = 1 # skip past prime 1 = 2, as can't do range (2,2)

while (primes_found < 10001):
	for x in range(2, current_integer):
		if (current_integer%x == 0):
			break
		if (current_integer - 1 == x):
			primes_found = primes_found + 1
	current_integer = current_integer + 1
print(str(current_integer - 1))
