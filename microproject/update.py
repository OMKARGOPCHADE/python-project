import os
import time

#function for updating new data to file
def s_updt_data():
     f = open('student','r');
     f_t = open('temp','w');
     roll_no = int(input("Enter a student roll no which you want to update: "));
     s =' '
     print()
     while(s):
           s = f.readline();
           l=s.split("~");
           if len(s)>0:
                if int(l[0])==roll_no:
                    roll_no = input("Enter student roll no.: ");
                    name = input("Enter student name: ");
                    age = input("Enter student age: ");
                    address = input("Enter student address: ");
                    email_id = input("Enter student email-id: ");
                    contact = input("Enter student contact number: ");
                    f_t.write(roll_no+"~"+name+"~"+age+"~"+address+"~"+email_id+"~"+contact+"\n");
                else:
                     f_t.write(s);
     print()
     print("Given Data Updating...")
     time.sleep(5)
     print()
     print("Given Data Updated Successfully...")
     f.close();
     f_t.close();
     os.remove('student');
     os.rename('temp','student');