from tkinter import ttk, constants
import tkinter as tk
from services.house_service import house_service


class HouseView:
    def __init__(self, root, handle_login, handle_assessment, user):#user_id):
        self._root = root
        self._handle_login = handle_login
        self._handle_assessment = handle_assessment
        self._user_id = user.id
        self.user = user
        self._house_id = house_service.get_users_house_id(user.id)
        self._house = house_service.get_users_house(user.id)
        self._frame = None
        self._house_age_entry = None
        self._type_of_heating_entry = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Grid the frame within the root widget
        self._frame.grid(row=0, column=0)

        heading_label = ttk.Label(
            master=self._frame, text="Check out the consumption of your home!")

        consumption_estimate = house_service.get_energy_consumption(
            self._house.id)

        consumption_label = ttk.Label(
            master=self._frame, text="Yearly energy consumption:"+str(consumption_estimate))
        self._house_age_entry = ttk.Entry(master=self._frame)

        pollution_estimate = house_service.get_pollution(self._house.id)

        pollution_label = ttk.Label(
            master=self._frame, text="House pollution: " + str(pollution_estimate))

        user_id_label = ttk.Label(
            master=self._frame, text="User_id: " + str(self.user.id)+
                ", Username: "+str(self.user.username) )

        update_button = ttk.Button(
            master=self._frame,
            text="Update",
            command=lambda: self._update_click()
        )
        assessment_button = tk.Button(
            master=self._frame,
            text="Create/update assessment",
            command=lambda: self._handle_assessment_click(),
            bg="#808000", fg="#ffffff"
        )
        logout_button = tk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self._handle_logout_click(),
            bg="#ff8c00", fg="#ffffff"
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        consumption_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        pollution_label.grid(row=2, column=0, padx=5, pady=5)
        # update_button.grid(row=3, column=0, columnspan=2, sticky=(
        #    constants.E, constants.W), padx=5, pady=5)
        assessment_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        logout_button.grid(row=5, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        user_id_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        pollution_label.grid(row=2, column=0, padx=5, pady=5)

        # Adjust column configuration for root widget
        self._root.grid_columnconfigure(0, weight=1)

    def _handle_logout_click(self):
        self._handle_login()

    def _handle_assessment_click(self):
        self._handle_assessment(self.user)

    def _update_click(self):
        house_age = self._house_age_entry.get()
        type_of_heating_entry = self._type_of_heating_entry.get()
        print(f"house age:{house_age}")
