# paginas/home.py
import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class ProductCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()
    image = StringProperty()

class HomeScreen(Screen):
    def on_pre_enter(self):
        """Garante que o banco exista e tenha produtos"""
        self.criar_banco()
        self.carregar_produtos()

    def criar_banco(self):
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

        # Se o banco estiver vazio, insere os produtos iniciais
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        if total == 0:
            produtos_iniciais = [
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
                produtos_iniciais
            )
            conexao.commit()

        conexao.close()

    def carregar_produtos(self):
        """Carrega produtos do banco e exibe na tela"""
        conexao = sqlite3.connect("banco/produtos.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT title, price, image FROM produtos")
        produtos = cursor.fetchall()
        conexao.close()

        grid = self.ids.products_grid
        grid.clear_widgets()

        for p in produtos:
            card = ProductCard(title=p[0], price=p[1], image=p[2])
            grid.add_widget(card)

    def ir_para_tela(self, tela):
        self.manager.current = tela
