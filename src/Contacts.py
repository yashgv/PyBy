import pickle
def Main():
    print('********************Contacts********************')
    while True:
        print('''1. Display all Contacts.
2.Search Contact.
3.Add Contact.
4.Edit Contact.
5.Delete Contact.
6.Exit.
''')
        ch=int(input("Enter your choice: "))
        print()
        if ch==1:
            Display()
        elif ch==2:
            Search()
        elif ch==3:
            Add()
        elif ch==4:
            Edit()
        elif ch==5:
            Name=input("Enter the name of the contact to be deleted:")
            Delete(Name)
        elif ch==6:
            break
        else:
            print('Entered wrong choice!')
    
def EmptyFile(): #Function to create empty file if does not exists.
    try:
        Contacts=open("Contacts","rb")
    except IOError:
        Contacts=open("Contacts","wb+")
        L={}
        pickle.dump(L,Contacts)
        Contacts.close()
def Naming():    #Function to do the naming conventions.
    Contacts=open('Contacts',"rb")    
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print('')
    C_name=input("New Contact Name: ")
    if C_name==str():
        C_name='NewContact'
    #Default Name for NewContact.
    #Also numbering the Contact with same name.
    k=1
    while True:
        if C_name in ContactList:
            if C_name[-1].isdigit():
                C_name=C_name[:-1]+str(k)
                k+=1
            else:
                C_name+=str(k)
                k+=1 
        elif C_name not in ContactList:
            break
    return C_name
def MobileNumber():   #Function for taking Mobile Number
    Contacts=open('Contacts',"rb")        
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print('')
    while True:
        try:
            Num=int(input("New Contact Number: "))
            l=len(str(Num))
            if l<10 or l>10:
                Num=0
                print('Entered wrong contact number!')
                break
            Flag=0 #Check for the same contact saved!
            for i in ContactList:
                if Num==ContactList[i]:
                    Flag=1
                    Saved=i
            if Flag==1:
                print("Number already saved as: ",Saved)
                break
        except Exception:
            print('Entered wrong contact number!')
            Num=0
            break
        break
    return Num
def Display():
    EmptyFile()
    Contacts=open("Contacts","rb+")
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print()
    while True:
        if ContactList=={}:
            print("No Contact Saved!")
            break
        print('Saved Contacts: ')
        for i in sorted(ContactList):
            print(i,':',ContactList[i])
        break
    print()
def Search():
    EmptyFile()
    Contacts=open("Contacts","rb+")
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print()
    while True:
        if ContactList=={}:
            print("No Contact Saved!")
            break
        print()
        Name=input("Enter the name of the contact to be searched:")
        print('Contacts found:')
        print()
        try:
            for i in sorted(ContactList):
                if Name.lower() in i.lower() or i.lower() in Name.lower():
                    print(i,':',ContactList[i])
            break
        except Exception:
            print('Contact not found!')
    print()
def Add():
    EmptyFile()
    Contacts=open("Contacts","rb+")
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print()
    while True:
        try:
            Name=Naming()  #input("Name: ")
            Num=MobileNumber()
            if Num==0:
                break
            ch=input("Save contact?(y/n): ")
            if ch.lower()=='y':
                ContactList[Name]=Num
                Contacts=open("Contacts","wb")
                pickle.dump(ContactList,Contacts)
                Contacts.close()
                print("Contact Saved!")
                break
            else:
                print("Contact not saved!")
                break
        except Exception:
            print('Entered wrong contact number!')
            break
    print()
def Edit():
    EmptyFile()
    Name=input("Enter the name of the contact to be edited:")
    while True:
        Contacts=open("Contacts","rb+")
        try:
            ContactList=pickle.load(Contacts)
        except Exception:
            print()
        try:
            print(Name,':',ContactList[Name])
        except Exception:
            print('Contact not found!')
            break
        print('''1.Edit(Name).
2.Edit(Number).
3.Delete Contact.
4.Exit.''')
        ch=int(input('Enter your choice: '))
        if ch==1:
            Num=ContactList[Name]
            del ContactList[Name]
            Name=Naming()
            ContactList[Name]=Num
            ch=input("Save edited contact?(y/n): ")
            if ch.lower()=='y':
                Contacts=open("Contacts","wb")
                pickle.dump(ContactList,Contacts)
                Contacts.close()
                print("Contact Saved!")
                continue
            else:
                print("Contact not edited!")
                continue
        elif ch==2:
            Num=MobileNumber()
            if Num==0:
                continue
            ContactList[Name]=Num
            ch=input("Save edited contact?(y/n): ")
            if ch.lower()=='y':
                Contacts=open("Contacts","wb")
                pickle.dump(ContactList,Contacts)
                Contacts.close()
                print("Contact Saved!")
                continue
            else:
                print("Contact not edited!")
                continue
        elif ch==3:
            Delete(Name)
            break
        elif ch==4:
            break
        else:
            print("Entered wrong choice!")
def Delete(Name):
    EmptyFile()
    Contacts=open("Contacts","rb+")
    try:
        ContactList=pickle.load(Contacts)
    except Exception:
        print()
    while True:
        try:
            print(Name,':',ContactList[Name])
            print()
            del ContactList[Name]
            ch=input('Delete Contact?(y/n): ')
            if ch.lower()=='y':
                Contacts=open("Contacts","wb")
                pickle.dump(ContactList,Contacts)
                Contacts.close()
                print("Contact Deleted!")
                break
            else:
                print("Not deleted!")
                break
        except Exception:
            print('Contact not found!')
            break
    print()
