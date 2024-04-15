from tkinter import ttk, constants
# from repositories.user_repository import user_repository
from services.house_service import house_service


class LoginView:
    def __init__(self, root, handle_assessment, handle_registration):
        self._root = root
        self._handle_registration = handle_registration
        self._handle_assessment = handle_assessment
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        # self_

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Grid the frame within the root widget
        self._frame.grid(row=0, column=0)

        heading_label = ttk.Label(master=self._frame, text="Log in")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=lambda: self._handle_login_click()
        )
        registration_button = ttk.Button(
            master=self._frame,
            text="Registration",
            command=lambda: self._handle_registration_click()
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        registration_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Adjust column configuration for root widget
        self._root.grid_columnconfigure(0, weight=1)

    def _handle_login_click(self):
        username_entry = self._username_entry.get()
        password_entry = self._password_entry.get()
        print(f"Attempt at logging in: {username_entry}")
        user_id = house_service.login(username_entry, password_entry)
        if user_id:
            self._handle_assessment(user_id)

    def _handle_registration_click(self):
        print("handling registration click by login view")
        self._handle_registration()


'''
def start(self):
    heading_label = ttk.Label(master=self._root, text="Login")

    username_label = ttk.Label(master=self._root, text="Username")
    username_entry = ttk.Entry(master=self._root)

    password_label = ttk.Label(master=self._root, text="Password")
    password_entry = ttk.Entry(master=self._root)

    button = ttk.Button(master=self._root, text="Button")

    # vasempaan laitaan
    heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

    username_label.grid(row=1, column=0)
    # vasempaan ja oikeaan laitaan
    username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

    password_label.grid(row=2, column=0)
    # vasempaan ja oikeaan laitaan
    password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W))

    # vasempaan ja oikeaan laitaan
    button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

    self._root.grid_columnconfigure(1, weight=1)
'''
