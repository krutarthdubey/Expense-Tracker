import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ---------------------- DATABASE SETUP ----------------------
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')
conn.commit()

# ---------------------- FUNCTIONS ----------------------
def add_expense():
    name = name_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    if not (name and category and amount and date):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    cursor.execute("INSERT INTO expenses (name, category, amount, date) VALUES (?, ?, ?, ?)",
                   (name, category, amount, date))
    conn.commit()
    clear_fields()
    view_expenses()

def view_expenses():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

def delete_expense():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a record to delete.")
        return

    item = tree.item(selected)
    record_id = item['values'][0]
    cursor.execute("DELETE FROM expenses WHERE id=?", (record_id,))
    conn.commit()
    view_expenses()

def clear_fields():
    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def show_summary():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    total = total if total else 0
    messagebox.showinfo("Expense Summary", f"Total Expenses: ₹{total:.2f}")

# ---------------------- GUI SETUP ----------------------
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("700x500")
root.configure(bg="#f4f4f4")

# Title
title_label = tk.Label(root, text="Personal Expense Tracker", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name", bg="#f4f4f4").grid(row=0, column=0, padx=5, pady=5)
tk.Label(input_frame, text="Category", bg="#f4f4f4").grid(row=0, column=1, padx=5, pady=5)
tk.Label(input_frame, text="Amount", bg="#f4f4f4").grid(row=0, column=2, padx=5, pady=5)
tk.Label(input_frame, text="Date (YYYY-MM-DD)", bg="#f4f4f4").grid(row=0, column=3, padx=5, pady=5)

name_entry = tk.Entry(input_frame)
category_entry = tk.Entry(input_frame)
amount_entry = tk.Entry(input_frame)
date_entry = tk.Entry(input_frame)
date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

name_entry.grid(row=1, column=0, padx=5, pady=5)
category_entry.grid(row=1, column=1, padx=5, pady=5)
amount_entry.grid(row=1, column=2, padx=5, pady=5)
date_entry.grid(row=1, column=3, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="View All", command=view_expenses, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete", command=delete_expense, bg="#f44336", fg="white").grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Summary", command=show_summary, bg="#FF9800", fg="white").grid(row=0, column=3, padx=10)

# Table
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("ID", "Name", "Category", "Amount", "Date")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack()

view_expenses()

root.mainloop()