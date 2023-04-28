"""Cerinte:
Creati un set de teste folosind modulul Pytest care sa acopere toate functionalitatile metodelor din clasa ServiceAuto.

Creati o clasa ServiceAuto cu urmatoarele atribute: nume, adresa si lista_masini_reparate.

Creati constructorul clasei care primeste numele si adresa service-ului ca parametri. Setati valorile atributelor corespunzatoare.

Creati o metoda "adauga_masina_reparatie" care primeste ca parametru o masina si o adauga in lista_masini_reparate.

Creati o metoda "sterge_masina_reparatie" care primeste ca parametru o masina si o sterge din lista_masini_reparate.

Creati o metoda "repara_masina" care primeste ca parametru o masina si o marcheaza ca reparata.
Acest lucru necesita schimbarea din string a obiectului masina in Obiect de tip Clasa, dictionar sau tuplu, la alegere.

Creati o metoda "verifica_masini_in_reparatie" care afiseaza numarul de masini in reparatie si numele lor.


Succes!"""


"""
Generatorii sunt tip special de iterabili.
Diferenta este ca informatia nu este blocata in memorie. Ea este generata in momentul in care este apelata functia next.
Functia generator foloseste cuvantul cheie yield care returneaza valorile una cate una la momentul apelarii.
O putem folosi la accesarea unor seturi mari de date.
Putem genera secvente si siruri de caractere.
"""
import random
import string
import datetime

def primul_nostru_generator():
    yield 1
    yield 2
    yield 3

gen = primul_nostru_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))


def secventa_la_putere(numar, putere):
    for i in range(numar):
        yield i ** putere

gen = secventa_la_putere(10, 3)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def generator_cod(lungime):
    caractere = string.digits + string.ascii_letters
    while True:
        cod_random = "".join(random.choices(caractere, k=lungime))
        yield cod_random

cod = generator_cod(10)
print(next(cod))
print(next(cod))
print(next(cod))
