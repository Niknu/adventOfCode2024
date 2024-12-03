#!/usr/bin/env python 3
import numpy as np


def is_safe(report):
    # Convert the report into a NumPy array
    report = np.array(report)
    #report = report.astype(np.int64)
    
    # Calculate the differences between adjacent levels
    diff = np.abs(np.diff(report))
    
    # Check if all differences are between 1 and 3 (inclusive)
    if not np.all((diff >= 1) & (diff <= 3)):
        return False
    
    # Check if the sequence is strictly increasing or strictly decreasing
    increasing = np.all(np.diff(report) > 0)
    decreasing = np.all(np.diff(report) < 0)
    
    return increasing or decreasing

def count_safe_reports(reports):
    # Use a list comprehension to count the number of safe reports

    reports = [list(map(int, report.strip(',').split(','))) for report in reports]

    safe_count = sum(is_safe(report) for report in reports)
    return safe_count



if __name__ == "__main__":
    

    # data = "7 6 4 2 1 \n" + "1 2 7 8 9 \n" + "9 7 6 2 1 \n" + "1 3 2 4 5 \n" + "8 6 4 4 1 \n" + "1 3 6 7 9 \n"

    # f = open("test.txt","w")
    # f.write(data)
    # f.close()


    with open("input.txt") as file:
        data = file.readlines()
        cleaned_data = [item.replace(" ", ",").strip() for item in data if item.strip()]
        count = count_safe_reports(cleaned_data)
        print(count)
    

        