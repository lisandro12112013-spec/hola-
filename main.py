print("palabras posibles:")
print("cringe")
print("lol")
print("creepy")
print("cocinar")

for i in range(5):
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "CREEPY": "una cosa aterradora o siniestra",
                "LORE":  "contexto/historia de algo",
                "COCINAR": "hacer algo bueno"
                }
  
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
   
    if word in meme_dict.keys():
        print(meme_dict[word])
        # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("esa palabra no esta en la base de datos")
        # ¿Qué hacer si no se encuentra la palabra?
