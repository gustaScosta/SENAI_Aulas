from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def listar_usuarios(self):
        return self.repository.listar_todos()
