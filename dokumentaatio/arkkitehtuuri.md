## Alustava rakenne
```mermaid
 classDiagram
  GameLoop "1" -- "1" GameLogic
  GameLoop "1" -- "1" EventQueue
  GameLoop "1" -- "1" Clock
  GameLoop "1" -- "1" ScoreRepository
  GameLoop "1" --> "1" Renderer
  Renderer --> GameLoop
  note for Renderer "UI main class"
  Renderer --> GameLogic : gets block positions to render
```
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
    EventQueue -->> GameLoop : event, left key down
    GameLoop ->> GameLogic : move_all_blocks_left()
    GameLoop ->> GameLogic : spawn_random_block()
    GameLogic -->> UI : (block positions updated)
    GameLoop ->> GameLogic : check_win()
    GameLogic -->> GameLoop : false
    GameLoop ->> GameLogic : check_game_over()
    GameLogic -->> GameLoop : false
    GameLoop ->> UI : render()
    UI -->> Player : Updated screen
```
