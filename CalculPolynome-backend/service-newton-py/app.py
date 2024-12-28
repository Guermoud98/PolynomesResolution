from flask import Flask, request, jsonify
from newton_solver import newton_method
from models import SessionLocal, NewtonResult

# Initialisation de l'application Flask
app = Flask(__name__)

@app.route('/newton', methods=['POST'])
def solve_with_newton():
    try:
        # Lecture des données envoyées par le client (format JSON)
        data = request.get_json()
        equation = data.get("equation")  # Récupération de l'équation
        variable = data.get("variable", "x")  # Nom de la variable (par défaut : 'x')
        initial_guess = data.get("initial_guess", 0)  # Estimation initiale
        tolerance = data.get("tolerance", 1e-7)  # Tolérance pour la convergence
        max_iterations = data.get("max_iterations", 100)  # Nombre maximum d'itérations

        # Vérification des données obligatoires
        if not equation or variable is None:
            return jsonify({
                "error": "L'équation et la variable sont obligatoires.",
                "success": False
            }), 400

        # Appel de la méthode de Newton
        result = newton_method(equation, variable, float(initial_guess), float(tolerance), int(max_iterations))

        # Enregistrement du résultat dans la base de données
        session = SessionLocal()
        try:
            newton_result = NewtonResult(
                equation=equation,
                solution=result["solution"],
                iterations=result["iterations"],
                success="True" if result["success"] else "False"
            )
            session.add(newton_result)  # Ajout du résultat à la session
            session.commit()  # Validation de la transaction
        finally:
            session.close()

        # Retourner le résultat au client
        return jsonify(result), 200

    except Exception as e:
        # En cas d'erreur, retourner une réponse avec un message d'erreur
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Lancement de l'application
