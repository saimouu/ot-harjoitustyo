# Ohjelmistotekniikka, harjoitustyö

## 2048 Peli
2048 pelissä yhdistetään 4x4-ruudukossa olevia laattoja keskenään. Saman numeroisia laattoja pystyy yhdistämään, ja muodostunut laatta on niiden summa. Tavoitteena on saada 2048 numeroinen laatta.

[Releaset](https://github.com/saimouu/ot-harjoitustyo/releases/)

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

## Asennus
Asenna projektin riippuvuudet:
```
poetry install
```
Käynnistä sovellus:
```
poetry run invoke start
```

## Komentorivitoiminnot
Ohjelman käynnistys:
```
poetry run invoke start
```
Testien suorittaminen:
```
poetry run invoke test
```
Testikattavuusraportin generointi htmlcov-hakemistoon:
```
poetry run invoke coverage-report
```
Pylint `.pylintrc`-tiedoston määrityksien mukaan:
```
poetry run invoke lint
```
