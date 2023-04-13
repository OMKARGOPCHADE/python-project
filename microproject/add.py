import os
import time
#function for adding new data to file
def s_add_data():
     f = open('student','a');
     roll_no = input("Enter student roll no.: ");
     name = input("Enter student name: ");
     age = input("Enter student age: ");
     address = input("Enter student address: ");
     email_id = input("Enter student email-id: ");
     contact = input("Enter student contact number: ");
     f.write(roll_no+"~"+name+"~"+age+"~"+address+"~"+email_id+"~"+contact+"\n");
     print()
     print("Adding Given student data to the file...")
     time.sleep(5)
     print()
     print("Given Data added to file successfully..")
     f.close()