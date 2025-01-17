import tkinter as tk
from tkinter import ttk
from database_handler import DataBaseHandler

class StudentListing(tk.Frame):
    """
    A class to display the list of students in a Treeview widget.
    """
    def __init__(self, parent):
        """
        Initializes the StudentListing frame.
        """
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        """
        Creates and configures the Treeview widget for displaying student data.
        """
        self.tree = ttk.Treeview(self, columns=('ID', 'Name', 'Email', 'Age', 'Gender'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Gender', text='Gender')

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_students()

    def load_students(self):
        """
        Loads student data from the database and populates the Treeview.
        """
        # Clear existing data in the Treeview
        self.tree.delete(*self.tree.get_children())

        # Fetch all students from the database using DataBaseHandler
        for student in DataBaseHandler.get_all_students():
            # Insert each student's data as a new row in the Treeview
            self.tree.insert('', tk.END, values=student)