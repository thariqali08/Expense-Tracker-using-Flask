# Expense Tracker

This is a simple web-based Expense Tracker application built using Flask and SQLite. The application allows users to log in and manage their expenses efficiently.

## Features

- User authentication (simple hardcoded username and password for demonstration)
- Add new expenses with date, category, description, and amount
- List all expenses
- Display total amount of expenses

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

## Getting Started

### Prerequisites

- Python 3.x installed
- Flask installed (`pip install Flask`)
- SQLite installed

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/yourusername/expense-tracker.git
2. Navigate to the project directory
   ```
   pip install Flask
   ```
3. Install the required packages
   ```sh
   pip install Flask
   ```
4. Run the Flask application
   ```sh
   python app.py
   ```

## Usage
- Home Page: Navigate to the home page to log in.
- Log In: Use the hardcoded credentials to log in (username: thariq, password: thariq08).
- Add Expense: After logging in, add new expenses by providing the date, category, description, and amount.
- List All Expenses: View all the expenses and the total amount spent.

## File Structure
- templates/: Contains the HTML templates for rendering the web pages.
- app.py: Main application file that contains the Flask routes and logic.
- expense_data.db: SQLite database file (will be created automatically).
