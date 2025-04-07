from tkinter import Tk, Label, Button, Listbox, END, Entry
import requests
from typing import List, Dict

# Initialize main application window
root = Tk()
root.title("Soccer League App")
root.attributes("-fullscreen", True)

# Data to hold the response from the API
data: List[Dict] = []

def on_click() -> None:
    """
    Fetches the data from the API and displays it in the listbox.
    If an error occurs, it displays an error message.
    """
    url = "https://api.openligadb.de/getbltable/ucl2024/2024"
    response = requests.get(url)
    if response.status_code == 200:
        global data
        data = response.json()
        display_data(data)
    else:
        listbox.insert(END, f"Error - {response.status_code}")

def display_data(data: List[Dict]) -> None:
    """
    Displays the provided data (list of teams) in the listbox.
    
    Args:
        data (List[Dict]): List of team data dictionaries.
    """
    listbox.delete(0, END)
    for team in data:
        listbox.insert(END, f'Team - {team["teamName"]}, Matches - {team["matches"]}, '
                            f'Lost - {team["lost"]}, Won - {team["won"]}')   

def filter_data() -> None:
    """
    Filters the data based on the user's search query (team name).
    Displays matching teams in the listbox.
    """
    query = entry.get().strip().lower()
    if query:
        filtered_data = [team for team in data if team['teamName'].lower().startswith(query)]
        display_data(filtered_data)
    else:
        display_data(data)

def filter_wins() -> None:
    """
    Filters the data based on the number of wins within a specified range.
    Displays matching teams in the listbox.
    """
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        filtered_data = [team for team in data if num1 <= team['won'] <= num2]
        display_data(filtered_data)
    except ValueError:
        listbox.insert(END, "Please enter valid numbers for the win range.")

# UI setup
label = Label(root, text="Soccer League", font=("Comic Sans MS", 44))
label.pack()

button = Button(root, text="Fetch Data", font=("Arial", 16), bg="lightgreen", fg="black", command=on_click)
button.pack(pady=10) 

listbox = Listbox(root, width=60, height=18)
listbox.pack()

filter_button = Button(root, text="Search for Team Names", command=filter_data)
filter_button.pack(pady=5)                                                                                               

entry = Entry(root, width=30)
entry.pack(pady=5)

button1 = Button(root, text="Search by Wins", command=filter_wins)
button1.pack(pady=10) 

entry1 = Entry(root, width=30)
entry1.pack(pady=5)

entry2 = Entry(root, width=30)
entry2.pack(pady=5)

root.mainloop()
