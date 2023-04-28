from masina import Masina

class ServiceAuto():
    def __init__(self, nume_service, adresa_service):
        self.nume_service = nume_service
        self.adresa_service = adresa_service
        self.lista_masini_reparate = []

    def adauga_masina_reparata(self, masina):
        self.lista_masini_reparate.append(masina)
        return self.lista_masini_reparate

    def sterge_masina_reparata(self, masina):
        self.lista_masini_reparate.remove(masina)
        return self.lista_masini_reparate

    def repara_masina(self,masina):
        masina.status_reparatie = True

    def verifica_masini_in_reparatie(self):
        print(len(self.lista_masini_reparate))
        for masina in self.lista_masini_reparate:
            print(masina.model)

serv1 = ServiceAuto("Serv1", "Bla, nr. 1")
car1 = Masina("Stelvio", 2022, "False")
car2 = Masina("Tonale", 2022, "False")
serv1.adauga_masina_reparata(car1)
serv1.adauga_masina_reparata(car2)
serv1.verifica_masini_in_reparatie()