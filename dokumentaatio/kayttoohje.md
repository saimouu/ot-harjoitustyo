# Käyttöohje
## Asennus ja käynnistys
1. Varmista, että Python vesrsio on vähintään 3.10
2. Lataa pelin uusin [release](https://github.com/saimouu/ot-harjoitustyo/releases/latest) *Source code* kohdasta `Assets`-osion alta, ja pura se
3. Mene pelin juurihakemistoon ja asenna projektin riippuvuudet komennolla:
```
poetry install
```
4. Käynnistä peli komennolla:
```
poetry run invoke start
```
## Peliohjeet
### Controllit
Laattoja liu'utetaan nuoli näppäimillä (<kbd>&#8592;</kbd> <kbd>&#8593;</kbd> <kbd>&#8594;</kbd> <kbd>&#8595;</kbd>).

Peliruudun alhaalla olevien nappien painaminen onnistuu käyttäen hiirtä.

### Napit
- *Scores* avaa highscores-näkymän, jossa voi tarkastella viittä parhainta tulosta
- *Undo* peruu tehdyn siirron, jos tämä on mahdollista
- *Retry* aloittaa pelin alusta ja tallentaa tuloksen
- *Quit* Sulkee pelin ja tallentaa tuloksen
- *?* Näyttää lyhyen ohjeen pelistä

### Pelin säännöt ja tavoite
Pelin tavoitteena on saada 2048 numeroinen laatta, mutta peliä voi tämän jälkeen jatkaa painamalla *continue*-näppäintä, joka ilmestyy 2048-laatan saatua *You Win*-ikkunaan.

Pelin aikana siirron voi perua kaksi kertaa.

Pelin tulos tallennetaan pelin loppuessa (Game Over) tai kun pelaaja painaa *retry*- tai *quit*-nappia. 
