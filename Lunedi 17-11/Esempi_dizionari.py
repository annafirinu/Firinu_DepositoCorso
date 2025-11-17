studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}

print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20

studente["età"] = 21
print(studente)
# Output: {'nome': 'Alice', 'età': 21, 'sesso':'Femmina'}

print(studente.keys()) # Output: dict_keys(['nome', 'età', 'sesso'])
print(studente.values()) # Output: dict_values(['Alice', 20, 'Femmina'])
print(studente.items()) # Output: dict_items([('nome', 'Alice'), ('età', 21), ('sesso', 'Femmina')])
print(studente.get("nome")) #Output: Alice

