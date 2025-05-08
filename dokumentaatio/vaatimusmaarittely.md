# Vaatimusmäärittely

## Pelin tarkoitus
2048 pelissä yhdistetään 4x4-ruudukossa olevia laattoja keskenään. Saman numeroisia laattoja pystyy yhdistämään, ja niiden muodostama laatta on niiden summa. Tavoitteena on saada 2048 numeroinen laatta, mutta peliä voidaan jatkaa myös tämän jälkeen. Peli loppuu kun koko ruudukko on täynnä laattoja, eikä yhtäkään pysty yhdistämään.

## Käyttäjät
Pelissä ei ole käyttäjiä, eli parhaimmat pistemäärät tallennetaan paikallisesti.

## Perusversion tarjoama toiminnallisuus
- Pelaaja voi siirtää laattoja nuolinäppäimillä // **tehty**
  - Siirron jälkeen, uusi laatta ilmestyy ruudukkoon, joka on joko 2 tai 4 arvoltaan
- Pelaaja näkee kertyneet pisteet // **tehty**
  - Pisteitä kertyy kun laatat yhdistyvät, niiden muodostaman laatan numeron verran
- Kun pelaaja saa 2048-laatan, näytetään "You Win!" näkymä // **tehty**
  - Samalla pelaajalta kysytään haluaako tämä jatkaa pelaamista 
- Peli loppuu kun koko ruudukko on täynnä laattoja, eikä yhtäkään laattaa pysty yhdistämään // **tehty**
  - Pelaajalle näytetään "Game Over!" näkymä.
- Pelaaja voi tarkastella viittä parhainta tulostaan // **tehty**
- Pelaaja voi perua siirron esim. kaksi kertaa pelin aikana // **tehty**
- "Retry"- ja "Quit"-napit pääruutuun // **tehty**
- Pelaaja pystyy näkemään parhaimpien tulosten suurimman laatan ja liu'utusten määrän // **tehty**
- Ohje ruutu, sillä tällä hetkellä ei ole selkeää mitä nappeja painamalla laattoja liu'utetaan // **tehty**

## Jatkokehitysideoita
- Suoritukset tallennetaan tietokantaan, jolloin pelaajat voivat tarkastella *globaalia* top 10 listaa
- Laatat liikkuvat *animoidusti* eikä välittömästi paikoilleen
