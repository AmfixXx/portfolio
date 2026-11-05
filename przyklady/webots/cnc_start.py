from controller import Robot  # Udostępnia połączenie programu z urządzeniem w Webots.

cnc = Robot()  # Łączy program z urządzeniem, do którego przypiszemy ten kontroler.
time_step = int(cnc.getBasicTimeStep())  # Pobiera długość jednego kroku symulacji w milisekundach.
czujnik = cnc.getDevice("czujnik_drzwi")  # Znajduje czujnik po nazwie nadanej mu w świecie Webots.
czujnik.enable(time_step)  # Włącza pomiary aktualizowane co jeden krok symulacji.
naped = cnc.getDevice("naped_drzwi")  # Znajduje napęd po nazwie wpisanej w polu name w Webots.
naped.setVelocity(0.1)  # Ustawia prędkość ruchu na maksymalnie 0,1 m/s, czyli 10 cm/s.
cel_drzwi = 0.20  # Zapisuje docelowe przesunięcie drzwi w metrach.
naped.setPosition(cel_drzwi)  # Przekazuje napędowi pozycję zapisaną w zmiennej.


oczekiwanie_zakonczone = False
limit_czasu = 1
poczatek = cnc.getTime()



while cnc.step(time_step) != -1:  # Wykonuje kolejne kroki symulacji, dopóki kontroler może pracować.
    polozenie = czujnik.getValue()  # Odczytuje aktualne przesunięcie drzwi w metrach.
    blad = abs(cel_drzwi - polozenie)  # Oblicza odległość od celu, zawsze jako liczbę nieujemną.
    
    uplynelo = cnc.getTime() - poczatek
    if oczekiwanie_zakonczone == False:
        if uplynelo >= limit_czasu:
            oczekiwanie_zakonczone = True
            print("Błąd: Oczekiwanie Zakonczone")
            
        elif blad <= 0.001: # Sprawdza, czy do celu brakuje najwyżej 1 mm.
            oczekiwanie_zakonczone = True
            print("Drzwi osiągnęły zadaną pozycję.")  # Informuje o osiągnięciu celu.
            
        else: 
        
            print(f"Trwa ruch. Położenie: {polozenie:.3f} m")  # Pokazuje aktualny pomiar podczas dojazdu.