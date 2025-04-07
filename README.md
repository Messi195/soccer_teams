# Soccer League App

This application is designed to display and filter soccer league data using the [OpenLigaDB](https://www.openligadb.de) API. The app allows users to fetch real-time data about teams and their performance in the 2024 UEFA Champions League season. It includes functionalities to search for teams by name or filter teams based on their number of wins.

## Features

- **Fetch Data**: Retrieve live soccer team data (team names, match statistics, wins, and losses) from the API.
- **Search by Team Name**: Search for teams by entering part of the team's name.
- **Search by Wins**: Filter teams based on a specified range of the number of wins.
- **Full-Screen Mode**: The app runs in full-screen mode for better visibility on larger screens.

## Requirements

- Python 3.x
- Tkinter (for GUI)
- Requests (for HTTP requests)

You can install the required dependencies using the following command:
```bash
pip install requests
