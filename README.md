# Higher‑Lower: Instagram Follower Count CLI Game

A quick terminal game where you guess which of two celebrities or brands has the larger Instagram following. Sharpen your pop‑culture radar and see how long you can keep the streak alive!

---

## Table of Contents

* [Gameplay](#gameplay)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running the Game](#running-the-game)
* [Project Structure](#project-structure)
* [Customising the Dataset](#customising-the-dataset)
* [Contributing](#contributing)
* [License](#license)

---

## Gameplay

```text
Compare A: Instagram, a Social media platform, from United States
 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Compare B: Cristiano Ronaldo, a Footballer, from Portugal

Who has more followers? Type 'A' or 'B':
```

Choose **A** or **B**. A correct guess earns a point and the winner stays for the next round. A wrong guess ends the game, but you can jump straight back in and try again.

---

## Features

* Simple, fast command‑line interface with clean ASCII art banners.
* Forty‑plus preloaded profiles spanning sports, music, film and global brands.
* Automatic score tracking and instant replay option.
* Pure Python implementation with no external dependencies.

---

## Prerequisites

* Python 3.8 or newer (only the standard library is used).

---

## Installation

```bash
# Clone the repository
git clone https://github.com/<your‑username>/<repo>.git
cd <repo>
```

Using a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

---

## Running the Game

```bash
python main.py
```

That is all you need. The game shuffles the dataset each time it starts so no two sessions are identical.

---

## Project Structure

```text
.
├── main.py        # Core game loop and logic
├── game_data.py   # List of profile dictionaries
└── art.py         # ASCII art logo and VS banner
```

---

## Customising the Dataset

Open `game_data.py` and append new dictionaries that contain:

```python
{
    "name": "New Profile",
    "follower_count": 123,
    "description": "What this person or brand is known for",
    "country": "Country"
}
```

Make sure **follower\_count** is an integer. Save the file and run `python main.py` to play with the updated set.

---

## Contributing

Pull requests are welcome. If you have ideas for new features or data improvements, please open an issue first so we can discuss them.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
