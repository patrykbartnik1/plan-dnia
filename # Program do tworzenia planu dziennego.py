# tworzenie planu dziennego

# Słownik
daily_plan = {}

def add_event(hour, event):
    """Dodaje wydarzenie do planu na daną godzinę"""
    if 0 <= hour <= 23:
        daily_plan[hour] = event
        print(f"Wydarzenie '{event}' zostało dodane na godzinę {hour}:00.")
    else:
        print("Podaj godzinę w formacie 0-23.")



def view_plan():
    """Wyświetla pełen plan dnia"""
    if daily_plan:
        print("\nTwój plan na dziś:")
        for hour in range(24):  # wyświetla każdą godzinę, nawet jak jest pusta
            event = daily_plan.get(hour, "Brak wydarzenia")
            print(f"{hour:02d}:00 - {event}")
    else:
        print("Plan jest pusty. Dodaj wydarzenia, aby wyświetlić plan.")



def delete_event(hour):
    """Usuwa wydarzenie z planu na daną godzinę"""
    if hour in daily_plan:
        removed_event = daily_plan.pop(hour)
        print(f"Wydarzenie '{removed_event}' zostało usunięte z godziny {hour}:00.")
    else:
        print("Nie ma wydarzenia na tę godzinę.")



def main():
    """Główna funkcja obsługująca menu programu"""
    while True:
        print("\n--- Twój plan dzienny ---")
        print("1. Dodaj wydarzenie")
        print("2. Wyświetl plan")
        print("3. Usuń wydarzenie")
        print("4. Zakończ")


        choice = input("Wybierz opcję (1-4): ")
        

        if choice == '1':
            try:
                hour = int(input("Podaj godzinę (0-23): "))
                event = input("Podaj nazwę wydarzenia: ")
                add_event(hour, event)
            except ValueError:
                print("Proszę podać poprawną liczbę dla godziny.")
        elif choice == '2':
            view_plan()
        elif choice == '3':
            try:
                hour = int(input("Podaj godzinę wydarzenia do usunięcia (0-23): "))
                delete_event(hour)
            except ValueError:
                print("Proszę podać poprawną liczbę dla godziny.")
        elif choice == '4':
            print("Zakończono program.")
            break
        else:
            print("Niepoprawny wybór. Wybierz opcję 1, 2, 3 lub 4.")




if __name__ == "__main__":
    main()
