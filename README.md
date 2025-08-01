# 🚀 Interactive 3D Cube Solver

### An advanced Rubik's Cube solver built for the **AeroHack'25** hackathon, featuring a Two-Phase algorithm and an interactive 3D web interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0-lightgrey.svg)

---

## Key Features

* **High-Speed Solving**: Implements Kociemba's Two-Phase algorithm to find solutions in under 20 moves, almost instantly.
* **Interactive 3D UI**: A fully interactive 3D cube built with pure HTML, CSS, and JavaScript that allows you to scramble and watch the solution animate.
* **Full-Stack Application**: Built with a Python/Flask backend that serves the application and provides a solver API.
* **Efficient Data Structures**: The solver logic is designed to use pre-computed Pruning Tables for an incredibly fast and efficient search.

---

## ⚙️ How It Works

This project uses an advanced two-phase algorithm to solve the cube, which is far more efficient than a standard search.

1.  **Phase 1: Solve Orientation**: The algorithm first finds a short sequence of moves to get all corner and edge pieces correctly oriented. It uses a pre-computed **Pruning Table** to know the minimum number of moves required to solve this sub-problem from any state.

2.  **Phase 2: Solve Permutation**: Once the pieces are oriented, the algorithm uses a different set of moves and pruning tables to move the pieces to their final solved positions.

This approach dramatically cuts down the search time, allowing it to find a solution almost instantly.

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML5, CSS3 (3D Transforms), JavaScript (Vanilla)

---

## Local Setup and Running

To run this project locally, please follow these steps:

### 1. Prerequisites
* Python 3.x
* pip

### 2. Installation
Clone the repository and navigate to the project directory:
```bash
git clone [your-repo-link]
cd kociemba_solver
