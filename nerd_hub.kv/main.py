# main.py
import os
import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from database import criar_tabelas

# Importação das telas
from paginas.playstation import PlaystationScreen
from paginas.disney import DisneyScreen
from paginas.marvel import MarvelScreen
from paginas.starwars import StarWarsScreen
from paginas.xbox import XboxScreen
from paginas.home import HomeScreen
from paginas.login import LoginScreen
from paginas.carrinho import CarrinhoScreen

# Tamanho da janela (para teste no desktop)
Window.size = (420, 900)


# -------------------------------
#  GERENCIADOR DE TELAS
# -------------------------------
class Gerenciador(ScreenManager):
    pass


# -------------------------------
#  APP PRINCIPAL
# -------------------------------
class NerdHubApp(App):
    def build(self):
        criar_tabelas()
        # Garante que o banco de dados exista
        self.criar_banco()

        # Carrega os arquivos .kv
        Builder.load_file("telas/home.kv")
        Builder.load_file("telas/login.kv")
        Builder.load_file("telas/playstation.kv")
        Builder.load_file("telas/xbox.kv")
        Builder.load_file("telas/marvel.kv")
        Builder.load_file("telas/starwars.kv")
        Builder.load_file("telas/disney.kv")
        Builder.load_file("telas/carrinho.kv")

        # Cria o gerenciador de telas
        sm = Gerenciador()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(PlaystationScreen(name="playstation"))
        sm.add_widget(XboxScreen(name="xbox"))
        sm.add_widget(MarvelScreen(name="marvel"))
        sm.add_widget(StarWarsScreen(name="starwars"))
        sm.add_widget(DisneyScreen(name="disney"))
        sm.add_widget(CarrinhoScreen(name="carrinho"))

        return sm

    # -------------------------------
    #  BANCO DE DADOS
    # -------------------------------
    def criar_banco(self):
        """Cria o banco e popula produtos iniciais se necessário"""
        os.makedirs("banco", exist_ok=True)
        conexao = sqlite3.connect("banco/produtos.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price TEXT NOT NULL,
                image TEXT
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]

        if total == 0:
            produtos = [
                ("FORZA - Xbox Series X", "R$ 179,00", "imagens/forza.jpg"),
                ("LEGO Minecraft - Aventura", "R$ 1.349,90", "imagens/lego_minecraft.jpg"),
                ("PlayStation 5 Pro", "R$ 6.509,00", "imagens/ps5.jpg"),
                ("PlayStation Portal", "R$ 1.349,90", "imagens/portal.jpg"),
                ("Funko Pop! Star Wars", "R$ 389,90", "imagens/funko.jpg"),
                ("Camiseta Marvel Avengers", "R$ 82,35", "imagens/camiseta_marvel.jpg"),
                ("Pelúcia Chewbacca", "R$ 141,50", "imagens/chewbacca.jpg"),
                ("LEGO Star Wars - 75257", "R$ 201,00", "imagens/lego_starwars.jpg"),
            ]
            cursor.executemany(
                "INSERT INTO produtos (title, price, image) VALUES (?, ?, ?)",
                produtos
            )
            conexao.commit()

        conexao.close()

    # -------------------------------
    #  CARRINHO
    # -------------------------------
    def adicionar_ao_carrinho(self, produto):
        """Adiciona um produto ao carrinho"""
        carrinho = self.root.get_screen("carrinho")
        carrinho.itens.append(produto)
        carrinho.atualizar_lista()


if __name__ == "__main__":
    NerdHubApp().run()
