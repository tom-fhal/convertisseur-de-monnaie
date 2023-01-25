from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
import tkinter as tk
import json
import requests
from tkinter import END



API_KEY = '2b544534ca760a3ab2db0bd9'

 #l'url de la requête standard
url = f'https://v6.exchangerate-api.com/v6/2b544534ca760a3ab2db0bd9/latest/USD'


# Faire la demande standard à l'API
response = requests.get(f'{url}').json()

currencies = dict(response['conversion_rates'])


root = tk.Tk()
root.title('TomFHAL.com - Convertisseur Monnaies')
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#créer deux cadres
currency_frame = Frame (my_notebook, width=480, height=480)
conversion_frame = Frame (my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

#Ajouter nos onglets
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# 2e onglet désactivé
my_notebook.tab(1, state='disabled')

def lock():
    if not home_entry.get() and not conversion_entry.get() and not rate_entry.get(): 
        messagebox.showwarning('ATTENTION !, tous les champs sont obligatoire')
    else:
        #Désactiver les boîtes de saisie
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        #Activer l'onglet
        my_notebook.tab(1, state='normal')
        #Changer les champs de l'onglet
        amount_entry.config(text=f'Montant du {home_entry.get()} à convertir en {conversion_entry.get()}')
        converted_label.config(text=f'Est égal à ce nombre {conversion_entry.get()}')
        convert_button.config(text=f'Convertir de  {home_entry.get()}')
lock()
        
def unlock():
    #Activer les boîtes de saisie
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    #Désactiver l'onglet
    my_notebook.tab(1, state='disabled')
    
unlock()

home = LabelFrame(currency_frame, text="Votre devise nationale")
home.pack(pady=20)
#Boîte de saisie de la monnaie nationale
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=20, padx=10)


#Cadre de conversion monétaire
conversion = LabelFrame(currency_frame, text="Conversion")
conversion.pack(pady=20)

#convertir en étiquette
conversion_label = Label(conversion, text="Devise à convertir en....")
conversion_label.pack(pady=10)

#convertir en entrée 
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=20, padx=10)

#étiquette de taux
rate_label = Label(conversion, text="Taux de conversion actuel....")
rate_label.pack(pady=10)

#convertir en entrée 
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=20, padx=10)

#Cadre du bouton
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

#Creation des  Bouttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)



#####################################
#########CONVERSION STUFF############
#####################################
def convert():
    # Boîte d'entrée convertie transparente
    converted_entry.delete(0, tk.END)

    source = home_entry.get()
    destination = conversion_entry.get()
    amount = float(amount_entry.get())
    rate = float(rate_entry.get())
    conversion = amount * rate
    converted_entry.insert(0, conversion)
    url = f'https://v6.exchangerate-api.com/v6/2b544534ca760a3ab2db0bd9/convert/{source}/{destination}/{amount}'
    response = requests.get(url).json()
    result = amount * response['rate']
    converted_entry.insert(0, result)
    history.append((amount, source, destination, conversion))
    history_listbox.insert(END, f'{amount} {source} = {conversion} {destination}')
convert()


def clear():
    amount_entry.delete(0,END)
    converted_entry.delete(0,END)
clear()

amount_label = LabelFrame(conversion_frame, text="Montant à convertir")
amount_label.pack(pady=20)

#Case d'entrée pour le montant
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

#bouton de conversion
convert_button = Button(amount_label, text="Convertir", command=convert)
convert_button.pack(pady=20)

#égale au cadre
converted_label = LabelFrame(conversion_frame, text="Devise convertie")
converted_label.pack(pady=20)

#Entrée convertie
converted_entry = Entry(converted_label, font=("Helvetica", 24,), bd=0, bg="#ff0000")
converted_entry.pack(pady=10, padx=10)

#Bouton d'effacement
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

#créer l'historique Listbox
history_listbox = Listbox(conversion_frame, font=("Helvetica", 14))
history_listbox.pack(pady=20, padx=10)

#fausse étiquette pour l'espacement
spacer = Label(conversion_frame,text="",width=68)
spacer.pack()

history = []

root.mainloop()

























