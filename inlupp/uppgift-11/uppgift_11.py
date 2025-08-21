# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    """
    Tar emot en text (sträng) och returnerar antalet ord.

    """
    # Dela texten på mellanslag och räkna elementen
    words = text.split()
    return len(words)