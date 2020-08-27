# TITA-DO
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:34:13 2020

@author: komeil parseh
"""
import pickle
import time

def write_file(data):
    """write data for TITA.DO"""
    file_tita = open('TITA.DO', 'wb')
    pickle.dump(data, file_tita)
    file_tita.close()
    return "write is", data, "in TATA.DO"

def load_file():
    """load data in TITA.DO"""
    file_tita = open('TITA.DO', 'rb')
    data = pickle.load(file_tita)
    file_tita.close()
    return data

print("You Todo with TITA-DO!")
print("     TITA-DO v2")
print("")
print("")

data_base = {}
NUMBER_TODO = 1

data = write_file(str(input("==> pleas enter your todo:")))
data_base[load_file()] = NUMBER_TODO
NUMBER_TODO += 1



OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
while OPERATOR_CASE != "1" and OPERATOR_CASE != "2":
    print("Your answer not found in program")
    print("Enter correct answer please")
    time.sleep(2)
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
    if OPERATOR_CASE == "1" or OPERATOR_CASE == "2":
        break

#پاسخ بله

while OPERATOR_CASE == "1":
    try:
        print("-> You Todo with TITA-DO! <-")
    except:
        print("Answer Error")
        print("Your answer is not found in program")
        print("Enter correct answer please")
        time.sleep(0.5)
        print("Your answer not found in program")
        print("Enter correct answer please")

    data = write_file(input(str("==>pleas enter your todo:")))
    data_base[load_file()] = NUMBER_TODO
    NUMBER_TODO += 1
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
while OPERATOR_CASE != "1" and OPERATOR_CASE != "2":
    print("Your answer not found in program")
    print("Enter correct answer please")
    time.sleep(0.5)
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
    if OPERATOR_CASE == "1" or OPERATOR_CASE == "2":
        break
    if OPERATOR_CASE == "2":
        break
#پاسخ خیر


if OPERATOR_CASE == "2":
    print("")
    print(data_base)
    print("  Thanks for using this program  ")
    print("             Goodbye             ")
    print("author", "==> TITA-DO <==", "Komeil Parseh")
    #time.sleep(3)
#تمام شد!
