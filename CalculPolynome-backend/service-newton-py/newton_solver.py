from sympy import symbols, diff, lambdify, sympify

def newton_method(equation, variable, initial_guess, tolerance=1e-7, max_iterations=100):
    try:
        # On remplace ^ par ** pour la compatibilité SymPy
        equation = equation.replace("^", "**")
        x = symbols(variable)  # Définir la variable symbolique
        equation = sympify(equation)  # Convertir l'équation en objet SymPy

        # Calcul de la dérivée
        derivative = diff(equation, x)

        # Conversion en fonctions évaluables
        f = lambdify(x, equation)  # Fonction f(x)
        f_prime = lambdify(x, derivative)  # Fonction f'(x)

        # Initialisation
        current_guess = initial_guess
        for iteration in range(max_iterations):
            # Calcul de la prochaine estimation
            f_value = f(current_guess)
            f_prime_value = f_prime(current_guess)

            if abs(f_prime_value) < 1e-12:  # Éviter la division par zéro
                raise ValueError("La dérivée est proche de zéro, Newton ne peut pas continuer.")

            next_guess = current_guess - f_value / f_prime_value

            # Vérification de la convergence
            if abs(next_guess - current_guess) < tolerance:
                return {
                    "solution": next_guess,
                    "iterations": iteration + 1,
                    "success": True
                }

            current_guess = next_guess

        raise ValueError("La méthode de Newton n'a pas convergé après le nombre maximum d'itérations.")
    except Exception as e:
        raise ValueError(f"Erreur lors de la résolution par Newton : {e}")
