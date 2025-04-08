# Changelog
## Viikko 3
- Pelaaja pystyy liu'uttamaan laattoja nuolinäppäimillä, ja saman numeroiset laatat yhdistyvät
- Peli päättyy kokonaan jos yhtäkään laattaa ei pysty enään yhdistämään, tai pelaaja onnistuu saamaan 2048 laatan
- Lisätty `GameLogic`-luokka, joka vastaa pelin tilan hallinnasta
- Lisätty `GameLoop`-luokka vastaamaan pelisilmukan pyörityksestä
- Lisätty `Clock`- ja `EventQueue`-luokka helpottamaan testausta
- Lisätty `config.py`, joka vastaa pelin vakioista, kuten näytön koosta
- `GameLogic`-luokan vastaamat laattojen yhdistämiset testattu täysillä riveillä ja kolumneilla

## Viikko 4
- Pelaaja näkee kertyneet pisteet
- Viittä parhainta tulosta pystyy tarkastelemaan "Score"-nappia painamlla
- Pelaajalle näytetää "You Win!"-näkymä kun saa 2048-laatan
  - Pelaaja voi jatkaa peliä "continue"-nappia painamalla
- Pelin päättyessä pelaajalla näytetään "You Lose!"-näkymä
  - Pelaaja voi aloittaa pelin alusta "retry"-nappia painamalla
- Lisätty `PopupScreen`-luokka ja sen perivät `HighScoreScreen`, `LoseScreen` ja `WinScreen`-luokat vastaamaan yllä mainuttujen toiminnallisuuksien UI-puolesta
- Lisätty `ScoreRepository` vastaamaan pisteiden tallentamisesta ja hakemisesta
- Testattu, että `GameLogic`-luokka ylläpitää pistemäärää oikein, ja että voitto ja pelin loppumis tarkistukset toimivat oikein
- Testattu, että `GameLoop`-luokka kutsuu vasemmalle siirtäessä vain kerran `move_all_blocks_left`-funktiota ja vain yksi uusi laatta luodaan
