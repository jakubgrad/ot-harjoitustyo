from tkinter import ttk, constants
# from repositories.user_repository import user_repository
from services.house_service import house_service


class LoginView:
    def __init__(self, root, handle_assessment,handle_house, handle_registration):
        self._root = root
        self._handle_registration = handle_registration
        self._handle_assessment = handle_assessment
        self._handle_house = handle_house
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
        user = house_service.login(username_entry, password_entry)
        print("handle login inside login view retrieved")
        print(f"user with params: id:{user.id},username:{user.username}")
        if user:
            if house_service.get_users_house(user.id):
                #user has a house already
                self._handle_house(user)
            else:
                self._handle_assessment(user)

    def _handle_registration_click(self):
        print("handling registration click by login view")
        self._handle_registration()

