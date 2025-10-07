from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class ProductCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()

class HomeScreen(Screen):
    def on_kv_post(self, base_widget):
        # Carousel de marcas
        marcas = [
            {"nome": "PlayStation", "cor": (0.15, 0.5, 0.85, 1), "tela": "playstation"},
            {"nome": "Xbox", "cor": (0, 0.6, 0, 1), "tela": "xbox"},
            {"nome": "Marvel", "cor": (0.8, 0, 0, 1), "tela": "marvel"},
            {"nome": "StarWars", "cor": (0, 0, 0, 1), "tela": "starwars"},
            {"nome": "Disney", "cor": (1, 0.85, 0, 1), "tela": "disney"},
        ]

        carousel = self.ids.subbanner_carousel
        carousel.clear_widgets()  # limpa antes de adicionar slides

        for marca in marcas:
            # Cada slide precisa ocupar todo o espaço
            slide = BoxLayout(size_hint=(1, 1), padding=dp(5))
            btn = Button(
                text=marca["nome"],
                background_normal='',
                background_color=marca["cor"],
                color=(1, 1, 1, 1),
                bold=True,
                on_release=lambda btn, tela=marca["tela"]: self.ir_para_tela(tela)
            )
            slide.add_widget(btn)
            carousel.add_widget(slide)

    def ir_para_tela(self, tela):
        self.manager.current = tela

    def on_enter(self):
        grid = self.ids.products_grid
        if len(grid.children) == 0:
            produtos = [
                {"title": "FORZA - Xbox Series X", "price": "R$ 179,00"},
                {"title": "LEGO Minecraft - Aventura", "price": "R$ 1.349,90"},
                {"title": "PlayStation 5 Pro", "price": "R$ 6.509,00"},
                {"title": "PlayStation Portal", "price": "R$ 1.349,90"},
                {"title": "Funko Pop! Star Wars", "price": "R$ 389,90"},
                {"title": "Camiseta Marvel Avengers", "price": "R$ 82,35"},
                {"title": "Pelúcia Chewbacca", "price": "R$ 141,50"},
                {"title": "LEGO Star Wars - 75257", "price": "R$ 201,00"},
            ]
            for p in produtos:
                card = ProductCard(title=p["title"], price=p["price"])
                grid.add_widget(card)
