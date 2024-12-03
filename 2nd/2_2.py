#!/usr/bin/env python 3
import numpy as np

def is_safe(report):
    """
    Checks if a given report is safe (strictly increasing or strictly decreasing with valid differences).
    """
    # Convert the report to a numpy array
    report = np.array(report)
    
    # Compute the differences between adjacent levels
    diffs = np.diff(report)
    
    # Check if all differences are between 1 and 3
    if not np.all((diffs >= 1) & (diffs <= 3)):
        return False
    
    # Check if the sequence is either strictly increasing or strictly decreasing
    if np.all(diffs > 0) or np.all(diffs < 0):
        return True
    return False

def is_safe_with_removal(report):
    """
    Checks if a report is safe, considering the Problem Dampener, which allows removal of one level.
    """
    # First, check if the report is already safe
    if is_safe(report):
        return True
    
    # Try removing each level one by one and check if the resulting report is safe
    n = len(report)
    for i in range(n):
        # Create a modified report with the i-th level removed
        modified_report = np.delete(report, i)
        # Check if this modified report is safe
        if is_safe(modified_report):
            return True
    
    return False

def count_safe_reports(reports):
    """
    Counts how many reports are safe either by removal of a single level or without removal.
    """
    # Convert each report string to a list of integers
    reports = [list(map(int, report.strip(',').split(','))) for report in reports]
    
    # Apply is_safe_with_removal function to each report and count the safe ones
    safe_count = sum(is_safe_with_removal(report) for report in reports)
    
    return safe_count


if __name__ == "__main__":
    

    # data = "7 6 4 2 1 \n" + "1 2 7 8 9 \n" + "9 7 6 2 1 \n" + "1 3 2 4 5 \n" + "8 6 4 4 1 \n" + "1 3 6 7 9 \n"

    # f = open("test.txt","w")
    # f.write(data)
    # f.close()


    with open("test.txt") as file:
        data = file.readlines()
        cleaned_data = [item.replace(" ", ",").strip() for item in data if item.strip()]

        print(cleaned_data)

        count = count_safe_reports(cleaned_data)
        print(count)
    