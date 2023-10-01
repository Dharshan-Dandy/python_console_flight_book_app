#CCC Fuse Error
#--------------------------------------------------
#--------------FLIGHT BOOKING SYSTEM---------------
#__________________________________________________
#Sign Up Module:

import re
import datetime

#prettytable module is use to display the records as in table format
from prettytable import PrettyTable

credential_info = {"ad@gmail.com": ["AD","Liflq#9:",'ad@gmail.com','2003-02-12',"User"]}



def encrypt(text, key):
        return ''.join([chr(ord(char) ^ key) for char in text])

def decrypt(encrypted_text, key):
       return ''.join([chr(ord(char) ^ key) for char in encrypted_text])


def create_user():
    details = []
    consitent = True
    print("Enter 0 for Exit")
    while True and consitent:
        u_name = input("Enter UserName >> ")
        if u_name == '0':
            consitent = False
        else:
            details.append(u_name)
            break
    while True and consitent:
        pas_wd = input("Enter PassWord >> ")
        pas_wd.strip()

        if pas_wd == '0':
            consitent = False
            break
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

        match = re.match(pattern, pas_wd)

        if match and u_name != pas_wd :
            details.append(pas_wd)
            break
        else:
            print("Invalid Password,Try another")
    while True and consitent:
        email = input("Enter Email >> ")
        if (email == 0):
            consitent = False
            break

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.match(pattern, email)
        if match:
            details.append(email)
            break
        else:
            print("Not Valid Email")
    while True and consitent:
        dob = input("Enter DOB YYYY-MM-DD >> ")
        if dob == '0':
            consitent = False
            break

        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        match = re.match(date_pattern, dob)
        if match:
            details.append(dob)
            break
        else:
            print("Not Valid Date")
    while True and consitent:
        U_A = input("Enter 1 for Admin (or) 2 for User >> ")
        if U_A == '0':
            consitent = False
            break
        if U_A == '1':
            details.append("Admin")
            break
        elif U_A == '2' :
            details.append("User")
            break
        else:
            continue
    if consitent :

        details[1] = encrypt(details[1],len(details[1]))

        credential_info[details[2]] = details
        return  True
    return False


def verify():
    print("Enter 0 for Exit")
    pwd_changed = False
    forgot_pwd_flag = False
    while True:

        email_2 = input("Enter Email Id >> ")
        if email_2 == '0':
            return -1
        if forgot_pwd_flag :
                while True:
                    re_passwd = input("Enter New Password >> ")
                    if re_passwd == '0':
                        pwd_changed = True
                        break
                    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
                    match = re.match(pattern, re_passwd)
                    if match:
                        credential_info[email_2][1] = encrypt(re_passwd,len(re_passwd))

                        break
                    else:
                        print("Not Valid Try Another !")
                        continue
                if pwd_changed:
                    continue
                else:
                    print("Successfully Password Changed")
                    forgot_pwd_flag = False
                    continue

        if email_2 in credential_info :
            pass_wd = input("Enter Password >>  ")
            if email_2 == '0':
                return -1


            if decrypt(credential_info[email_2][1],len(credential_info[email_2][1])) == pass_wd.strip() :
                return credential_info[email_2]
            else:
                   u_pwd_choice = input("Not Valid Credentials, Enter 1 for Reset Password (or) 0 for Retry >> ")
                   if u_pwd_choice == '1' :
                        forgot_pwd_flag = True
        else:
            continue

# flight_details = {"AIR121":{"Name":"AIRINDIA","FlightNo":"AIR121","Dest":"Delhi","Arrival":'Chennai',"Dest_date":'2001-02-01',"Dest_Time":'04:21',"Arrival_Date":"2001-02-02","Arrival_Time":'20:12',"Nof_Seats":'60',"Status":'Flying'}}
flight_details = {
    "AIR121": [ "AIR121","AIRINDIA", "Delhi", 'Chennai', '2001-02-01', '04:21', "2001-02-02", '20:12', '60', 'Flying'],
    "AIR122": [ "AIR122","AIRINDIA", "Mumbai", 'Bangalore', '2001-03-01', '05:30', "2001-03-02", '21:45','59', 'Delayed'],
    "AIR123": [ "AIR123","AIRINDIA", "Kolkata", 'Hyderabad', '2001-04-01', '06:45', "2001-04-02", '22:30','58', 'On Time']
}
booking_status = {
    'ad@gmail.com':['AIR121','2000-01-02']
}

