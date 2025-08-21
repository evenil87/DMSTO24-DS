# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password: str) -> bool:
    """
    Kontrollerar att lösenordet är minst 8 tecken långt
    och innehåller minst en siffra.

    Returnerar True om kraven uppfylls, annars False.
    """
    # Kolla längd och om någon tecken är en siffra
    return len(password) >= 8 and any(ch.isdigit() for ch in password)