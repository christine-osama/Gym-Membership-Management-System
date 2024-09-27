import os
import time

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

class Member:
    def __init__(self, first_name, last_name, membership_id, membership_status='inactive'):
        self.first_name=first_name
        self.last_name=last_name
        self.membership_id=membership_id
        self.membership_status=membership_status

    def display_member(self):
        print(f"First name: {self.first_name}")   
        print(f"Last name: {self.last_name}")  
        print(f"Membership ID: {self.membership_id}")  
        print(f"Membership status: {self.membership_status}")
        print('_'*20)

def create_member():
    clear_screen()
    first_name=input("Enter first name: ")
    last_name=input("Enter last name: ")   
    membership_id=input("Enter membership ID: ")     
    membership_status=input("Enter Membership status ,or click enter: ")
    if not membership_status:
        membership_status='inactive'
    return Member(first_name, last_name, membership_id, membership_status)

#بداية البحث

def search_member(members):
    clear_screen()
    print("\n search by: \n")
    print("1.Membership ID")
    print("2.First name")
    print("3.Membership status\n")

    search_choice=input("Enter your choice")

    found_members=[]
    
    if search_choice=='1':
        search_id=input("Enter the membership ID to search: ")
        for x in members:
            if x.membership_id == search_id:
                found_members.append(x)
                break
    elif search_choice=='2':
        first_name=input("Enter the first name to search : ")
        for x in members:
            if x.first_name.lower()==first_name.lower():
                found_members.append(x)
    elif search_choice=='3':
        membership_status=input("Enter Membership status to search: ")
        for x in members:
            if x.membership_status.lower()==membership_status.lower():
                found_members.append(x)
    else:
        print("invalid choice")

    if found_members: 
        clear_screen()
        print("Members found: ")
        for x in found_members:
            x.display_member()
    else:
        print("Member not found!")
    time.sleep(2)
#نهاية البحث
members=[]
while True:
    clear_screen()
    print("\nWelcome to Gym membership management \n")
    print("\nChoose an action: \n")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        members.append(create_member())
        print("Member added successfully!")
        time.sleep(2)
    elif choice =='2':
        clear_screen()
        if members:
            print("Displayong all members ........")

            for i in members:
                i.display_member()
                time.sleep(5)
        else:
            print("No members to display!")
            time.sleep(2)        
    elif choice=='3':
        if members:
            search_member(members)
        else:
            print("No members to search!")
            time.sleep(2)    
    elif choice=='4':
        print("Exiting......")
        break
    else:
        print("invalid choice! please try again.")       
        time.sleep(2)   












    
