class Logger:
    def log_acesso(self, usuario, sucesso):
        if sucesso:
            print(f"Log: O usuário '{usuario.nome}' fez login com sucesso!")
        else:
            print(f"Log: Tentativa de login malsucedida para o usuário '{usuario.nome}'!")
