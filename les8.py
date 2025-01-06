# import requests

# url = "https://api.openligadb.de/getbltable/ucl2024/2024"

# respont = requests.get(url)

# if respont.status_code == 200:
#     data = respont.json()
#     for team in data:
#         print(f' Team - {team["teamName"]}, matches - {team["matches"]}, lost - {team["lost"]}, won - {team["won"]}')

from tkinter import Tk, Label, Button,Listbox,END,Entry
import requests


root = Tk()
root.title("my app")
root.attributes("-fullscreen", True)


data = []

def on_click():
    url = "https://api.openligadb.de/getbltable/ucl2024/2024"
    response = requests.get(url)
    if response.status_code == 200:
        global  data
        data = response.json()
        display_data(data)
    else:
        listbox.insert(END, f"Error - {response.status_code}")

def display_data(data):
    listbox.delete(0, END)
    for team in data:
        listbox.insert(END, f'Team - {team["teamName"]}, matches - {team["matches"]}, lost - {team["lost"]}, won - {team["won"]}')   

def filter_data():
    query = entry.get().strip().lower()
    if query:
        filter_data = [team for team in data if team['teamName'].lower().startswith(query)]
        display_data(filter_data)
    else:
        display_data(data)

def filter_wins():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    filter_data = [team for team in data if team['won'] >= num1 and team['won'] <= num2]
    display_data(filter_data)

label = Label(root, text="Soccer league", font=("Comic Sans MS", 44))
label.pack()

button = Button(root, text="получить даные", font=("Arial", 16), bg="lightgreen", fg="black", command=on_click)
button.pack(pady=10) 

listbox = Listbox(root, width=60, height=18)
listbox.pack()

filter_button = Button(root, text="Search for names", command=filter_data)
filter_button.pack(pady=5)                                                                                               

entry = Entry(root, width=30)
entry.pack(pady=5)

button1 = Button(root, text="Search for wins", command=filter_wins)
button1.pack(pady=10) 

entry1 = Entry(root, width=30)
entry1.pack(pady=5)

entry2 = Entry(root, width=30)
entry2.pack(pady=5)
































root.mainloop()