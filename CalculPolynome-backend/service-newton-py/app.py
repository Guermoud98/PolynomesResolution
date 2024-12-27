from flask import Flask, request, jsonify
from newton_solver import newton_method

app = Flask(__name__)

@app.route('/newton', methods=['POST'])
def solve_with_newton():
    try:
        # Récupérer les données JSON de la requête
        data = request.get_json()
        equation = data.get("equation")
        variable = data.get("variable", "x")
        initial_guess = data.get("initial_guess", 0)
        tolerance = data.get("tolerance", 1e-7)
        max_iterations = data.get("max_iterations", 100)

        if not equation or variable is None:
            return jsonify({
                "error": "L'équation et la variable sont obligatoires.",
                "success": False
            }), 400

        # Appeler la méthode de Newton
        result = newton_method(equation, variable, float(initial_guess), float(tolerance), int(max_iterations))

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
