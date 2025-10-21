from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
from database import cadastrar_usuario, verificar_login


class LoginScreen(Screen):
    mensagem = StringProperty("")

    def fazer_login(self):
        email = self.ids.email_input.text
        senha = self.ids.senha_input.text
        usuario = verificar_login(email, senha)
        if usuario:
            self.mensagem = f"Bem-vindo, {usuario[1]}!"
            self.manager.current = "home"
        else:
            self.mensagem = "Email ou senha incorretos."

    def cadastrar(self):
        nome = self.ids.nome_input.text
        email = self.ids.email_input.text
        senha = self.ids.senha_input.text
        if cadastrar_usuario(nome, email, senha):
            self.mensagem = "Cadastro realizado com sucesso!"
        else:
            self.mensagem = "Email já cadastrado!"
