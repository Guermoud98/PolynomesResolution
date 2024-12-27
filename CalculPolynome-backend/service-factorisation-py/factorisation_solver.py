from sympy import symbols, factor, simplify

def advanced_factorization(equation, variable):
    try:
        # la variable symbolique
        x = symbols(variable)

        # la factorisation de l'equation
        expression = simplify(equation)  # Simplification de l'equation si nécessaire
        factorized_expression = factor(expression)

        return str(factorized_expression)
    except Exception as e:
        raise ValueError(f"Erreur lors de la factorisation : {e}")
