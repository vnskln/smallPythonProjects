from tkinter import *
from tkinter import messagebox
from functools import partial

window=Tk()

behaviorScore = ["wzorowe","bardzo dobre","dobre","poprawne","nieodpowiednie","naganne"]

def gradeCheckerGUI():
    classesFourthGrade = ["Język polski","Język angielski","Muzyka","Plastyka","Historia","Przyroda","Matematyka","Informatyka","Wychowanie fizyczne"]
    window.title("Licznik średniej 0.5")
    window.geometry("200x200")
    frame=Frame(window)
    frame.grid()

    title=Label(frame,text="Wybierz klasę")
    title.grid(row=0,column=0,sticky=W,padx=55,pady=20)
    
    button1=Button(text="Klasa czwarta",width=12)
    button1.grid(row=4,column=0,sticky=W,padx=55)
    button1["command"]=buttonFourthGrade

    button1=Button(text="Klasa piąta",width=12)
    button1.grid(row=5,column=0,sticky=W,padx=55)
    button1["command"]=buttonFifthGrade

    button1=Button(text="Klasa szósta",width=12)
    button1.grid(row=6,column=0,sticky=W,padx=55)
    button1["command"]=buttonSixthGrade
    window.mainloop()

def buttonFourthGrade():
    window.destroy()
    classesFourthGrade = ["Język polski","Język angielski","Muzyka","Plastyka","Historia","Przyroda","Matematyka","Informatyka","Wychowanie fizyczne", "Zachowanie"]
    createClassGUI(classesFourthGrade)

def buttonFifthGrade():
    window.destroy()
    classesFifthGrade = ["Język polski","Język angielski","Muzyka","Plastyka","Historia", "Geografia", "Biologia", "Fizyka", "Matematyka","Informatyka", "Zajęcia techniczne", "Wychowanie fizyczne", "Zachowanie"]
    createClassGUI(classesFifthGrade)

def buttonSixthGrade():
    window.destroy()
    classesSixthGrade = ["Język polski","Język angielski","Muzyka","Plastyka","Historia", "Geografia", "Biologia", "Chemia", "Fizyka", "Matematyka","Informatyka", "Zajęcia techniczne", "Wychowanie fizyczne" , "Zachowanie"]
    createClassGUI(classesSixthGrade)

def gradeCheckerGUIComeBack():
    window.destroy()
    gradeCheckerGUI()

def createClassGUI(classes):
    window=Tk()
    window.title("Licznik średniej 0.1")
    window.geometry("300x450")
    frame=Frame(window)
    frame.grid()
    title=Label(frame,text="Podaj swoje oceny:")
    title.grid(row=0,column=0,pady=10)
    classLabels=[]
    fields=[]
    for i in range (0,len(classes)):                       
        classLabels.append(Label(text=classes[i]))
        classLabels[i].grid(row=i+1,column=0,sticky=E)
        fields.append(Entry())
        fields[i].grid(row=i+1,column=1,sticky=W)
    result=Text(width=10,height=1,wrap=WORD)
    redBarResult = Text(width=15,height=2,wrap=WORD)
    buttonFinal=Button(text="Oblicz średnią",width=12)
    buttonFinal.grid(row=len(fields)+1,column=1,sticky=W,pady=10)
    buttonFinal["command"]=partial(calculate,fields,result,redBarResult)
    result.grid(row=len(fields)+2,column=1,sticky=W)
    redBarResult.grid(row=len(fields)+3,column=1,sticky=W)
    window.mainloop()

def calculate(fields,result, redBarResult):
    mean=0
    try:
        for i in range (0, len(fields)-1):
            if(float(fields[i].get()) < 1 or float(fields[i].get()) > 6):
                raise ValueError
            mean+=float(fields[i].get())
        mean/=len(fields)-1
        result.delete(0.0,END)
        result.insert(0.0,round(mean, 2))
        redBarResult.delete(0.0, END)
        if(fields[int(len(fields)-1)].get() not in behaviorScore):
            raise ValueError
        if( mean > 4.5 and fields[int(len(fields)-1)].get() in ["bardzo dobre", "wzorowe"]):
            redBarResult.insert(0.0,"Świadectwo z wyróżnieniem")
        else:
            redBarResult.insert(0.0,"Świadectwo bez wyróżnienia")
    except:
        messagebox.showerror("BŁĄD","Oceny muszą być liczbami całkowitymi od 1 do 6,a ocena z zachowania przyjmuje tylko wartośći: naganne, nieodpowiednie, poprawne, dobre, bardzo dobre, wzorowe.")

def validate(self, value):
    try:
        if value:
            v = int(value)
            return value
    except ValueError:
        return None
    
def main():
    gradeCheckerGUI()

main()
