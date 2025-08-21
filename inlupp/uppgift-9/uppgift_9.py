# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string: str) -> bool:
    """
    Palindrom kontroll
    Ignorerar stora/små bokstäver och mellanslag.
    """
    # Gör allt till små bokstäver och ta bort mellanslag
    cleaned = string.replace(" ", "").lower()
    return cleaned == cleaned[::-1]