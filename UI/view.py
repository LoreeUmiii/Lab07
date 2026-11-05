import flet as ft
from flet.controls import alignment


from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        self._ddBiblioteca = None
        self._ddGenere = None
        self.lista_libri = None

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._ddBiblioteca = ft.Dropdown(label = "Biblioteche di Torino",
                                         width = 400,
                                         on_select = self.controller.handle_sel_biblioteche)
        self._ddGenere = ft.Dropdown(label = "Genere",
                                     width = 400,
                                    on_select = self.controller.handle_sel_genere)

        self.controller.popola_dropdown()
        # Sezione 3: Libri
        # TODO
        btn_libri = ft.Button(content = "Mostra Libri",
                                on_click = self.controller.mostra_libri )
        self.lista_libri = ft.ListView(expand = True, spacing = 5,
                                        padding = 10,  auto_scroll = True, )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row( spacing = 80,
                    controls = [self._ddBiblioteca, self._ddGenere],
                    alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            # TODO
            ft.Row( spacing = 80,
                    controls = [btn_libri],
                    alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            self.lista_libri,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
