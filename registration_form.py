import tkinter as tk
from tkinter import ttk
from database_handler import DataBaseHandler
from student_listing import StudentListing
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import messagebox


class RegistrationForm(tk.Frame):
    """
    A class representing the registration form for new students.

    This form allows users to input student details including name, email, age, and gender,
    and submit the data to be stored in the database. It also includes a feature to visualize
    the gender distribution of registered students using a pie chart.
    """
    def __init__(self, parent, refresh_callback):
        """
        Initializes the RegistrationForm.
        """
        super().__init__(parent, padx=10, pady=10)
        self.refresh_callback = refresh_callback

        tk.Label(self, text='Full Name').pack(fill='x')
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(fill='x')

        tk.Label(self, text='Email').pack(fill='x')
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(fill='x')

        tk.Label(self, text='Age').pack(fill='x')
        self.age_spinbox = ttk.Spinbox(self, from_=10, to=100)
        self.age_spinbox.pack(fill='x')

        tk.Label(self, text='Gender').pack(fill='x')
        self.gender_var = tk.StringVar()
        tk.Radiobutton(self, text='Male', value='Male', variable=self.gender_var).pack(anchor='w')
        tk.Radiobutton(self, text='Female',value='Female', variable=self.gender_var).pack(anchor='w')

        self.submit_button = tk.Button(self, text='Submit', command=self.submit_form)
        self.submit_button.pack(fill='x')

        self.visualize_button = tk.Button(self, text='Visualize Gender Distribution', command=self.visualize_gender_distribution)
        self.visualize_button.pack(fill='x')

    def submit_form(self):
        """
        Handles the submission of the registration form.
        """
        name = self.name_entry.get()
        email = self.email_entry.get()
        try :
            age = self.age_spinbox.get()
            age = int(age)
            gender = self.gender_var.get()

            if name and email and age and gender:
                DataBaseHandler.insert_student(name, email, age, gender)
                self.refresh_callback()

                # Reset Form
                self.resset_form()
        except :
            messagebox.showinfo("Error", "please enter a number in age.")

        

    def resset_form(self):
        """
        Resets the form fields to their default values.
        """
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.age_spinbox.set(10)
        self.gender_var.set(None)

    def visualize_gender_distribution(self):
        """
        Visualizes the gender distribution of registered students using a pie chart.
        """
        try:
            students = DataBaseHandler.get_all_students()
            if not students:
                messagebox.showinfo("No Students", "No students registered yet.")
                return

            genders = [student[4] for student in students]  # Extract genders
            male_count = genders.count('Male')
            female_count = genders.count('Female')

            # Create pie chart
            fig, ax = plt.subplots()
            labels = ['Male', 'Female']  # Explicit labels for the legend
            sizes = [male_count, female_count]
            colors = ['blue', 'pink']  # Assign colors to genders
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)  # Show percentages
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Gender Distribution')  # Add a title

            # Display the chart
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


              
    