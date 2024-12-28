from flask import Flask, request, jsonify
from quadratique_solver import resolution_quadratique

app = Flask(__name__)

@app.route('/quadratique', methods=['POST'])
def resolve_quadratic():
    try:
        # Lecture des données envoyées dans la requête
        data = request.json
        a = data.get('a')
        b = data.get('b')
        c = data.get('c')

        if a is None or b is None or c is None:
            return jsonify({
                "error": "Les paramètres 'a', 'b' et 'c' sont requis.",
                "success": False
            }), 400

        # Appel à la fonction de résolution
        result = resolution_quadratique(float(a), float(b), float(c))
        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": f"Erreur lors de la résolution : {e}",
            "success": False
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
