# paginas/carrinho.py
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CarrinhoScreen(Screen):
    itens = ListProperty([])  # lista de dicionários de produto

    def atualizar_lista(self):
        layout = self.ids.carrinho_lista
        layout.clear_widgets()

        if not self.itens:
            layout.add_widget(Label(
                text="Seu carrinho está vazio.",
                size_hint_y=None,
                height=40,
                halign='center',
                valign='middle',
                text_size=(self.width, None)
            ))
            return

        for produto in self.itens:
            # Box principal do item
            box = BoxLayout(size_hint_y=None, height=60, padding=8, spacing=8)

            # Coluna esquerda: título e preço lado a lado
            left = BoxLayout(orientation='horizontal', size_hint_x=0.75, spacing=8)

            titulo = Label(
                text=produto.get("title", ""),
                halign='left',
                valign='middle',
                size_hint_x=0.7
            )
            preco = Label(
                text=produto.get("price", ""),
                halign='right',
                valign='middle',
                size_hint_x=0.3,
                color=(0, 0.6, 0, 1)
            )

            left.add_widget(titulo)
            left.add_widget(preco)

            # Coluna direita: botão remover
            right = BoxLayout(size_hint_x=0.25)
            remover = Button(
                text="Remover",
                size_hint=(1, None),
                height=40,
                background_normal='',
                background_color=(1, 0.3, 0.3, 1)
            )
            remover.bind(on_release=lambda btn, p=produto: self.remover_item(p))
            right.add_widget(remover)

            # Adiciona à linha principal
            box.add_widget(left)
            box.add_widget(right)
            layout.add_widget(box)

    def remover_item(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            self.atualizar_lista()
