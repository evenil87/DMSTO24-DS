# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list[tuple[str, int]]) -> dict[str, int]:
    """
    Tar emot en lista och returnerar
    en dictionary där namnet är nyckeln och åldern är värdet.

    """
    return {name: age for name, age in students}