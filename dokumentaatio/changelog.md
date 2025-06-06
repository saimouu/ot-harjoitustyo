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

## Viikko 5
- Pelaaja pystyy perumaan siirron kaksi kertaa pelin aikana
- Lisätty pääruutuun retry- ja quit-napit
- Score-näkymässä näkyy pisteiden lisäksi myös isoin saatu laatta ja liu'utusten lukumäärä
- Suurimman osan nappien mm. score, quit ja undo tapahtumankäsittely testattu

## Viikko 6
- Lisätty lyhyt info-ruutu
- Tapahtuman käsittely refaktoroitu omaan `EventHandler`-luokkaan
- `GameLoop`-luokan testit refaktoroitu `EventHandler`-luokan testeiksi
- Loput nappien tapahtumankäsittelyistä testattu

## Viikko 7
- Testattu, että `GameLoop` ja `EventHandler` toimivat yhdessä oikein painaessa oikeaa nuolinäppäintä
- Testattu, että peli näyttää häviöruudun kun peli on ohi, ja voittoruudun kun on saatu 2048-laatta
- Testattu, että "exit" tapahtuma sulkee popup ruudun
