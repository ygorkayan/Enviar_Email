import smtplib

class Enviar_Email:

    """ Classe feita para mandar email usando o Gmail """

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.email = None

    def _criar_conexao(self):
        if self.email.ehlo()[0] == 250:
            print("Conexao estabelecida")
        else:
            raise Exception("Erro ao se conectar")

    def _iniciar_criptografia(self):
        if self.email.starttls()[0] == 220:
            print("Criptografia iniciada")
        else:
            raise Exception("Erro ao iniciar criptografia")

    def conectar(self):
        self.email = smtplib.SMTP("smtp.gmail.com", 587)

        self._criar_conexao()

        self._iniciar_criptografia()

        self.email.login(self.usuario, self.senha)

    def desconectar(self):
        self.email.quit()

    def Enviar(self, destinatario, assunto, mensagem):
        self.email.sendmail(self.usuario, destinatario,
                            f"Subject: {assunto}\n\n {mensagem}")
