class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def fazer_login(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"Usuário '{self.nome}' fez login com sucesso!")
        else:
            print(f"Erro: Senha incorreta para o usuário '{self.nome}'!")

    def fazer_registro(self):
        print(f"Usuário '{self.nome}' foi registrado com sucesso!")
