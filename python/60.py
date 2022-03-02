"""
Eliminar elementos
"""

alumnos = {
            "Jorge": "4C",
            "Marco": "5B",
            "Polo": "3B",
            "Migue": "6A"
            }

nombres = alumnos.pop("Jorge", "No existe")
nom, clase = alumnos.popitem()

print(alumnos)
print(nombres)

print(nom, clase)
print(alumnos)