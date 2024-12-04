from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Listbox, Scrollbar, OptionMenu


class NutritionistView:
    def __init__(self, root):
        self.controller = None  # Initially, controller is None
        self.root = root
        self.root.title("Nutritionist Database")

        # Define StringVars for form inputs
        self.name_var = StringVar()
        self.lastname_var = StringVar()
        self.email_var = StringVar()
        self.birthdate_day_var = StringVar()
        self.birthdate_month_var = StringVar()
        self.birthdate_year_var = StringVar()
        self.gender_var = StringVar()
        self.start_date_day_var = StringVar()
        self.start_date_month_var = StringVar()
        self.start_date_year_var = StringVar()
        self.end_date_day_var = StringVar()
        self.end_date_month_var = StringVar()
        self.end_date_year_var = StringVar()
        self.description_var = StringVar()

        # Create main frame for holding other frames
        self.main_frame = Frame(root)
        self.main_frame.pack(side="top", fill="both", expand=True)

        # Create menu frames
        self.main_menu_frame = Frame(self.main_frame)
        self.add_user_frame = Frame(self.main_frame)
        self.add_diet_frame = Frame(self.main_frame)  # Initialize add_diet_frame

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

        # Create a frame to hold the Listbox and Scrollbar
        listbox_frame = Frame(self.main_menu_frame)
        listbox_frame.pack(pady=10, fill="both", expand=True)

        self.user_listbox = Listbox(listbox_frame)
        self.user_listbox.pack(side="left", fill="both", expand=True)

        # Add a Scrollbar
        scrollbar = Scrollbar(listbox_frame, orient="vertical", command=self.user_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.user_listbox.config(yscrollcommand=scrollbar.set)

        self.add_user_button = Button(self.main_menu_frame, text="Afegir un Pacient", command=self.show_add_user_menu)
        self.add_user_button.pack(pady=10)

        # Button to create a new diet
        self.add_diet_button = Button(self.main_menu_frame, text="Crear Nova Dieta", command=self.show_add_diet_menu)
        self.add_diet_button.pack(pady=10)

    def create_add_user_menu(self):
        # Configure grid for centering
        for i in range(8):  # Total rows for form
            self.add_user_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # Total columns for form
            self.add_user_frame.grid_columnconfigure(i, weight=1)

        Label(self.add_user_frame, text="Nom").grid(row=0, column=1, sticky='e')
        Entry(self.add_user_frame, textvariable=self.name_var).grid(row=0, column=2)

        Label(self.add_user_frame, text="Cognoms").grid(row=1, column=1, sticky='e')
        Entry(self.add_user_frame, textvariable=self.lastname_var).grid(row=1, column=2)

        Label(self.add_user_frame, text="Email").grid(row=2, column=1, sticky='e')
        Entry(self.add_user_frame, textvariable=self.email_var).grid(row=2, column=2)

        Label(self.add_user_frame, text="Data de naixement (Dia, Mes, Any)").grid(row=3, column=1, sticky='e')

        days = [str(i) for i in range(1, 32)]
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        OptionMenu(self.add_user_frame, self.birthdate_day_var, *days).grid(row=3, column=2, sticky='w')
        OptionMenu(self.add_user_frame, self.birthdate_month_var, *months).grid(row=3, column=3, sticky='w')
        Entry(self.add_user_frame, textvariable=self.birthdate_year_var, width=5).grid(row=3, column=4, sticky='w')

        Label(self.add_user_frame, text="Sexe (HOME/DONA)").grid(row=4, column=1, sticky='e')

        sexes = ["HOME", "DONA"]
        OptionMenu(self.add_user_frame, self.gender_var, *sexes).grid(row=4, column=2, sticky='w')

        Button(self.add_user_frame, text="Afegir nou Pacient", command=self.add_user).grid(row=5, column=1,
                                                                                           columnspan=2)
        Button(self.add_user_frame, text="Anar al Menú Principal", command=self.show_main_menu).grid(row=6, column=1,
                                                                                                     columnspan=2)

    def show_main_menu(self):
        self.add_user_frame.pack_forget()
        self.add_diet_frame.pack_forget()
        self.main_menu_frame.pack(side="top", fill="both", expand=True)
        self.load_users()

    def show_add_user_menu(self):
        self.main_menu_frame.pack_forget()
        self.add_diet_frame.pack_forget()
        self.add_user_frame.pack(side="top", fill="both", expand=True)

    def show_add_diet_menu(self):
        selected_indices = self.user_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Compte!", "Sisuplau selecciona un pacient.")
            return

        selected_index = selected_indices[0]
        self.selected_patient = self.user_listbox.get(selected_index)

        self.main_menu_frame.pack_forget()
        self.add_user_frame.pack_forget()
        self.add_diet_frame.pack(side="top", fill="both", expand=True)

        self.create_diet_form()

    def create_diet_form(self):
        # Configure grid for centering
        for i in range(8):  # Total rows for form
            self.add_diet_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):  # Total columns for form
            self.add_diet_frame.grid_columnconfigure(i, weight=1)

        Label(self.add_diet_frame, text="Data d'inici (Dia, Mes, Any)").grid(row=0, column=1, sticky='e')

        start_days = [str(i) for i in range(1, 32)]
        start_months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        OptionMenu(self.add_diet_frame, self.start_date_day_var, *start_days).grid(row=0, column=2, sticky='w')
        OptionMenu(self.add_diet_frame, self.start_date_month_var, *start_months).grid(row=0, column=3, sticky='w')
        Entry(self.add_diet_frame, textvariable=self.start_date_year_var, width=5).grid(row=0, column=4, sticky='w')

        Label(self.add_diet_frame, text="Data de finalització (Dia, Mes, Any)").grid(row=1, column=1, sticky='e')

        end_days = [str(i) for i in range(1, 32)]
        end_months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        OptionMenu(self.add_diet_frame, self.end_date_day_var, *end_days).grid(row=1, column=2, sticky='w')
        OptionMenu(self.add_diet_frame, self.end_date_month_var, *end_months).grid(row=1, column=3, sticky='w')
        Entry(self.add_diet_frame, textvariable=self.end_date_year_var, width=5).grid(row=1, column=4, sticky='w')

        Label(self.add_diet_frame, text="Descripció").grid(row=2, column=1, sticky='e')
        Entry(self.add_diet_frame, textvariable=self.description_var).grid(row=2, column=2)

        Button(self.add_diet_frame, text="Afegir Dieta", command=self.add_diet).grid(row=3, column=1, columnspan=2)
        Button(self.add_diet_frame, text="Anar al Menú Principal", command=self.show_main_menu).grid(row=4, column=1,
                                                                                                     columnspan=2)
    def load_users(self):
        if self.controller:
            users = self.controller.get_users()
            user_count = len(users)
            if user_count == 0:
                self.user_count_label.config(text="No hi ha Pacients encara.")
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
            "birthdate": f"{self.birthdate_year_var.get()}-{self.birthdate_month_var.get()}-{self.birthdate_day_var.get()}",
            "gender": self.gender_var.get()
        }
        if not all([data['name'], data['lastname'], data['email'], data['birthdate'], data['gender']]):
            messagebox.showerror("Compte!", "Sisuplau omple tots els camps.")
            return
        self.controller.add_user(data)
        messagebox.showinfo("Ha estat un éxit!", "Pacient afegit correctament a la base de dades!")
        self.clear_fields()
        self.show_main_menu()

    def add_diet(self):
        start_date = f"{self.start_date_year_var.get()}-{self.start_date_month_var.get()}-{self.start_date_day_var.get()}"
        end_date = f"{self.end_date_year_var.get()}-{self.end_date_month_var.get()}-{self.end_date_day_var.get()}"
        description = self.description_var.get()

        if not all([start_date]):
            messagebox.showerror("Compte!", "Sisuplau omple tots els camps.")
            return

        pacient_info = self.selected_patient.split()
        pacient_name = pacient_info[0]
        pacient_lastname = " ".join(pacient_info[1:]) if len(pacient_info) > 1 else ""

        pacient_id = self.controller.get_patient_id(pacient_name, pacient_lastname)

        self.controller.add_diet(pacient_id, start_date, end_date, description)
        messagebox.showinfo("Ha estat un éxit!", "Dieta afegida correctament a la base de dades!")
        self.clear_diet_fields()
        self.show_main_menu()

    def clear_diet_fields(self):
        self.start_date_day_var.set("")
        self.start_date_month_var.set("")
        self.start_date_year_var.set("")
        self.end_date_day_var.set("")
        self.end_date_month_var.set("")
        self.end_date_year_var.set("")
        self.description_var.set("")
