class Aluno:
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def login(self, email, senha):
        print("login realizado com sucesso")

    def logout(self):
        print("logout realizado com sucesso")