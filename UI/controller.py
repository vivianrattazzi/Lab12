import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._listCountry = self._model.getNazioni()
        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))

        self._listYear = self._model.getAnni()
        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))



    def handle_graph(self, e):
        nazioneSelezionata = self._view.ddcountry.value
        annoSelezionato = self._view.ddyear.value
        if nazioneSelezionata == "":
            self._view.create_alert(ft.Text("Non hai inserito la nazione"))
            return
        if annoSelezionato == "":
            self._view.create_alert(ft.Text("Non hai inserito l'anno"))
            return
        self._model.buildGraph(nazioneSelezionata, annoSelezionato)
        nodi = self._model.getNumNodes()
        archi = self._model.getNumEdges()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nodi} Numero di archi: {archi}"))
        self._view.update_page()




    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
