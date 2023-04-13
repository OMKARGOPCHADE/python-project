import os
import time

#function for displaying all data from file
def s_disAll_data():
     print()
     print("Featching Data Wait...")
     time.sleep(5)
     print()
     f = open('student','r');
     for i in f:
           l=i.split("~");
           for j in l:
              print(" ",j,end="");
     f.close()