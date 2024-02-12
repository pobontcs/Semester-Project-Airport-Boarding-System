#Rottweiler
import os
import time

#declaring the overall variables

luggage_count=0
luggage_weight=float()
destination=''

#declaring lists
list_of_passengers=[]
data_of_passenger=[]

def save():#saving function(file handling)
        
        f=open('passengerinfo.txt','w')
        for i in list_of_passengers:
            f.write(' '.join(i))
            f.write('\n')
            
        f.close()
        
def show():#show info here
    f=open('passengerinfo.txt','r')
    s=int(input("Number of passengers: "))
    showinglist=[]
    for i in range(s):
        showinglist.append(f.readline())
    for items in showinglist:
        print(items)
    f.close()
        
def security():#security access function   
    os.system('CLS')
    print("Processing....")
    time.sleep(1.5)
    os.system('CLS')
    print("\t\t\tSecurity check")
    global n
    n=int(input('Total Passengers: '))
    
    for i in range(n):
        data_of_passenger=[]
        name_passenger=input('Name: ')
        age=input("Age: ")
        adress=input('Adress: ')
        profession=input('Profession: ')
        data_of_passenger.append(name_passenger)
        data_of_passenger.append(age)
        data_of_passenger.append(adress)
        data_of_passenger.append(profession)
        list_of_passengers.append(data_of_passenger)
     
def showsecuritylist() :#showing info of the lists 
    for i in list_of_passengers:
        for j in i:
            print(j)
        print('\n')    

def weight():#function for weight charge
    luggage_weight=float(input('Luggage Weight: '))
    if luggage_weight>30.00:
        extra=luggage_weight-30
        global charge1
        charge1=extra*10
    else:
        charge1=0
    
def admin(x):#admin function
    bag_count=int(input("Total Luggages: "))
    if bag_count>2:
        extra=bag_count-2
    luggage_count=bag_count
    charge2=extra*200
    os.system('CLS')
    print("Processing...")
    time.sleep(2)
    os.system('CLS')
    weight()#calling weight function here
    os.system('CLS')
    print("Processing...")
    time.sleep(2)
    os.system('CLS')
    print(f'Name: {name}',
          f'Destination: {x}',
          f'Luggage Count: {luggage_count}',
          f'Extra Charge: {charge1+charge2}',
          sep='\n')


def convert(x):#converting the destination name                                                                         
    new=x.lower()
    return new

def menu1():#name asking function
     global name
     name=input("\t 1. Name: ")

def menu2(given):#boarding process menu
    print('\t\t\t Boarding')
    destination=input("\t 2. Destination: ")
    des=convert(destination)
    if des!=given:
        print('\n\t\t\t Wrong Counter!!!')
        time.sleep(1.5)
        os.system('CLS')
        return menu2(given)
    else:
        time.sleep(1.0)
        os.system('CLS')
        admin(destination)
    g=input('Move next>>>> ')
    main_menu()
def main_menu():#main menu
    os.system('CLS')
    print("\n\n\t\t\tWelcome\n")
    print("1.Boarding \n")
    print("2.Security \n")
    print("3.Register(Security required) \n")
    print("4.Show info (Register Required)")
    print('\n')
    command=int(input("Enter Command: "))#calling command
    if command == 1:#calling menu 1
        os.system('CLS')
        print("Processing...")
        time.sleep(2)
        os.system('CLS')   
        menu1()
        menu2('dubai')
    elif command == 2:#calling security process
        os.system('CLS')
        print("Processing...")
        time.sleep(2)
        os.system('CLS')
        security()
        showsecuritylist()
        s=int(input("Move next(Click any button): "))
        return main_menu()
    elif command == 3:#calling save info
        x=input("Did you gave the security info?(Yes/No): " )
        n=x.lower()
        if n=='yes':
            os.system('CLS')
            print("Processing...")
            time.sleep(2)
            os.system('CLS')
            save()#using the save function
            print('Saved successfully......\n')
            time.sleep(1.5)
            return main_menu()
     
        else:# if doesnt it goes to main menu
           return main_menu()
    elif command == 4:
        os.system('CLS')
        print('Processing...')
        show()
    else:
        os.system('CLS')
        main_menu()
main_menu()



