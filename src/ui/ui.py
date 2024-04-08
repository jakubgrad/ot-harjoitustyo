from tkinter import Tk
from ui.registration_view import RegistrationView
from ui.assessment_view import AssessmentView
from ui.login_view import LoginView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_registration(self):
        print("UI is handling registration")
        self._show_registration_view()

    def _handle_assessment(self):
        print("UI is handling assessment")
        self._show_assessment_view()

    def _handle_login(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_assessment,
            self._handle_registration
        )



    def _show_registration_view(self):
        print("attempt by UI to show registration view")
        self._hide_current_view()

        self._current_view = RegistrationView(
            self._root,
            self._handle_login
        )

        print("attempt by UI to show registration view finished")

    def _show_assessment_view(self):
        print("attempt by UI to show assessment view")
        self._hide_current_view()

        self._current_view = AssessmentView(
            self._root,
            self._handle_login
        )

        print("attempt by UI to show assessment view finished")