def view_flight():
    table = PrettyTable()
    table.field_names = [ "FlightNo","FlightName","Destignation","Arrival",'Dest_Date','Dest_Time','Arrival_Date','Arrival_Time','Nof_Seats','Status']

    # Add data to the table
    for value in flight_details.values():
        table.add_row(value)
    print(table)

def admin_space() :
    while True:
        print("Type as : >>\n> VIEW\n> ADD\n> DELETE\n> BOOK HISTORY\n> EXIT")
        admin_choice = input(">> ")
        if admin_choice == "EXIT" :
            break
        if admin_choice == "VIEW" :
            
            view_flight()
        if admin_choice == "ADD":
            print("Enter Information of Flight")
            flight_add_details = []
            flight_add_details.append(input("FlightNo >> "))
            flight_add_details.append(input("FlightName >> "))
            flight_add_details.append(input("Destignation >> "))
            flight_add_details.append(input("Arrival >> "))
            flight_add_details.append(input("Dest_Date >> "))
            flight_add_details.append(input("Dest_Time >> "))
            flight_add_details.append(input("Arrival_Date >> "))
            flight_add_details.append(input("Arrival_Time >> "))
            flight_add_details.append(input("No_Of_Seats >> "))
            flight_add_details.append(input("Status >> "))
            flight_details[flight_add_details[0]]=flight_add_details
            print("Added",flight_add_details[0])
            continue
        if admin_choice == 'DELETE':

            print("Enter the FlightNo")
            fly_No = input(" >> ")
            if fly_No in flight_details :
                del flight_details[fly_No]
                print("Deleted",fly_No)
            else :
                print("Not Valid Flight No !\n")
            continue
        if admin_choice == "BOOK HISTORY":
            book_history = PrettyTable()
            book_history.field_names = ["Passanger_Details","FlightNo",'Booked_Time']

            # Add data to the table
            for value in booking_status.keys():
                print(value,booking_status[value])
                book_info=booking_status[value]
                book_history.add_row([value,book_info[0],book_info[1]])
            #     book_history.add_row(value)
            print(book_history)

def user_space(user_details):
    while True:
        print("Type as : >>\n> VIEW\n> BOOK\n> HISTORY\n> EXIT")
        user_choice = input(">> ")
        if user_choice == "EXIT" :
            break
        if user_choice == "VIEW" :
            
            view_flight()
        if user_choice == "BOOK":
            book_flight_no = input("Enter Flight No >> ")
            if book_flight_no not in flight_details:
                print("Flight Number Invalid !!")
                continue
            else:
                booking_status[user_details[2]] = [book_flight_no,datetime.date.today()]
                print("Booked Flight No : ",book_flight_no,"Done")
                continue
        if user_choice == "HISTORY" :
            # print(user_details[2])
            if user_details[2] in booking_status :
                table = PrettyTable()
                table.field_names = ["Your Detail","FlightNo","Booking Date"]
                # temp_mem_for_group_details = [
                details_his=booking_status[user_details[2]]
                table.add_row([user_details[2],details_his[0],details_his[1]])
                print(table)
                continue

            else:
                print("Not History Available")








while True:
    print('''#--------------------------------------------------
#--------------FLIGHT BOOKING SYSTEM---------------
#__________________________________________________''')
    user_choice=int(input("Hi,\nChoose :\nSign Up : 1 (or) Sign In : 2 >> "))

    if user_choice ==  1 :
        if create_user():
            print("Successfully Sign Up")
        else:
            continue
    if user_choice == 2:
             user_data = verify()

             if user_data == -1:
                continue
             elif user_data[-1] == 'User':
                print("Hi,",user_data[0],"How I Help You")
                user_space(user_data)
             elif user_data[-1] == 'Admin' :
                 print("Hi,",user_data[0],"How I Help You")
                 admin_space()






