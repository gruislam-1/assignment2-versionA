#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py
Author: G.M. REZWAN UL ISLAM
Semester: Fall 2024

The python code in this file is original work written by
"G.M. REZWAN UL ISLAM". No code in this file is copied from any other source
except those provided by the course instructor, including any person
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: assignment2-versionA

'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in human readable format")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    if percent < 0.0:
        percent = 0.0
    elif percent > 1.0:
        percent = 1.0

    # Calculate for hash symbols
    hash_symbol = int(percent * length)
    # Making the graph with hash symbols and spaces
    graph = "#" * hash_symbol + " " * (length - hash_symbol)

    return graph
# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    # Locating the total system memory from /proc/meminfo
    f = open('/proc/meminfo', 'r')
    for mem_info_file in f:
        if "MemTotal" in mem_info_file:
            total_mem_kb = int(mem_info_file.split()[1]) # MemTotal in kilobytes
            f.close()
            return total_mem_kb
    f.close()

def get_avail_mem() -> int:
    "return total memory that is available"
    # Locating the available system memory from /proc/meminfo
    f = open('/proc/meminfo', 'r')
    mem_free = 0
    swap_free = 0
    mem_available = False
    for mem_info_file in f:
        if "MemFree" in mem_info_file:
            mem_free = int(mem_info_file.split()[1])  # MemFree as integer
        elif "SwapFree" in mem_info_file:
            swap_free = int(mem_info_file.split()[1])  # SwapFree as integer
        elif "MemAvailable" in mem_info_file:
            mem_available = int(mem_info_file.split()[1])  # MemAvailable as integer

    f.close()
    if mem_available == False:  # When MemAavilable is not available/included
        return mem_free + swap_free # Returns sum of MemFree + SwapFree

    return mem_available


def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    ...

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    ...

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    # process args
    # if no parameter passed,
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.
