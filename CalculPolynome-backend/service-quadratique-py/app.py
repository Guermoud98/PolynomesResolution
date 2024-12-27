from flask import Flask, request, jsonify
from sympy import symbols, Eq, solve

app = Flask(__name__)

@app.route('/quadratique', methods=['POST'])
def resolve_quadratic():
    data = request.json
    try:
        # Extraire les coefficients
        a = data.get('a')
        b = data.get('b')
        c = data.get('c')

        if a is None or b is None or c is None:
            return jsonify({"error": "Les paramètres 'a', 'b' et 'c' sont requis.", "success": False}), 400

        if a == 0:
            return jsonify({"error": "Ce n'est pas une équation quadratique, car 'a' = 0.", "success": False}), 400

        # Définir la variable symbolique x
        x = symbols('x')

        # Construire et résoudre l'équation
        equation = Eq(a * x**2 + b * x + c, 0)
        solutions = solve(equation, x)

        return jsonify({
            "equation": f"{a}x^2 + {b}x + {c} = 0",
            "roots": [str(solution) for solution in solutions],
            "success": True
        })
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la résolution : {e}", "success": False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
