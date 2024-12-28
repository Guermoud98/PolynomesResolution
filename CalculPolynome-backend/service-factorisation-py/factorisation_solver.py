from sympy import symbols, factor, simplify
from sympy.core.sympify import SympifyError
from flask import jsonify
from models import SessionLocal, Polynomial

def advanced_factorization(equation, variable):
    try:
        # définition de la variable symbolique
        x = symbols(variable)

        # factorisation de l'équation avec SymPy
        factored = str(factor(equation))

        # conversion de  `**` en `^` pour l'affichage ou le stockage
        factored_with_caret = factored.replace('**', '^')

        # Enregistrement dans la base de données
        session = SessionLocal()
        try:
            polynomial = Polynomial(
                equation=equation.replace('**', '^'),  # Stocke également l'équation avec `^`
                factorized_result=factored_with_caret
            )
            session.add(polynomial)
            session.commit()
        except Exception as e:
            session.rollback()
            raise ValueError(f"Erreur lors de l'enregistrement dans la base de données : {e}")
        finally:
            session.close()

        return factored_with_caret
    except SympifyError:
        return jsonify({"error": "L'équation fournie est invalide."}), 400
    except Exception as e:
        raise ValueError(f"Erreur lors de la factorisation : {e}")
