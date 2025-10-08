"""Module permettant de vérifier si une chaîne est un palindrome."""

import unicodedata


def ispalindrome(p):
    """Retourne True si la chaîne p est un palindrome, False sinon.

    La fonction :
    - met en minuscules la chaîne ;
    - supprime les accents ;
    - retire tous les caractères non alphanumériques ;
    - compare la chaîne nettoyée avec son inversion.
    """
    p = p.lower()
    p = ''.join(
        c for c in unicodedata.normalize('NFD', p)
        if unicodedata.category(c) != 'Mn'
    )
    p = ''.join(c for c in p if c.isalnum())
    return p == p[::-1]


def main():
    """Teste la fonction ispalindrome avec quelques exemples simples."""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
