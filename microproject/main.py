import os
import time
import add
import delete
import dis_all
import dis_sp
import update
#python microproject created by Mr.Gopchade Omkar Using File-Handling

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
       add.s_add_data()
#second choice function called..
 elif choice=="2":
          delete.s_del_data()
#third choice function called..
 elif choice=="3":
      update.s_updt_data() 
#fourth choice function called.. 
 elif choice =="4":
      dis_all.s_disAll_data() 
#fifth choice function called..         
 elif choice=="5":
      dis_sp.s_disSpe_data()
#exit..
 elif choice=="6":
         print("Existing The System...")
         print()
         time.sleep(4)
         print("Thank You For Visiting...!")
         break
#Thank you for reading my code..