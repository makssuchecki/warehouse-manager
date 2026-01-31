Maksymilian Suchecki
Grupa 2

Założeniem aplikacji jest wsparcie w zarządzaniu produktami oraz operacjami magazynowymi sklepu muzycznego.

Aplikacja umożliwia:

- tworzenie produktów
- usuwanie produktów (operacja dostępna wyłącznie dla użytkowników z rolą admin)
- pobieranie listy produktów oraz pojedynczych zasobów
- przyjmowanie towaru
- wydawanie towaru
- kontrole poprawności operacji zgodnie z logiką biznesową (np. brak możliwości wydania towaru ponad dostępny stan)
- tworzenie użytkowników
- prowadzenie historii operacji wykonanych na produkcie
- zapisywanie oraz wczytywanie aktualnego stanu produktów (do bazy mongo, funkcjonalność testowana z wykorzystaniem mockowania)

Aplikacja zawiera komplenty zestaw testów automatycznych:

- testy jednostkowe
- testy api
- testy bdd 
- testy wydajnościowe

Do wykonania testów potrzbne jest odpalenie flask i docker:

py -m flask --app app/api.py --debug run

docker compose -f mongo.yml up

Testy jednostkowe, API i wydajnościowe (pytest)

py -m pytest

py -m coverage run --source=src -m pytest tests/unit

py -m coverage report --fail-under=100

Testy BDD

py -m behave 

Test wydajnościowy (locust)

py -m locust -f ./tests/performance/locustfile.py --headless --run-time 10s -u 20 -r 5

