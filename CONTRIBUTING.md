# Zasady współpracy
Aby współpraca przebiegała płynnie prosimy o stosowanie się do poniższych zasad.

##Przygotowanie projektu
1. **Sforkuj (Fork) repozytorium** na swoje konto GitHub.
2. **Sklonuj** swój fork lokalnie na komputer:
  ```bash
   git clone [https://github.com/oskarjusta/Zaj-cia-Narz-dzia-wspieraj-ce-wytwarzanie-oprogramowania
.git](https://github.com/oskarjusta/Zaj-cia-Narz-dzia-wspieraj-ce-wytwarzanie-oprogramowania
.git)
```
3.Utwórz wirtualne środowisko
```bash
python -n venv .venv
```

4. Aktywuj środowisko i zainstaluj zależności
```bash
.venv\Scripts\Active.psl


##Praca z gałęziami
-**Nigdy nie wprowadzaj** zmian bezpośrednio do gałęzi main
-Twórz osobne gałęzi dla każdego zadania, błędu lub funkcji, stosując czytelny prefiks:
-feature/nazwa-funkcji – dla nowych funkcjonalności
-bugfix/opis-bledu – dla naprawy błędów
-docs/opis-zmian – dla aktualizacji dokumentacji
-Przed rozpoczęciem pracy na nowej gałęzi upewnij się, że Twój lokalny main jest zaktualizowany:

##Zasady pisania kodu
-Trzymaj się przyjętych w projekcie konwencji
-Pisz kod czytelny modularny i zrozumiały
-Dodawaj komentarze tam gdzie wymagane są wyjaśnienia
-Nie powielaj kodu (Zasada DRY)
-Nie pisz kodu na zapas (Zasada YAGNI)
-Jeśli dodajesz nową funkcję lub naprawiasz błąd, postaraj się dopisać odpowiednie testy jednostkowe lub upewnij się, że istniejące testy przechodzą pomyślnie.

##Commity
Każdy commit powinien zawierać krótki i zrozumiały opus zmian w trybie rozkazującym np:
+feat: – dodanie nowej funkcjonalności
+fix: – naprawa błędu
+docs: – zmiany w dokumentacji (np. w README)
+style: – formatowanie kodu, brak zmian w logice (spacje, średniki itp.)
+refactor: – przebudowa kodu bez zmieniania jego działania
+test: – dodanie lub poprawienie testów

##Zgłoszenia (issuses)


##Pull requests


##Komunikacja w zespole
-Kultura wypowiedzi: Szanujemy się nawzajem. W dyskusjach w komentarzach pod kodem lub zgłoszeniami zachowujemy profesjonalizm i życzliwość.
-Gdzie rozmawiamy: Głównym miejscem komunikacji zespołu jest [np. nasz kanał na Discordzie / Slack / sekcja Discussions na GitHubie].
-Blokady (Blockers): JeśliUtkniesz nad jakimś problemem na dłużej, nie bój się pytać o pomoc – od tego jest zespół!
-Korzystaj z Issue i Pull Request do dyskusji dotyczących projektu

#Dziękujemy za współprace i wkład w rozwój projektu
