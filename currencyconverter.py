############################################################## importation 
from tkinter import *
from tkinter import ttk
################################################## création d'une fenêtre
root = Tk()
root.title('Convertisseur')
root.geometry("600x400")
############################### ajouts de certains éléments
frame1 = Frame(root, padx = 60, pady = 30)
frame1.pack()
label = Label(frame1, text = "Convertisseur", font = 'TimesNewRoman 24', fg = 'red', bd = 2)
label.pack(side = TOP)
frame2 = Frame(frame1, pady = 15)
frame2.pack()
frame3 = Frame(frame2, pady = 10)
frame3.pack()
frame4 = Frame(frame2, pady = 10)
frame4.pack()
#Label(frame3, text = "Dollars", font = 'TimesNewRoman 16').pack(side = LEFT)
############################### Première liste déroulante
deviseOne = Entry(frame3, font = 'TimesNewRoman 16', fg = 'black', bg = '#ddd', bd = 2, relief = RIDGE)
deviseOne.pack(side = RIGHT)
#Label(frame4, text = "Euros ", font = 'TimesNewRoman 16').pack(side = LEFT)
################################# 2 eme liste déroulante
deviseTwo = Entry(frame4, font = 'TimesNewRoman 16', fg = 'black', bg = '#ddd', bd = 2, relief = RIDGE)
deviseTwo.pack(side = RIGHT)
frame5 = Frame(frame1)
frame5.pack()
devise = ttk.Combobox(frame3, values=["Dollar", "Yen", "Euro", "Livre"], font = 'TimesNewRoman 16')
devise.pack(side = RIGHT)
devise.current(0)
devise2 = ttk.Combobox(frame4, values=["Dollar", "Yen", "Euro", "Livre"], font = 'TimesNewRoman 16')
devise2.pack(side = RIGHT)
devise2.current(0)
######################## convertion des devises
def convertir(t1,t2):
    global devise
    global devise2
    global deviseOne
    global deviseTwo
    historique = ""
    nombre1 = deviseOne.get()
    nombre2 = deviseTwo.get()
    if len(str(nombre2)) > 0 and len(str(nombre1)) > 0:
        deviseOne.delete(0,'end')
        deviseTwo.delete(0,'end')
    elif len(str(nombre1)) != 0:
        deviseTwo.insert(0,str(int(nombre1) * t1))
        historique = str(nombre1) + " " + devise.get() + " = " + deviseTwo.get() + " " + devise2.get() + "\n"
        f = open("Historique.csv","a")
        f.write(historique)
        f.close()
    elif len(str(nombre2)) != 0:
        deviseOne.insert(0,str(int(nombre2) * t2))
        historique = str(nombre2) + " " + devise2.get() + " = " + deviseOne.get() + " " + devise.get() + "\n"
        f = open("Historique.csv","a")
        f.write(historique)
        f.close()
def appel_convertir():
    global deviseOne 
    global deviseTwo
    global devise
    select1 = devise.get()
    select2 = devise2.get()
############################## conversion des devises (conditions)
    for i in ["Dollar", "Yen", "Euro", "Livre"]:
        if select1 == i and select2 == i:
            convertir(1,1)       
    for i in ["Yen", "Euro", "Livre"]:
        if select1 == "Dollar" and select2 == i:
            if i == "Yen":
                convertir(130.27,0.0077)
            elif i == "Euro":
                convertir(0.92,1.09)
            elif i == "Livre":
                convertir(0.81,1.23)
    for i in ["Dollar", "Euro", "Livre"]:
        if select1 == "Yen" and select2 == i:
            if i == "Dollar":
                convertir(130.27,0.0077)
            elif i == "Euro":
                convertir(0.0071,141.74)
            elif i == "Livre":
                convertir(0.0062,160.42)
    for i in ["Dollar", "Yen", "Livre"]:
        if select1 == "Euro" and select2 == i:
            if i == "Dollar":
                convertir(1.09,0.92)
            elif i == "Yen":
                convertir(141.74,0.0071)
            elif i == "Livre":
                convertir(0.88,1.13)
    for i in ["Dollar", "Euro", "Yen"]:
        if select1 == "Livre" and select2 == i:
            if i == "Dollar":
                convertir(1.23,0.81)
            elif i == "Yen":
                convertir(160.42,0.0062)
            elif i == "Euro":
                convertir(1.13,0.88)
####################### on crée un bouton pour reset nos entrées
def reset():
    global deviseOne
    global deviseTwo
    deviseOne.delete(0,'end')
    deviseTwo.delete(0,'end')
####################################### Ajout des boutons et leur actions celui de convertir et de supprimer
Button(frame5, text = "Convertir", font = 'TimesNewRoman 15', padx = 5, command = appel_convertir).pack(side = LEFT)
Button(frame5, text = "Reset", font = 'TimesNewRoman 15', padx = 5, command = reset).pack(side = RIGHT)
root.mainloop()

























