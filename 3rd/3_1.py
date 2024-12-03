#!/usr/bin/env python 3
import numpy as np
import re

#data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("/home/nicolai/git/privateGitHub/adventOfCode2024/3rd/input.txt", "r") as file:
    data = file.read().rstrip()

print(data)

if __name__ == "__main__":
    
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern,data)
    
    result = 0 
    for x, y in matches:
        result += int(y)*int(x)   
    print(result)
