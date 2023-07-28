from usuario import Usuario
from logger import Logger

class AspectoLogin:
    def __init__(self, usuario):
        self.usuario = usuario
        self.logger = Logger()

    def fazer_login_aspecto(self, senha_digitada):
        sucesso = senha_digitada == self.usuario.senha
        self.usuario.fazer_login(senha_digitada)
        self.logger.log_acesso(self.usuario, sucesso)

if __name__ == "__main__":
    usuario1 = Usuario("usuario123", "senha123")

    aspecto_login = AspectoLogin(usuario1)

    # Teste de login
    aspecto_login.fazer_login_aspecto("senha123")  # Login bem-sucedido
    aspecto_login.fazer_login_aspecto("senhaerrada")  # Tentativa de login malsucedida
