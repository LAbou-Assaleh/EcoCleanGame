# EcoClean

EcoClean is a local **Pygame** game that blends:
- a **Minesweeper-style** “e-waste zone clearing” challenge (Easy / Medium / Hard), and  
- a **2048-style** “Compacter” minigame where you merge tiles to score points,

with a simple **local login/signup** system and a **persistent leaderboard** stored in CSV files.

---

## Features

- Minesweeper zones in **three difficulties**
- **Compacter (2048-like)** mode for scoring
- **Multiplier system**: clearing zones increases your multiplier, which boosts your Compacter score
- **Local accounts** and **leaderboard persistence** via CSV (no server required)

---

## Tech Stack

- Python 3
- Pygame
- CSV persistence (accounts + leaderboard)

---

# EcoClean

EcoClean is a local **Pygame** game that blends:
- a **Minesweeper-style** “e-waste zone clearing” challenge (Easy / Medium / Hard), and  
- a **2048-style** “Compacter” minigame where you merge tiles to score points,

with a simple **local login/signup** system and a **persistent leaderboard** stored in CSV files.

---

## Features

- Minesweeper zones in **three difficulties**
- **Compacter (2048-like)** mode for scoring
- **Multiplier system**: clearing zones increases your multiplier, which boosts your Compacter score
- **Local accounts** and **leaderboard persistence** via CSV (no server required)

---

## Tech Stack

- Python 3
- Pygame
- CSV persistence (accounts + leaderboard)

---

## Getting Started

### Requirements
- Python 3.x
- `pygame`

Install dependency:

```bash
python -m pip install pygame
```

## Run

Run the game from the folder that contains main.py, trash.png, and the CSV files:
```bash
python main.py
```

⸻

## How to Play

#Login / Sign Up

On launch, choose:
- Login (existing account)
- Sign Up (create a new account)

# Constraints:
- Username: max 10 characters
- Password: max 10 characters

Account data is stored locally in acount.csv.

⸻

## Controls

# Minesweeper Zones (Easy / Medium / Hard)
- Left click: reveal a cell
- Right click: flag/unflag a cell
- Revealing a mine ends the run and resets your multiplier.
- Win by revealing all non-mine cells.

# Compacter (2048-style)
- Arrow keys: move tiles (Up / Down / Left / Right)
- Matching tiles merge to increase score.
- When no moves remain, the mode ends and your score is finalized.

# Home Button
- A circular home button appears near the bottom of gameplay screens.
- Click it to return to the menu.

⸻

## Scoring & Multiplier
- Starting multiplier: 0.5
- Zone wins increase multiplier:
- Easy win: +0.5
- Medium win: +2.5
- Hard win: +5.5

Final score after Compacter:

total_score = int(compacter_score * multiplier)

The leaderboard is updated if total_score exceeds a previous best (or qualifies for ranking).

⸻

## Project Structure

EcoClean/
  main.py
  trash.png
  acount.csv
  leaderboard.csv
  
⸻

## Security Note

EcoClean is designed to run entirely offline and locally. 
Account data is stored in acount.csv in a simple format to keep the project lightweight and easy to understand. 
As a result, usernames/passwords are saved in plaintext—this was an intentional tradeoff for simplicity, since security was not a design goal for this project.

⸻

## Troubleshooting

Missing file errors (e.g., trash.png or CSVs): Run python main.py from the project directory (where the files exist).
Pygame not found: python -m pip install pygame



⸻

## License

Licensed under the Apache License 2.0. See LICENSE for details.
