from tkinter import Tk
from ui.hello_view import HelloView
from ui.good_bye_view import GoodByeView
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

    def _handle_good_bye(self):
        self._show_good_bye_view()

    def _handle_hello(self):
        self._show_hello_view()

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._handle_good_bye
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_good_bye,
            self._handle_good_bye
        )

        self._current_view.pack()


    def _show_good_bye_view(self):
        self._hide_current_view()

        self._current_view = GoodByeView(
            self._root,
            self._handle_hello
        )

        self._current_view.pack()

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()
