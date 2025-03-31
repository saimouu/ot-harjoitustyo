# Changelog
## Viikko 3
- Pelaaja pystyy liu'uttamaan laattoja nuolinäppäimillä, ja saman numeroiset laatat yhdistyvät
- Peli päättyy kokonaan jos yhtäkään laattaa ei pysty enään yhdistämään, tai pelaaja onnistuu saamaan 2048 laatan
- Lisätty `GameLogic`-luokka, joka vastaa pelin tilan hallinnasta
- Lisätty `GameLoop`-luokka vastaamaan pelisilmukan pyörityksestä
- Lisätty `Clock`- ja `EventQueue`-luokka helpottamaan testausta
- Lisätty `config.py`, joka vastaa pelin vakioista, kuten näytön koosta
- `GameLogic`-luokan vastaamat laattojen yhdistämiset testattu täysillä riveillä ja kolumneilla
