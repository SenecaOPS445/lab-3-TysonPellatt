#!/usr/bin/env python3
# Seneca ID: tpellatt
import os

def free_space():
    result = os.popen("df -h | grep '/$' | awk '{print $4}'").read()
    return result.strip()

if __name__ == '__main__':
    print(free_space())