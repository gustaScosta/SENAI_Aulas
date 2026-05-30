class User:
    def __init__(self, id_usuario: int, nome: str):
        self.id_usuario = id_usuario
        self.nome = nome

    def __repr__(self):
        return f'User(id_usuario={self.id_usuario}, nome={self.nome})'
