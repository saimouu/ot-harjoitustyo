# Ohjelmistotekniikka, harjoitustyö

## 2048 Peli
2048 pelissä yhdistetään 4x4-ruudukossa olevia laattoja keskenään. Saman numeroisia laattoja pystyy yhdistämään, ja muodostunut laatta on niiden summa. Tavoitteena on saada 2048 numeroinen laatta.

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)
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
