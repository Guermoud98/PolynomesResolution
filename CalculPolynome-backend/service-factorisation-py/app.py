from flask import Flask, request, jsonify
from factorisation_solver import advanced_factorization

# initialisation de l'application Flask
app = Flask(__name__)

@app.route('/factoriser', methods=['POST'])
def factorize_advanced():
    """
    Endpoint pour factoriser un polynôme.
    """
    try:
        # Lecture des données JSON envoyées par le client
        data = request.json
        equation = data.get('equation')
        variable = data.get('variable', 'x')  # Variable par défaut : 'x'

        if not equation:
            return jsonify({"success": False, "error": "L'équation est obligatoire."}), 400

        # Appel à la fonction de factorisation
        factorized_result = advanced_factorization(equation, variable)

        # Réponse au client
        return jsonify({
            "success": True,
            "original_equation": equation,
            "factorized_result": factorized_result
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
