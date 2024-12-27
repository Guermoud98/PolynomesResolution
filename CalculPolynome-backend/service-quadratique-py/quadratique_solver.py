from sympy import symbols, Eq, solve

def resolve_quadratic(a, b, c):
    """
    Résout une équation quadratique de la forme ax^2 + bx + c = 0.
    
    :param a: Coefficient de x^2
    :param b: Coefficient de x
    :param c: Terme constant
    :return: Les racines de l'équation quadratique
    """
    try:
        if a == 0:
            raise ValueError("Ce n'est pas une équation quadratique, car a = 0.")
        
        # Définir la variable symbolique x
        x = symbols('x')
        
        # Construire l'équation
        equation = Eq(a * x**2 + b * x + c, 0)
        
        # Résoudre l'équation
        solutions = solve(equation, x)
        
        return {
            "equation": f"{a}x^2 + {b}x + {c} = 0",
            "roots": [str(solution) for solution in solutions],
            "success": True
        }
    except Exception as e:
        return {
            "error": f"Erreur lors de la résolution : {e}",
            "success": False
        }

# Exemple d'utilisation
result = resolve_quadratic(1, -5, 6)  # Résout l'équation x^2 - 5x + 6 = 0
print(result)
