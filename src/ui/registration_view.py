from tkinter import ttk, constants, messagebox
import tkinter as tk
from services.house_service import house_service


class RegistrationView:
    """Class representing the view for user registration.

    Args:
        root (tk.Tk): The root Tkinter window.
        handle_login (function): Callback function for entering login view.
        handle_assessment (function): Callback function for entering assessment view.
    """

    def __init__(self, root, handle_login, handle_assessment):
        self._root = root
        self._handle_login = handle_login
        self._handle_assessment = handle_assessment
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def destroy(self):
        """Destroys the RegistrationView frame."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._frame.grid(row=0, column=0)

        heading_label = ttk.Label(
            master=self._frame, text="Register as a new user")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        register_button = tk.Button(
            master=self._frame,
            text="Register",
            command=lambda: self._handle_registration_click()
        )

        logging_in_button = tk.Button(
            master=self._frame,
            text="Logging in",
            command=lambda: self._handle_login()
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        logging_in_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(0, weight=1)

    def _handle_registration_click(self):
        username_entry = self._username_entry.get()
        password_entry = self._password_entry.get()
        print(f"Attempt at registering for: {username_entry}")
        user = house_service.register(username_entry, password_entry)
        if user:
            self._handle_assessment(user)
        else:
            messagebox.showerror(title="Registration failed",
                                 message="Username taken")
