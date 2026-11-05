# ChoQ

Własny prototyp aplikacji społecznościowej opartej na wyborach A/B, rozwijany przy pomocy agentów AI.

## Pomysł

Użytkownik odpowiada na porównania i poznaje swoje preferencje. Projekt obejmuje głosowania, dyskusje i historię wyborów. Rozważany kierunek rozwoju profilu to humorystyczny portret wynikający z wielu odpowiedzi.

## Mój wkład

Określam funkcje, wymagania i kierunek rozwoju. Przykładowa decyzja dotyczy wspólnego głównego feedu i wykorzystania kategorii do porządkowania historii odpowiedzi w profilu. To zapisana decyzja kierunkowa; jej wpływ na użyteczność wymaga sprawdzenia z użytkownikami.

Agenci AI realizują implementację kolejnych wersji. Technologie projektu obejmują Flutter, Dart i Firebase. Nazwy technologii opisują prototyp i zakres współpracy z AI.

## Stan

Rozwijany lokalny prototyp z wersjami Android i środowiskiem emulatorów Firebase. 5 listopada 2026 uruchomiono wersję webową w trybie mock i sprawdzono poniższy scenariusz. Zrzuty przedstawiają dane demonstracyjne: użytkownicy, komentarze, liczby głosów i statystyki profilu nie są dowodem rzeczywistego ruchu. Sprawdzenie tej wersji nie obejmuje działania backendu Firebase ani zachowania aplikacji na Androidzie.

## Wybór i porównanie odpowiedzi

![Feed z porównaniem A/B](../materialy/choq/02-feed.png)

Główny ekran przedstawia pytanie oraz dwie ilustrowane odpowiedzi. W sprawdzonej wersji są także widoczne filtry kategorii; wspólny feed pozostaje decyzją kierunkową dla dalszego rozwoju.

![Wynik po wybraniu odpowiedzi A](../materialy/choq/03-wynik.png)

Po wybraniu Audi RS6 karta A została wyróżniona i pojawiły się demonstracyjne udziały odpowiedzi: 43% i 57%. To potwierdzenie działania interakcji w lokalnym prototypie.

## Dyskusja i powrót do wyborów

![Dyskusja z widoczną odpowiedzią na komentarz](../materialy/choq/04-dyskusja.png)

Panel dyskusji pokazuje komentarze, zagnieżdżoną odpowiedź, reakcje i opcje sortowania. Zrzut przedstawia istniejący wątek demonstracyjny; podczas tej próby nie sprawdzano publikacji nowego komentarza.

![Wybór zapisany w historii odpowiedzi](../materialy/choq/06-historia.png)

W historii pojawiła się odpowiedź oddana podczas próby. Ekran udostępnia wyszukiwanie i wybór kategorii. Profil i historia łączą pojedyncze decyzje z możliwością wrócenia do wcześniejszego pytania.

[Ekran powitalny](../materialy/choq/01-powitanie.png) · [Profil demonstracyjny](../materialy/choq/05-profil.png)

## Kolejne kierunki

Spójny, humorystyczny portret z wielu wyborów i rozwinięte porównywanie osób pozostają kierunkami produktu. Obecne ekrany i liczniki nie potwierdzają walidacji psychologicznej ani wdrożenia wszystkich planowanych funkcji.
