rex=3
bob=6
oli=5
def teste (rex, bob, oli):
    if rex < oli and bob >= oli:
        return "bob"
    elif bob < oli and rex >= oli:
        return "Rex"
    elif bob == rex and rex >= oli:
        return "Oli"
    else:
        return "Oli"
resultado= teste(rex, bob, oli)
print(resultado)