# Testausdokumentti
Ohjelmaa on testattu automatisoiduin yksikkö- ja integraatiotesteillä, sekä manuaalisesti järjestelmätasolla.

## Yksikkö- ja integraatiotestatus
Kaikki testit ovat kirjoitettu [tests](src/tests/)-hakemistoon.
### Sovelluslogiikka
Pelin päälogiikasta vastaa `GameLogic`-luokka, jota testataan `TestGameLogic`-testiluokalla. Sillä `GameLogic` ei ole riippuvainen muista luokista, on sen metodeja testattu suoraan.

Eri painikkeiden klikkaus tapahtumia on testattu `TestButtonEventCalls`-testiluokassa. Jossa varmistetaan, että `EventHandler`-luokan sisäisiä funktioita kutsutaan oikein, ja sen tila muuttu oikein. Itse painikkeiden painallukset ovat näissä testeissä abstraktoitu pois.

Painikkeiden ja nappien toimivuutta on testattu `TestEventHandler`- ja `GameLoop`-testiluokissa.

### Repositorio-luokka
Repositorio-luokkaa `ScoreRepository` testataan `TestScoreRepository`-testiluokalla. Uusi testitiedosto luodaan jokaisen testin alussa ja poistetaan lopussa, jotta yli kirjoitusta oikean tiedoston kanssa ei tapahdu.

### Testauskattavuus
Käyttöliittymää lukuunottamatta pelin haaraumakattavuus on 88%. Myös `config.py` ja `main.py` on jätetty kattavuuden ulkopuolelle.


![](https://github.com/saimouu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/testikattavuus.png)


Puutteita jäi osittain nuolinäppäinten tapahtumien testaukseen. `Clock`- ja `EventQueue`-luokkia ei testattu, lähtökohtaisesti siitä syystä, että ne toimivat pelkästään wrappereinä pygamen päätoiminnallisuuksille.

# Järjestelmätestaus
Pelin järjestelmätestaus on tehty manuaalisesti, eli pelaamalla peliä ja käyttämällä eri toimintoja mahdollisimman kattavasti.

### Asennus ja käynnistys
Peli on ladattu ja käynnistetty [käyttöohjeen](dokumentaatio/kayttoohje.md) mukaan Cubbli Linux-ympäristössä.

### Toiminnallisuudet
Kaikkia [määrittelydokumentin](dokumentaatio/vaatimusmaarittely.md) perusversion tarjoaman toiminnallisuuksien toimintaa on testattu manuaalisesti. Peliä on yritetty rikkoa mahdollisimman kattavasti.
