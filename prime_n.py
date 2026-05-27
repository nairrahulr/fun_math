#!/usr/bin/env python

""" 
Prime Numbers

"""

__author__      = "Rahul Nair"
__credits__     = "Veritasium"
__date__        = "2024/12/18"
__deprecated__  = False
__email__       = "rahul7manu@gmail.com"
__maintainer__  = "Rahul Nair"
__status__      = "Development"
__version__     = "0.0.1"

import os
import sys
import time
import math

class Number:
    
    def __init__(self):
        pass
    
    def is_prime(self, n):
        # Check if the number is less than 2 or even
        if n < 2 or n % 2 == 0:
            if n != 2:
                return False
        else:
            # Check divisibility from 3 up to the square root of n
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
        return True
    
    def get_nearest_prime(self, n):
        prime_numbers = []
        
        if n >= 2:
            # Find nearest prime smaller than N
            for i in range(n - 1, n // 2, -1):
                if self.is_prime(i):
                    prime_numbers.append(i)
                    break
            
            # Find nearest prime greater than N
            for j in range(n + 1, 2 * n):
                if self.is_prime(j):
                    prime_numbers.append(j)
                    break
        else:
            prime_numbers.append(2)  # The smallest prime
        
        return prime_numbers
    
    def first_n_primes(self, n):
        primes = []
        num = 2  # Start checking from the first prime number
        
        while len(primes) < n:
            if self.is_prime(num):
                primes.append(num)
            num += 1
        
        return primes
    
    def is_perfect(self, n):
        if n <= 1:
            return False  # 1 and numbers less than or equal to 1 are not perfect
        
        # Find divisors and sum them up
        sum_of_divisors = 0
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sum_of_divisors += i
        
        # Check if the sum of divisors equals the number
        return sum_of_divisors == n

    def nearest_perfect_numbers(self, n):
        if self.is_perfect(n):
            return f"{n} is a perfect number."
        
        # Find the nearest previous perfect number
        prev_perfect = n - 1
        while not self.is_perfect(prev_perfect) and prev_perfect > 1:
            prev_perfect -= 1
        
        # Find the nearest next perfect number
        next_perfect = n + 1
        while not self.is_perfect(next_perfect):
            next_perfect += 1
        
        return [prev_perfect, next_perfect]
    
    def first_n_perfect_numbers(self, n):
        perfect_numbers = []
        number = 2  # Start checking from 2
        
        while len(perfect_numbers) < n:
            if self.is_perfect(number):
                perfect_numbers.append(number)
            number += 1
        
        # Calculate the differences between consecutive perfect numbers
        differences = [perfect_numbers[i] - perfect_numbers[i-1] for i in range(1, len(perfect_numbers))]
        
        return perfect_numbers, differences

def euler_perfect(p):
    return (2**p - 1)*(2**(p-1))

# Main code
if __name__ == "__main__":
    start_time = time.time()
    
    number = Number()
    input_number = 624097  # Example number; you can change this to any number
    
    for input_number in [4]:
        ### PRIME NUMBER
        print(f"{input_number} is prime?: {number.is_prime(input_number)}")
        nearest_primes = number.get_nearest_prime(input_number)
        if nearest_primes:
            print(f"Nearest prime: {nearest_primes}")
        
        ### PERFECT NUMBER
        # nearest_perfect_numbers = number.nearest_perfect_numbers(input_number)
        # print(f"Nearest perfect number: {nearest_perfect_numbers}")
        # perfect_numbers, differences = number.first_n_perfect_numbers(input_number)
        # print(f"The first {input_number} perfect numbers are: {perfect_numbers}")
        # print(f"The differences between consecutive perfect numbers are: {differences}")
        
    n_prime_list = number.first_n_primes(30)
    i=1
    for p in n_prime_list: #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        perfect = euler_perfect(p)
        print(f"{i}: {p}: {perfect}")
        i+=1
    
    # log the time taken to execute
    print('main() -> executed in', round(time.time() - start_time, 6), 'seconds!')