def add(x,y):
    add=x+y
    return add
def sub(x,y):
    diff=x-y
    return diff
def mult(x,y):
    prod=x*y
    return prod
def div(x,y):
    quot=x/y
    return quot
def per(x,y):
    per=(x*100)/y
    return per

print('Note:- Input your number then operator(+,-,*,/,%[Percentage]) then input your next number')
def Operators(num1,num2,oper):
    if oper=='+':
        out=add(num1,num2)
    elif oper=='-':
        out=sub(num1,num2)
    elif oper=='*':
        out=mult(num1,num2)
    elif oper=='/':
        out=div(num1,num2)
    elif oper=='%':
        out=per(num1,num2)
    else:
        print('Entered inappropriate operator!')
    return out
def Calculator():
    try:
        num1=int(input('Enter first number: '))
        oper=input('Enter the operator: ')
        num2=int(input('Enter second number: '))
    except Exception:
        print('Entered wrong figure!')
    Total=Operators(num1,num2,oper)
    while True:
        oper=input('Enter operator: ')
        if oper=='=':
            print("~~~~~~~~~~~~~~")
            print("Result is :",Total)
            print("~~~~~~~~~~~~~~")
            break
        num2=int(input('Enter number: '))
        Total=Operators(Total,num2,oper)
def Main():
    while True:
        try:
            print('''1.Calculate.
2.Exit.''')
            ch=int(input('Enter your choice: '))
            if ch==1:
                Calculator()
            elif ch==2:
                break
            else:
                print('Entered wrong choice!')
        except Exception:
            print('Something went wrong,try again!')
