import pickle
import os
def Main():
    print('********************Notepad********************')
    while True:
        print('''Notepad:
    1.Create New Note.
    2.Open Note(Read Only).
    3.Edit Note.
    4.Delete Note.
    5.Exit.
    ''')
        ch=int(input("Enter your choice: "))
        if ch==1:
            CreateNew()
            print()
        elif ch==2:
            Open()
            print()
        elif ch==3:
            EOpen()
            print()
        elif ch==4:
            Delete()
            print()
        elif ch==5:
            break
        else:
            print("Entered wrong choice!")
def NamesFile(): #Function to create file of names of notes if does not exists
    try:
        Snotes=open("Notes","rb")
    except IOError:
        Snotes=open("Notes","wb+")
        L=[]
        pickle.dump(L,Snotes)
        Snotes.close()
def Naming():    #Function to do the naming conventions.
    Snotes=open('Notes',"rb") #File to take the names of the Notes.        
    N_name=input("Enter the Name of the Note.: ")
    if N_name==str():
        N_name='NewNote'  #Default Name for New Note.
    try:
        names=pickle.load(Snotes)
    except Exception:
        print('')
    #Also numbering the Note with same name.
    k=1
    while True:
        if N_name in names:
            if N_name[-1].isdigit():
                N_name=N_name[:-1]+str(k)
                k+=1
            else:
                N_name+=str(k)
                k+=1 
        elif N_name not in names:
            break
    names.append(N_name)
    print(names)
    return names
def CreateNew():
    NamesFile()  #Function to create file of names of notes if does not exists.
    Names=Naming() #Function to do the naming conventions.
    #Opening NoteFile. 
    print()
    print()
    l=len(Names)-1
    Note=''
    print('''Press: 1.Save.
Press: 2.Don't Save.
''')
    Flag=0
    print("\t"*5+Names[l]+"\n==>>")
    #Taking Multiline Input.
    while True:
        TEXT=input()
        if TEXT=='1':
            Flag=1
            break
        elif TEXT=='2':
            break
        Note+=TEXT+'\n'
    if Flag==1: #Writing and saving the note in the file.
        Snotes=open("Notes","wb+")
        pickle.dump(Names,Snotes)
        Snotes.close()
        f=open(Names[l],'w')
        f.write(Note)
        f.close()
        print("Note Saved!")       
def Open():#READ ONLY
    #Text file with saved notes.
    NamesFile()
    Snotes=open('Notes',"rb")
    try:
        Notes=pickle.load(Snotes)
    except Exception:
        print()
    while True:
        if Notes==[]:
            print("No Notes saved!")
            break
        else:
            print("Saved Notes: ",Notes)
        N_name=input("Enter the name of the note to be opened: ")
        if N_name in Notes:
            fobj=open(N_name,"r+")
            note=fobj.read()
            print("\t"*5+N_name+"\n==>>")
            print(note)
            fobj.close()
        elif N_name not in Notes:
            print("Note not found!")
        break
    print()
def EOpen():#Editing Mode
    NamesFile()
    Snotes=open('Notes',"rb")
    try:
        Notes=pickle.load(Snotes)
    except Exception:
        print()
    while True:
        if Notes==[]:
            print("No Notes saved!")
            break
        else:
            print("Saved Notes: ",Notes)
        N_name=input("Enter the name of the note to be opened: ")
        while True:
            if N_name in Notes:
                print()
            elif N_name not in Notes:
                print("Note not found!")
                break
            print('''Modes: 1.Write Mode.
       2.Edit Line Mode.
       3.Clear All
       4.Exit.''')
            ch=int(input("Enter the mode: "))
            if ch==1:
                Write(N_name)
            elif ch==2:
                EditLine(N_name)
            elif ch==3:
                fobj=open(N_name,'w+')
                fobj.close()
                print('Cleared all successfully')
            elif ch==4:
                break
            else:
                print("Entered wrong choice!")
        break
def Write(N_name):
    print('''Press: 1.Save Changes.
Press: 2.Don't Save.
''')
    fobj=open(N_name,"r+")
    print("\t"*5+N_name+"\n==>>")
    print(fobj.read())
    print("==>>")
    Note=''
    #Taking Multiline Input.
    Flag=0
    while True:
        TEXT=input()
        if TEXT=='1':
            Flag=1
            break
        elif TEXT=='2':
            break
        Note+=TEXT+'\n'
    if Flag==1: #Writing and saving the note in the file.
        fobj.write(Note)
        fobj.close()
        print("Changes Saved!")   
def EditLine(N_name):
    f=open(N_name,"r+")
    print("\t"*5+N_name+"\n==>>")
    lines=f.readlines()
    LineNum=1
    for line in lines:
        print(LineNum,line)
        LineNum+=1
    LineNum=int(input("Enter the Line Number to be edited: "))
    print('1.Edit    2.Delete')
    while True:
        ch=int(input("Enter your choice: "))
        if ch==1:
            lines[LineNum-1]=input("Write New Line: ")
            print()
            ch=input("Save changes?(y/n): ")
            if ch.lower()=='y':
                fobj=open(N_name,'w+')
                fobj.writelines(lines)
                print("Changes Saved!")
                fobj.close()
            break
        elif ch==2:
            try:
                lines.pop(LineNum-1)
            except Exception:
                print('Entered wrong line number!')
                break
            ch=input("Save changes?(y/n): ")
            if ch.lower()=='y':
                fobj=open(N_name,'w+')
                fobj.writelines(lines)
                print("Changes Saved!")
                fobj.close()
            break
        else:
            print('Entered wrong choice')
def Delete():
    NamesFile()
    Snotes=open('Notes',"rb")
    try:
        Notes=pickle.load(Snotes)
    except Exception:
        print()
    while True:
        if Notes==[]:
            print("No Notes saved!")
            break
        else:
            print("Saved Notes: ",Notes)
        N_name=input("Enter the name of the note to be Deleted: ")
        ch=input('Do you want to delete Note?(y/n): ')
        Notes.remove(N_name)
        if ch.lower()=='y':
            try:
                os.remove(N_name)
                Snotes=open('Notes',"wb")
                pickle.dump(Notes,Snotes)
                Snotes.close()
            except Exception:
                print('Note not found!')
                break
            print('Note deleted successfully!')
            break
