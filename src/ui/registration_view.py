from tkinter import ttk, constants
from repositories.user_repository import user_repository

class RegistrationView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        #self_

        self._initialize()
    
    def destroy(self):
        self._frame.destroy()
    

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid(row=0, column=0)  # Grid the frame within the root widget

        heading_label = ttk.Label(master=self._frame, text="Register as a new user")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(
          master=self._frame, 
          text="Register",
          command=lambda: self._handle_registration_click()
        )

        logging_in_button = ttk.Button(
            master=self._frame,
            text="Logging in",
            command=lambda: self._handle_login()
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        logging_in_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(0, weight=1)  # Adjust column configuration for root widget

    def _handle_registration_click(self):
        username_entry=self._username_entry.get()
        password_entry=self._password_entry.get()
        print(f"Attempt at registering for: {username_entry}")
        val = user_repository.register(username_entry, password_entry)
        print(val)
        self._handle_login()
