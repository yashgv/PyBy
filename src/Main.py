print('--------------------Program PyBy--------------------')
import Notepad
import Contacts
import Calendar
import Calculator
while True:
    print('''Menu:
    1.Notepad
    2.Contacts
    3.Calendar
    4.Calculator
    5.Exit''')
    ch=int(input('Enter your choice: '))
    if ch==1:
        Notepad.Main()
    elif ch==2:
        Contacts.Main()
    elif ch==3:
        Calendar.Main()
    elif ch==4:
        Calculator.Main()
    elif ch==5:
        break
    else:
        print('Entered wrong choice!')
