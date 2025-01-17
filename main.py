import tkinter as tk
from registration_form import RegistrationForm
from student_listing import StudentListing  # Corrected import name


class MainApplication(tk.Tk):
    """
    Main application window for the Student Management System.
    """
    def __init__(self):
        """
        Initializes the main application window.
        """
        super().__init__()
        self.title("Students Management System")
        self.geometry("1600x900")
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and arranges the main widgets of the application.
        """
        # Title label
        title_label = tk.Label(self, text="Students Management System", font=('Helvetica', 16))
        title_label.pack(side='top', fill='x')

        # Registration form (left side)
        self.registration_form = RegistrationForm(self, self.refresh_listing)
        self.registration_form.pack(side='left', fill='y', padx=10, pady=10)

        # Student listing (right side)
        self.student_listing = StudentListing(self)
        self.student_listing.pack(side='right', fill='both', expand=True, padx=10, pady=10)

    def refresh_listing(self):
        """
        Refreshes the student listing by calling the load_students method of the StudentListing instance.
        """
        self.student_listing.load_students()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()