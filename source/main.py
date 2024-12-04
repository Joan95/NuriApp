from error_cfg import *
from os import path
from tkinter import Tk
from model import NutritionistModel
from view import NutritionistView
from controller import NutritionistController


def main():
    root = Tk()

    root.geometry('800x600')
    root.resizable(True, True)

    try:
        model = NutritionistModel(path.join('..', 'database', 'nutriDB.sql'))
    except FileNotFoundError:
        print("Error! Database was not found, please check its path")
        exit(ERROR_CODE_DATABASE_NOT_FOUND)

    view = NutritionistView(root)  # Initialize view without the controller
    controller = NutritionistController(model, view)  # Create controller
    view.set_controller(controller)  # Assign controller to view and load users

    root.mainloop()

    # Close the model connection when the app closes
    model.close()


if __name__ == '__main__':
    main()
