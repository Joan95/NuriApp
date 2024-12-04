from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Listbox, Scrollbar

class NutritionistView:
    def __init__(self, root):
        self.controller = None  # Initially, controller is None
        self.root = root
        self.root.title("Nutritionist Database")

        # Define StringVars for form inputs
        self.name_var = StringVar()
        self.lastname_var = StringVar()
        self.email_var = StringVar()
        self.birthdate_var = StringVar()
        self.gender_var = StringVar()

        # Create main frame for holding other frames
        self.main_frame = Frame(root)
        self.main_frame.pack(side="top", fill="both", expand=True)

        # Create menu frames
        self.main_menu_frame = Frame(self.main_frame)
        self.add_user_frame = Frame(self.main_frame)

        self.create_main_menu()
        self.create_add_user_menu()

        # Show main menu initially
        self.show_main_menu()

    def set_controller(self, controller):
        self.controller = controller
        self.load_users()

    def create_main_menu(self):
        self.main_menu_frame.pack(side="top", fill="both", expand=True)

        self.user_count_label = Label(self.main_menu_frame, text="")
        self.user_count_label.pack(pady=10)

        self.user_listbox = Listbox(self.main_menu_frame)
        self.user_listbox.pack(pady=10, fill="both", expand=True)

        self.add_user_button = Button(self.main_menu_frame, text="Add New Patient", command=self.show_add_user_menu)
        self.add_user_button.pack(pady=10)

    def create_add_user_menu(self):
        self.add_user_frame.pack(side="top", fill="both", expand=True)

        Label(self.add_user_frame, text="Name").grid(row=0, column=0)
        Entry(self.add_user_frame, textvariable=self.name_var).grid(row=0, column=1)

        Label(self.add_user_frame, text="Last Name").grid(row=1, column=0)
        Entry(self.add_user_frame, textvariable=self.lastname_var).grid(row=1, column=1)

        Label(self.add_user_frame, text="Email").grid(row=2, column=0)
        Entry(self.add_user_frame, textvariable=self.email_var).grid(row=2, column=1)

        Label(self.add_user_frame, text="Birthdate (YYYY-MM-DD)").grid(row=3, column=0)
        Entry(self.add_user_frame, textvariable=self.birthdate_var).grid(row=3, column=1)

        Label(self.add_user_frame, text="Gender (MALE/FEMALE)").grid(row=4, column=0)
        Entry(self.add_user_frame, textvariable=self.gender_var).grid(row=4, column=1)

        Button(self.add_user_frame, text="Add User", command=self.add_user).grid(row=5, column=0, columnspan=2)
        Button(self.add_user_frame, text="Back to Main Menu", command=self.show_main_menu).grid(row=6, column=0, columnspan=2)

    def show_main_menu(self):
        self.add_user_frame.pack_forget()
        self.main_menu_frame.pack(side="top", fill="both", expand=True)
        self.load_users()

    def show_add_user_menu(self):
        self.main_menu_frame.pack_forget()
        self.add_user_frame.pack(side="top", fill="both", expand=True)

    def load_users(self):
        if self.controller:
            users = self.controller.get_users()
            user_count = len(users)
            if user_count == 0:
                self.user_count_label.config(text="No users have been added yet.")
                self.user_listbox.delete(0, 'end')
            else:
                self.user_count_label.config(text=f"Number of users: {user_count}")
                self.user_listbox.delete(0, 'end')
                for user in users:
                    self.user_listbox.insert('end', f"{user['name']} {user['lastname']}")

    def add_user(self):
        data = {
            "name": self.name_var.get(),
            "lastname": self.lastname_var.get(),
            "email": self.email_var.get(),
            "birthdate": self.birthdate_var.get(),
            "gender": self.gender_var.get()
        }
        if not all([data['name'], data['lastname'], data['birthdate'], data['gender']]):
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return
        self.controller.add_user(data)
        messagebox.showinfo("Success", "User added successfully!")
        self.clear_fields()
        self.show_main_menu()

    def clear_fields(self):
        self.name_var.set("")
        self.lastname_var.set("")
        self.email_var.set("")
        self.birthdate_var.set("")
        self.gender_var.set("")
