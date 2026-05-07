class Aluno:
    def __init__(self, nome, email, senha, telefone, data_nasc):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.data_nasc = data_nasc

    def login(self, email, senha):
        print("login realizado com sucesso")

    def logout(self):
        print("logout realizado com sucesso")