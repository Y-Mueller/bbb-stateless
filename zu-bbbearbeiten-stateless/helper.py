from dataclasses import dataclass
from datetime import datetime, timedelta, date

# Liste zur Speicherung der Items
items = []


@dataclass
class Item:
    text: str
    date: date
    isCompleted: bool = False


def oneWeekFromToday() -> date:
    today = datetime.now()
    one_week = timedelta(weeks=1)
    return (today + one_week).date()


def add(text: str, date_str: str = None):
    """
    Fügt ein neues Item zur Liste hinzu und sortiert die Liste nach Datum.
    """
    # Ersetze alle Vorkommen von 'b' und 'B'
    text = text.replace('b', 'bbb').replace('B', 'Bbb')

    # Datum parsen oder Standarddatum setzen
    if date_str is None:
        date_value = oneWeekFromToday()
    else:
        date_value = datetime.strptime(date_str, '%Y-%m-%d').date()

    # Neues Item erstellen
    new_item = Item(text, date_value)

    # Item zur Liste hinzufügen
    items.append(new_item)

    # Liste direkt nach Datum sortieren
    items.sort(key=lambda item: item.date)


def get_all():
    """Gibt alle Items zurück."""
    return items


def get(index: int):
    """Gibt ein Item an der angegebenen Indexposition zurück."""
    if 0 <= index < len(items):
        return items[index]
    else:
        raise IndexError("Ungültiger Index.")


def update(index: int):
    """Ändert den Status von isCompleted für das Item am angegebenen Index."""
    if 0 <= index < len(items):
        items[index].isCompleted = not items[index].isCompleted
    else:
        raise IndexError("Ungültiger Index.")