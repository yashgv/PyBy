import calendar
def Main():
    print('********************Calendar********************')
    while True:
        print('''1.Year Calendar.
2.Month Calendar.
3.Exit.''')
        ch=int(input('Enter your choice: '))
        if ch==1:
            try:
                Year=int(input('Enter the calendar year: '))
                print(calendar.calendar(Year))
            except Exception:
                print('Entered wrong Year!')
        elif ch==2:
            try:
                Year=int(input('Enter the calendar year: '))
                Month=int(input('Enter the month number: '))
                print(calendar.month(Year,Month))
            except Exception:
                print('Entered wrong Year/Month!')
        elif ch==3:
            break
        else:
            print('Entered wrong choice!')
