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

