# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string: str) -> dict[str, int]:
    """

    """
    counts = {}
    for ch in string:
        if ch.isalpha():  # vi räknar bara bokstäver
            counts[ch] = counts.get(ch, 0) + 1
    return counts