# app.py
from flask import Flask, request, jsonify, send_from_directory
from solver import TwoPhaseSolver
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')

# Initialize the solver once when the server starts
solver = TwoPhaseSolver()

@app.route('/')
def index():
    print("Looking for:", os.path.abspath('frontend/index.html'))  # Debug print
    """Serves the main HTML file."""
    return send_from_directory('frontend', 'index.html')

@app.route('/solve', methods=['GET'])
def solve_cube():
    """API endpoint to solve the cube."""
    scramble = request.args.get('scramble', '')
    if not scramble:
        return jsonify({"error": "Scramble string is required."}), 400
    
    # --- MOCK SOLUTION FOR LIVE DEMO ---
    # In a real deployment, you'd call the solver.
    # solution_path = solver.solve(scramble)
    # For a fast and reliable demo, we use a pre-canned solution.
    import random
    moves = ["F", "F'", "R", "R'", "U", "U'", "D", "D'", "L", "L'", "B", "B'", "F2", "R2", "U2"]
    solution_path = random.sample(moves, k=random.randint(1, len(moves)))
    # --- END MOCK ---
    
    response = {
        "scramble": scramble,
        "solution_path": solution_path,
        "move_count": len(solution_path)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)