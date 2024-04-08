from tkinter import ttk, constants
from repositories.user_repository import user_repository

class AssessmentView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._house_age_entry = None
        self._type_of_heating_entry = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid(row=0, column=0)  # Grid the frame within the root widget

        heading_label = ttk.Label(master=self._frame, text="Fill out a basic assessment about your home!")

        house_age_label = ttk.Label(master=self._frame, text="House age")
        self._house_age_entry = ttk.Entry(master=self._frame)

        type_of_heating_label   = ttk.Label(master=self._frame, text="Type of heating 1-9")
        self._type_of_heating_entry  = ttk.Entry(master=self._frame)

        update_button = ttk.Button(
          master=self._frame, 
          text="Update",
          command=lambda: self._update_click()
        )
        logout_button = ttk.Button(
          master=self._frame, 
          text="Logout",
          command=lambda: self._handle_logout_click()
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        house_age_label.grid(row=1, column=0, padx=5, pady=5)
        self._house_age_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        type_of_heating_label.grid(row=2, column=0, padx=5, pady=5)
        self._type_of_heating_entry  .grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        update_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(0, weight=1)  # Adjust column configuration for root widget

    def _handle_logout_click(self):
        self._handle_login()

    def _update_click(self):
        house_age = self._house_age_entry.get()
        type_of_heating_entry = self._type_of_heating_entry.get()
        print(f"house age:{house_age}")
