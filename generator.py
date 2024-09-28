import os
import re

params = {}

def get_params():
   
    with open('./config/.config', 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                params[key] = value
                print(params[key])

def create_c_and_h_files(filename):
    # 创建.c文件
    c_filename = f"{filename}.c"
    with open(c_filename, 'w') as c_file:
        c_file.write(f'#include "{filename}.h"\n\n')
        c_file.write('// C source code goes here\n')
    
    # 创建.h文件
    h_filename = f"{filename}.h"
    with open(h_filename, 'w') as h_file:
        h_file.write(f'#ifndef {filename.upper()}_H\n')
        h_file.write(f'#define {filename.upper()}_H\n\n')
        h_file.write('// Function declarations and other definitions go here\n\n')
        h_file.write(f'#endif // {filename.upper()}_H\n')
    
    print(f"Files '{c_filename}' and '{h_filename}' created successfully.")

if __name__ == "__main__":
    get_params()
    filename = input("Enter the base filename (without .c or .h): ")
    create_c_and_h_files(filename)


# 



# print(params)