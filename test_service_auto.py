import pytest
from service_auto import ServiceAuto
from masina import Masina

@pytest.fixture
def service():
    nume_service = "Service Auto Test"
    adresa_service = "Calea Bucuresti 185"
    service_test = ServiceAuto(nume_service, adresa_service)
    yield service_test

@pytest.fixture
def automobil():
    model = "Stelvio"
    an_de_fabricatie = 2022
    status_reparatie = False
    auto_test = Masina(model, an_de_fabricatie, status_reparatie)
    yield auto_test

def test_creare_obiect_ServiceAuto():
    nume_service = "Service Auto Test"
    adresa_service = "Calea Bucuresti 185"
    service_test = ServiceAuto(nume_service, adresa_service)

    assert service_test.nume_service == nume_service
    assert service_test.adresa_service == adresa_service
    assert  len(service_test.lista_masini_reparate) == 0

def test_verificare_adaugare_masina_reparata():
    nume_service = "Service Auto Test"
    adresa_service = "Calea Bucuresti 185"
    service_test = ServiceAuto(nume_service, adresa_service)
    masina_test = ("X5", 2019, False)
    service_test.adauga_masina_reparata(masina_test)

    assert masina_test in service_test.lista_masini_reparate

def test_verificare_sterge_masina_reparata():
    model_masina = "Stelvio"
    an_de_fabricatie = 2022
    status_reparatie = False
    masina_test = Masina(model_masina, an_de_fabricatie, status_reparatie)

    nume_service = "Service Auto Test"
    adresa_service = "Calea Bucuresti 185"
    service_test = ServiceAuto(nume_service, adresa_service)
    service_test.adauga_masina_reparata(masina_test)
    service_test.sterge_masina_reparata(masina_test)

    assert masina_test not in service_test.lista_masini_reparate

def test_repara_masina():
    model_masina = "Stelvio"
    an_de_fabricatie = 2022
    status_reparatie = False
    masina_test = Masina(model_masina, an_de_fabricatie, status_reparatie)

    nume_service = "Service Auto Test"
    adresa_service = "Calea Bucuresti 185"
    service_test = ServiceAuto(nume_service, adresa_service)

    service_test.repara_masina(masina_test)
    assert masina_test.status_reparatie == True

# def test_verifica_masini_in_reparatiew():
#     model_masina = "Stelvio"
#     an_de_fabricatie = 2022
#     status_reparatie = False
#     masina_test1 = Masina(model_masina, an_de_fabricatie, status_reparatie)
#
#     model_masina = "Tonale"
#     an_de_fabricatie = 2022
#     status_reparatie = False
#     masina_test2 = Masina(model_masina, an_de_fabricatie, status_reparatie)
#
#     nume_service = "Service Auto Test"
#     adresa_service = "Calea Bucuresti 185"
#     service_test = ServiceAuto(nume_service, adresa_service)
#
#     service_test.adauga_masina_reparata(masina_test1)
#     service_test.adauga_masina_reparata(masina_test2)
#
#     assert len(service_test.lista_masini_reparate)