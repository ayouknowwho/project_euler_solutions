# Copyright 2025 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Find the summation of primes below two million
#
# Prints the solution 142913828922

MAX = 2000000

# Array of bools for sieve of Eratosthenes
is_prime = [True] * (MAX - 1)
summation = 0

for i in range(2, MAX):
    if is_prime[i - 1]:
        summation += i
        not_prime = i * 2
        while not_prime < MAX:
            is_prime[not_prime - 1] = False
            not_prime += i
    
print(summation)
