from flask import Flask, request, jsonify
from polynomial_solver import find_roots

app = Flask(__name__)

@app.route('/racines', methods=['POST'])
def calculate_roots():
    try:
        # On récupère les données JSON envoyées par l'utilisateur
        data = request.get_json()

        equation = data.get("equation", "")
        variable = data.get("variable", "x")

        # Vérification si l'équation est fournie
        if not equation:
            return jsonify({
                "error": "Aucune équation n'a été fournie.",
                "success": False
            }), 400

        # Calcul des racines
        result = find_roots(equation, variable)

        return jsonify(result)
    except Exception as e:
        return jsonify({
            "error": f"Erreur inattendue : {str(e)}",
            "success": False
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
