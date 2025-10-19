from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock

from paginas.playstation import PlaystationScreen
from paginas.disney import DisneyScreen
from paginas.marvel import MarvelScreen
from paginas.starwars import StarWarsScreen
from paginas.xbox import XboxScreen
from paginas.home import HomeScreen
from paginas.login import LoginScreen  # Tela de login
from paginas.carrinho import CarrinhoScreen

# Tamanho da janela (opcional, para desktop)
Window.size = (420, 900)

# Gerenciador de telas
class Gerenciador(ScreenManager):
    pass

class HomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.show_first_banner, 0)
    
    def show_first_banner(self, dt):
        self.ids.subbanner_carousel.index = 0

class NerdHubApp(App):
    def build(self):
        # Carrega arquivos KV
        Builder.load_file("telas/home.kv")
        Builder.load_file("telas/login.kv")
        Builder.load_file("telas/playstation.kv")
        Builder.load_file("telas/xbox.kv")
        Builder.load_file("telas/marvel.kv")
        Builder.load_file("telas/starwars.kv")
        Builder.load_file("telas/disney.kv")
        Builder.load_file("telas/carrinho.kv")


        sm = Gerenciador()
        # Telas principais
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))

        # Telas das marcas
        sm.add_widget(PlaystationScreen(name="playstation"))
        sm.add_widget(XboxScreen(name="xbox"))
        sm.add_widget(MarvelScreen(name="marvel"))
        sm.add_widget(StarWarsScreen(name="starwars"))
        sm.add_widget(DisneyScreen(name="disney"))
        sm.add_widget(CarrinhoScreen(name="carrinho"))

        return sm
    
    def adicionar_ao_carrinho(self, produto):
        carrinho = self.root.get_screen("carrinho")
        carrinho.itens.append(produto)
        carrinho.atualizar_lista()

if __name__ == "__main__":
    NerdHubApp().run()
