#!/usr/bin/env python 3
import numpy as np
import re

data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("/home/nicolai/git/privateGitHub/adventOfCode2024/3rd/input.txt", "r") as file:
    instruction_string = file.read().rstrip()

#if __name__ == "__main__":
#   
#    pattern = r"mul\((\d+),(\d+)\)"
#    matches = re.findall(pattern,data)
#
#    removePattern = r"don't\(\)*.?(mul\((\d+),(\d+))*.?do\(\)\)"
#    remove_matches = re.findall(removePattern, data)
#
#    #removePattern = r"don't\(\)*?.*do\(\)"
#    #remove_matches = re.findall(removePattern, data)
#
#    print(remove_matches)
#
#    result = 0 
#    print(matches)
#    for x, y in matches:
#        result += int(y)*int(x)   
#    print(result)




def process_instructions(instruction_string):
    # Initialize the state of mul (enabled at the start)
    mul_enabled = True
    total_sum = 0
    
    # Regular expression to match the relevant components: mul(a,b) and do()/don't()
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Split the input string by instructions
    parts = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", instruction_string)
    
    for part in parts:
        if re.match(mul_pattern, part):
            # If mul is enabled, process the multiplication
            match = re.match(mul_pattern, part)
            if match and mul_enabled:
                a, b = int(match.group(1)), int(match.group(2))
                total_sum += a * b
        elif re.match(do_pattern, part):
            # Enable mul
            mul_enabled = True
        elif re.match(dont_pattern, part):
            # Disable mul
            mul_enabled = False
    
    return total_sum

# The given string
#instruction_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Process the instructions
total_sum = process_instructions(instruction_string)
print(total_sum)