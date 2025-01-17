# School Registration System

This project is a desktop application built with Tkinter for managing student registrations in a school. It allows users to add new student records, view a list of registered students, and visualize the gender distribution of the student body using a pie chart. The application uses an SQLite database (`students.db`) that is automatically created upon the first run.

## Screenshot

![Application Screenshot](screenshot.png)  

## How to Run the Application

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/0xDag0n/school_registration_system.git](https://github.com/0xDag0n/school_registration_system.git)
    cd school_registration_system
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv  # Use python3 explicitly for clarity
    ```

3.  **Activate the virtual environment:**

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**

    ```bash
    python main.py
    ```

## Dependencies

-   Python 3.8 or higher
-   The following packages (listed in `requirements.txt`):