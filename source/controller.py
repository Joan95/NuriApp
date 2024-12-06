class NutritionistController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self, data):
        self.model.add_user(
            data["name"],
            data["lastname"],
            data["email"],
            data["birthdate"],
            data["gender"]
        )

    def get_users(self):
        return self.model.get_users()

    def add_diet(self, pacient_id, start_date, end_date, description):
        self.model.add_diet(pacient_id, start_date, end_date, description)

    def get_patient_id(self, name, lastname):
        return self.model.get_patient_id(name, lastname)

    def get_current_diet(self, pacient_id):
        return self.model.get_current_diet(pacient_id)
