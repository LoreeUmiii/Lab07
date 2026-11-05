import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self ):
        # --- Popolamento DropDown Biblioteche ---
        self._view._ddBiblioteca.options.clear()
        self._view._ddBiblioteca.options.append(
            ft.dropdown.Option(key = "NONE", text = "Nessun Filtro")
        )
        biblioteche = self._model.get_biblioteche()
        #print(biblioteche)
        for biblioteca in biblioteche:
            self._view._ddBiblioteca.options.append(
                ft.dropdown.Option(
                    key = str(biblioteca.id),
                    text = str(biblioteca.nome) ) )

        # --- Popolamento DropDown Generi ---
        self._view._ddGenere.options.clear()
        self._view._ddGenere.options.append(
            ft.dropdown.Option(key = "NONE", text = "Nessun Filtro")
        )
        generi = self._model.get_generi()
        for genere in generi:
            self._view._ddGenere.options.append(
                ft.dropdown.Option(
                    key = str(genere), text = str(genere) )
            )

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handle_sel_biblioteche(self):
        key = self._view._ddBiblioteca.value
        if key == "NONE" or not key:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = key

    def handle_sel_genere(self):
        key = self._view._ddGenere.value
        if key == "NONE" or not key:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = key

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata,
                                               self.genere_selezionato)
        self._view.lista_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun filtro attivato ")
        else:
            for libro in libri:
                txt_item = f"📖 {libro.titolo} | Autore: {getattr(libro, 'autore', 'N/D')} | Genere: {getattr(libro, 'genere', 'N/D')}"
                self._view.lista_libri.append(ft.Text(txt_item))