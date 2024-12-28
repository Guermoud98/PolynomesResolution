from sympy import symbols, solve, simplify

def find_roots(equation, variable):
    try:
        # définition de la variable symbolique
        x = symbols(variable)

        # Simplification de l'équation si nécessaire
        simplified_eq = simplify(equation)

        # les racines
        roots = solve(simplified_eq, x)

        # Retourner les racines
        return {
            "roots": [str(root) for root in roots],
            "original_equation": equation,
            "success": True
        }
    except Exception as e:
        return {
            "error": f"Erreur lors du calcul des racines : {str(e)}",
            "success": False
        }
