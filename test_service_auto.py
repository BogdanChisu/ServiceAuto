# from data_ex import Data
#
# @pytest.fixture()
# def prepared_object():
#     data = Data()
#     data.prepare("John", "Smith")
#     yield data
#     data.prepare("John", "Smith")

import pytest
from service_auto import ServiceAuto
from masina import Masina

@pytest.fixture()
def prep_car():
    car1 = Masina("Stelvio", 2022, False)
    yield car1

@pytest.fixture()
def prep_car1():
    car2 = Masina("Giulia", 2022, False)
    yield car2

@pytest.fixture()
def prep_service():
    serv1 = ServiceAuto("Service Auto Test", "Calea Dorobantilor 185")
    yield serv1

def test_creation(prep_service: ServiceAuto):
    assert prep_service.nume_service == "Service Auto Test"

def test_adaugare_masina_in_lista_reparate(prep_service: ServiceAuto):
    prep_service.adauga_masina_reparata(prep_car)
    prep_service.adauga_masina_reparata(prep_car1)
    assert  len(prep_service.lista_masini_reparate) == 2

def test_stergere_masina_din_lista_reparate(prep_service: ServiceAuto):
    prep_service.adauga_masina_reparata(prep_car)
    prep_service.adauga_masina_reparata(prep_car1)
    prep_service.sterge_masina_reparata(prep_car1)
    assert len(prep_service.lista_masini_reparate) == 1

def test_marcheaza_masina_ca_fiind_reparata(prep_car: Masina):
    assert prep_car.status_reparatie == False
    prep_car.marcheaza_masina_ca_fiind_reparata()
    assert prep_car.status_reparatie == True

def test_adauga_in_lista_de_masina_in_curs_de_reparatie(prep_service: ServiceAuto):
    assert len(prep_service.lista_masini_in_reparatie) == 0
    prep_service.adauga_in_lista_de_masina_in_curs_de_reparatie(prep_car)
    prep_service.adauga_in_lista_de_masina_in_curs_de_reparatie(prep_car1)
    assert len(prep_service.lista_masini_in_reparatie) == 2