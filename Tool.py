# Basic School Administration Tool
import csv

#function
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(info_list)

#condition
if __name__ == '__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter Student information for student #{} in following  format (Name Age Contact_number Email_ID) : ".format(student_num))


        #split
        student_info_list = student_info.split(' ')

        print("The Entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-Mail ID: {}".format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is entered information correct? (yes/no) ")

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter another student information : ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
                print("\nPlease re-enter the values!")
#output
#Enter Student information for student #1 in following  format (Name Age Contact_number Email_ID) : satyam 65 667 777
#The Entered information is -
#Name: satyam
#Age: 65
#Contact_number: 667
#E-Mail ID: 777
#Is entered information correct? (yes/no) yes
#Enter (yes/no) if you want to enter another student information : no



