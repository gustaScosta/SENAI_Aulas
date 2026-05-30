from app.models.user_model import User


class UserRepository:
    def listar_todos(self):
        return [User(1, 'Ana'), User(2, 'Joao')]
