from tkinter import Tk
from ui.registration_view import RegistrationView
from ui.assessment_view import AssessmentView
from ui.administration_view import AdministrationView
from ui.login_view import LoginView
from ui.house_view import HouseView

class UI:
    """Class representing the user interface.

    Args:
        root (tk.Tk): The root Tkinter window.
    """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
       """Starts the user interface by displaying the login view."""
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_registration(self):
        self._show_registration_view()

    def _handle_assessment(self, user):
        self._show_assessment_view(user)

    def _handle_house(self, user):
        self._show_house_view(user)

    def _handle_login(self):
        self._show_login_view()

    def _handle_administration(self, administrator):
        self._show_administration_view(administrator)

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_assessment,
            self._handle_house,
            self._handle_registration,
            self._handle_administration
        )

    def _show_registration_view(self):
        self._hide_current_view()

        self._current_view = RegistrationView(
            self._root,
            self._handle_login,
            self._handle_assessment
        )

    def _show_assessment_view(self, user):
        self._hide_current_view()

        self._current_view = AssessmentView(
            self._root,
            self._handle_login,
            self._handle_house,
            user
        )

    def _show_administration_view(self, administrator):
        self._hide_current_view()

        self._current_view = AdministrationView(
            self._root,
            administrator,
            self._handle_login
        )

    def _show_house_view(self, user_id):
        self._hide_current_view()

        self._current_view = HouseView(
            self._root,
            self._handle_login,
            self._handle_assessment,
            user_id
        )
