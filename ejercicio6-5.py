def teams(candidates, k):
    # Caso base 1: Si k es 0, devuelve una lista con una cadena vacía (equipo vacío).
    if k == 0:
        return [""]
    # Caso base 2: Si no hay suficientes candidatos para formar un equipo de tamaño k, devuelve una lista vacía.
    if len(candidates) < k:
        return []

    # Recursión: 
    # 1. Incluir el primer candidato en el equipo y buscar combinaciones con el resto y tamaño k - 1.
    # 2. Excluir el primer candidato y buscar combinaciones del mismo tamaño en los candidatos restantes.
    with_first = [candidates[0] + team for team in teams(candidates[1:], k - 1)]
    without_first = teams(candidates[1:], k)

    return with_first + without_first

# Programa de prueba para llamar a la función teams()
print(teams("ABTZ", 2))  
print(teams("ABTZ", 3))  
print(teams("ABTZ", 1))  
print(teams("ABTZ", 4))  
print(teams("ABTZ", 0))  
print(teams("ABTZ", 5))  