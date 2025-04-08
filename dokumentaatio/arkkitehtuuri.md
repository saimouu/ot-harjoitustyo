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
```
