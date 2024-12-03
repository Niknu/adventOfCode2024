#!/usr/bin/env python 3
import numpy as np
import re

data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# with open("/home/nicolai/git/privateGitHub/adventOfCode2024/3rd/input.txt", "r") as file:
    # data = file.read().rstrip()

#print(data)

if __name__ == "__main__":
    
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.search(pattern,data)

    removePattern = r"don't\(\)*?mul\((\d+),(\d+)\)"

    remove_matches = re.search(removePattern, data)

    print(remove_matches)
    
    result = 0 
    print(matches)
    for x, y in matches:
        result += int(y)*int(x)   
    print(result)
