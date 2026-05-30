from app.services.user_service import UserService


class UserController:
    def __init__(self):
        self.service = UserService()

    def listar_usuarios(self):
        return self.service.listar_usuarios()
