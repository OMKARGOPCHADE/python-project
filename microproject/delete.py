import os
import time

#function for deleting data from file
def s_del_data():
     f = open('student','r');
     f_t = open('temp','w');
     roll_no = int(input("Enter a student roll no which you want to delete: "));
     s =' '
     while(s):
           s = f.readline();
           l=s.split("~");
           if len(s)>0:
                if int(l[0])!=roll_no:
                     f_t.write(s);
     print("Data Deleting...")
     time.sleep(5)
     print()
     print("Data Deleted From File...")
     f.close();
     f_t.close();
     os.remove('student');
     os.rename('temp','student');