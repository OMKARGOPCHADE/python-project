import os
import time

#function for displaying specified data from file
def s_disSpe_data():
     print()
     f = open('student','r');
     f_t = open('temp','w');
     roll_no = int(input("Enter a student roll no which you want to see: "));
     s =' '
     print()
     print("Given roll no student data featching wait...")
     time.sleep(5)
     print()
     while(s):
           s = f.readline();
           l=s.split("~");
           if len(s)>0:
                if int(l[0])==roll_no:
                     print("Roll No      : ",l[0])
                     print("Name         : ",l[1])
                     print("Age          : ",l[2])
                     print("Address      : ",l[3])
                     print("Email Address: ",l[4])
                     print("Contact No   : ",l[5])