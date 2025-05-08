# Arkkitehtuuri
## Rakenne
Pelin yleistason rakennetta ja yhteyksiä havainnollistaa seuraava luokkakaavio:
```mermaid
 classDiagram
  EventHandler "1" -- "1" GameLogic
  Renderer --> EventHandler : Returns button event results
  EventHandler "1" -- "1" ScoreRepository
  EventHandler "1" -- "1" GameLoop
  GameLoop "1" -- "1" EventQueue
  GameLoop "1" -- "1" Clock
  GameLoop "1" --> "1" Renderer
  Renderer --> GameLoop
  note for Renderer "UI main class"
  Renderer --> GameLogic : gets block positions to render
```
- `GameLogic` sisältää pelin logiikan ja tilan.
- `GameLoop` vastaa pelisilmukan pyörityksestä.
- `EventHandler` käsittelee käyttäjän syötteet ja vastaa popup-ikkunoiden tilan hallinnasta.
- `Renderer` vastaa pelin ja popup-ikkunoiden piirtämisestä ruudulle.
- `ScoreRepository` huolehtii tulosten tallennuksesta ja hakemisesta.
- `Clock` wrapper pygamen kellolle.
- `EventQueue` hakee pygame tapahtumat.
  
## Sovelluslogiikka
Peli käynnistetään `GameLoop`-luokan `run()` metodilla, jossa se pyörii silmukassa. 

Pelin päälogiikka ja tila sijaitsee `GameLogic`-luokassa. Pelaajan syötteet, kuten nuolinappien painallukset, prosessoidaan `EventHandler`-luokassa ja delegoidaan `GameLogic`-luokalle, joka huolehtii laattojen siirroista, pisteiden laskennasta sekä voitto- ja häviötilanteiden tarkituksesta. `EventHandler` huolehtii myös popup-ruutujen, kuten voitto- ja pistenäkymien tilan hallinnasta.

`Renderer`-luokka vastaa pelin piirtämisestä näytölle, ja päänäkymän nappien painalluksien palautusarvoista `EventHandler`-luokalle. Se hakee laattojen sijainnit ja muut tila arvot `GameLogic`-luokalta ja renderöi ne ruudulle. `Renderer`-luokka vastaa myös popup-ikkunoiden renderöinnistä, mutta näiden ikkunoiden nappien palautusarvojen vastuu on popup-ikkunaa vastaavalla `PopupScreen`-luokan aliluokalla.

Pisteiden pysyväistallennuksesta ja lukemisesta vastaa `ScoreRepository`, joka tallentaa pisteet pelin loputtua tai kun pisteikkuna avataan.

## Päätoiminnallisuudet
### Laattojen liu'uttaminen
Oletetaan, että peli on alustettu ja käynnistetty. Pelaajan painaessa peliruudussa ollessaan vasenta nuolinäppäintä, ja pelin jatkuessa tämän jälkeen, toimii sovelluksen logiikka sekvenssikaavion mukaan:
```mermaid
sequenceDiagram
    actor Player
    participant PygameEvents
    participant EventQueue
    participant GameLoop
    participant GameLogic
    participant UI
    Player ->> PygameEvents : press left key
    GameLoop ->> EventQueue : event_queue.get()
    Note over GameLoop, EventQueue: called every frame <br/> when game state is "playing" 
    EventQueue ->> PygameEvents : pygame.event.get()
    PygameEvents -->> EventQueue : event(s)
    EventQueue -->> GameLoop : event(s)
    GameLoop ->> EventHandler: handle_events(events)
    EventHandler ->> GameLogic: move_all_blocks_left()
    EventHandler ->> GameLogic: spawn_random_block()
    GameLogic -->> UI : (block positions updated)
    EventHandler ->> GameLogic : check_win()
    GameLogic -->> EventHandler : false
    EventHandler ->> GameLogic : check_game_over()
    GameLogic -->> EventHandler : false
    EventHandler -->> GameLoop : true
    GameLoop ->> UI : render()
    UI -->> Player : Updated screen
```
### Päänäkymän painikkeiden toiminta
Käytännössä jokaisen päänäkymän painikkeen klikkaus toimii samalla logiikalla. Seuraavassa kaaviossa esitetään ohjelman toiminta, kun käyttäjä painaa "Scores"-painiketta. Kaaviossa UI-komponentteja ovat `Renderer` ja `Button`.
```mermaid
sequenceDiagram
    actor Player
    participant PygameEvents
    participant EventQueue
    participant GameLoop
    participant EventHandler
    participant Renderer
    participant Button
    Player ->> PygameEvents : click "Scores"-button
    GameLoop ->> EventQueue : event_queue.get()
    Note over GameLoop, EventQueue: called every frame <br/> when game state is "playing" 
    EventQueue ->> PygameEvents : pygame.event.get()
    PygameEvents -->> EventQueue : event(s)
    EventQueue -->> GameLoop : event(s)
    GameLoop ->> EventHandler: handle_events(events)
    EventHandler ->> Renderer: handle_button_events(event)
    Renderer ->> Button : handle_event(event)
    Button -->> Renderer : "score"
    Renderer -->> EventHandler : "score"
    EventHandler ->> EventHandler : _handle_button_event("score")
    Note over EventHandler: Updates state and popup
    EventHandler -->> GameLoop : True
    GameLoop ->> Renderer : render(popup)
    Note over GameLoop, Renderer: GameLoop grabs updated state and popup object <br/> from EventHandler
    Renderer -->> Player : Updated screen with high scores popup
```
Jokaisella painikkella on `command`-atribuutti, joka määrittää, mitä `Button`-olio palauttaa, kun sen `hande_event`-metodia kutsutaan. Jos klikkauksen sijainti osuu painikkeen alueelle, palauttaa painike merkkijonon `command`-atribuuttin mukaan `Renderer`-oliolle, joka välittää sen edelleen `EventHandler`-oliolle. Painikkeet eivät siis itse muuta pelin tilaa suoraan, vaan varsinainen tapahtumankäsittely tehdään palautettujen arvojen perusteella `EventHandler`-luokassa. `EventHandler` muuttaa palautusarvojen perusteella omaa tilaansa, ja `GameLoop` hakee nämä tilan muutokset siltä.
