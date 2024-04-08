from tkinter import Tk
from ui.ui import UI 

from config import DATABASE_PATH

print(DATABASE_PATH)
def main():
    window = Tk()
    window.title("House app")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
