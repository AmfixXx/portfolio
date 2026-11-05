# Próbka kodu z nauki Webots

Plik `cnc_start.py` jest kopią kontrolera z projektu edukacyjnego, zachowaną w jego aktualnej postaci. Powstawał w ramach nauki ze wsparciem dydaktycznym AI. Komentarze i objaśnienia to część tego procesu.

## Wymagane otoczenie

Kod korzysta z modułu `controller` udostępnianego przez Webots. W świecie symulacji potrzebuje robota z napędem liniowym `naped_drzwi` oraz czujnikiem pozycji `czujnik_drzwi`. Kontroler uruchamia się wewnątrz Webots. Próbka pokazuje logikę; pełny plik świata pozostaje w lokalnym projekcie edukacyjnym.

## Co robi

Zadaje pozycję 0,20 m i prędkość 0,1 m/s. W każdym kroku odczytuje pozycję oraz czas. Sprawdza najpierw limit czasu, następnie tolerancję położenia 0,001 m. Flaga ogranicza komunikat końcowy do jednego wystąpienia, a pętla symulacji nadal działa.

W zapisanej wersji limit wynosi 1 sekundę, co służy ćwiczeniu przekroczenia czasu. Podczas nauki sprawdzano również limit 5 sekund i potwierdzenie osiągnięcia celu. Przekroczenie czasu kończy ocenę wyniku; napęd nadal realizuje wcześniej zadane polecenie.

## Weryfikacja

Przed publikacją 5 listopada 2026 sprawdzono składnię przez parser Pythona i odczytano kod. Wyniki prób symulacji pochodzą z wcześniejszego potwierdzenia autora podczas nauki. Kolejny etap to zapis odrębnego wyniku sukcesu lub błędu i komunikacja z ramieniem.
