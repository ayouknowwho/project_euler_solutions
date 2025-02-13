# Copyright 2023 by ayouknowwho

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# (outputs the solution 232792560)

# lowest possible solution is 2520
trial_solution = 2520

# all other divisors are remainder 0 if this set of divisors are remainder 0
important_divisors = set([20,19,18,17,16,14,13,11]) 

all_success = False
while all_success == False:
    #loop will end if every divisor is remainder 0
    for x in important_divisors:
        if trial_solution%x == 0:
            continue
        else:
            #iterate if a divisor is not remainder 0
            all_success=False
            trial_solution = trial_solution+2520
            break
    all_success = True

print(str(trial_solution))
