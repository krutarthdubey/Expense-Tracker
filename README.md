Personal Expense Tracker
A simple Python desktop application to record, manage, and track daily expenses — built with Tkinter for the GUI and SQLite for database management.

Features
- Add new expenses with name, category, amount, and date  
- View all expenses in a sortable table  
- Delete selected expense records  
- View total expense summary  
- Automatically saves data in an SQLite database  
- Simple and intuitive Tkinter interface  

Tech Stack
- Programming Language: Python  
- Database: SQLite  
- GUI Framework: Tkinter  
- Libraries Used:  
  - sqlite3 – for database connection  
  - tkinter – for GUI components  
  - datetime – for handling dates  

Installation & Setup

1. Clone the repository
   bash
   git clone https://github.com/<your-username>/Expense-Tracker.git
   cd Expense-Tracker
   

2. Run the app
   bash
   python expense_tracker.py
   

3. The application window will open.  
   You can now add, view, and delete expenses.

How It Works
- The app connects to an **SQLite database (expenses.db).  
- Each record includes:
  - id – Unique identifier  
  - name – Expense name  
  - category – Category (e.g., Food, Travel, Rent)  
  - amount – Expense amount  
  - date – Date in YYYY-MM-DD format  
- The app performs *CRUD operations* (Create, Read, Update, Delete) directly from the GUI.  

Future Enhancements
- Add category-wise expense charts using *Matplotlib*  
- Include monthly filters and analytics  
- Export data to CSV  
- User authentication for multiple profiles  

Author
Krutarth Dubey  
📍 Bhopal, India  
📧 krutarthdubey2001@gmail.com
🔗 [GitHub](https://github.com/krutarthdubey) | [LinkedIn](https://linkedin.com/in/krutarth-dubey) | [LeetCode](https://leetcode.com/u/cracky123/)
