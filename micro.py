import os
import time
#python microproject created by Mr.Gopchade Omkar Using File-Handling
#functions are listed below

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
#functions completed...

#actual view of project..                     
print()
print("|| HELLO WELCOME TO GPH STUDENT MANAGEMENT SYSTEM ||");
print()
print()
#loop for itrate till user leaves the system or exits the system..
while(True):
 print()
 print("1. Add");
 print("2. Delete");
 print("3. Update");
 print("4. Display All Data");
 print("5. Display Specified Roll.no Data")
 print("6. Exit")
 print();

#getting choice from user
 choice = input("Enter Your Choice: ");

#first choice function called..
 if choice == "1":
       s_add_data()
#second choice function called..
 elif choice=="2":
          s_del_data()
#third choice function called..
 elif choice=="3":
      s_updt_data() 
#fourth choice function called.. 
 elif choice =="4":
      s_disAll_data() 
#fifth choice function called..         
 elif choice=="5":
      s_disSpe_data()
#exit..
 elif choice=="6":
         print("Existing The System...")
         print()
         time.sleep(4)
         print("Thank You For Visiting...!")
         break
#Thank you for reading my code..