class Masina():
    def __init__(self, model, an_de_fabricatie, status_reparatie):
        self.model = model
        self.an_de_fabricatie = an_de_fabricatie
        self.status_reparatie = status_reparatie

    def marcheaza_masina_ca_fiind_reparata(self):
        self.status_reparatie = True