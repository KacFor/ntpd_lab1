# NOWOCZESNE TECHNOLOGIE PRZETWARZANIA DANYCH

Cel ćwiczenia:  
Celem ćwiczenia jest stworzenie prostego modelu uczenia maszynowego w Pythonie (skorzystanie z biblioteki scikit-learn lub TensorFlow); Zapisywanie i wersjonowanie modelu (pickle, joblib); Omówienie różnic między środowiskiem deweloperskim a produkcyjnym.

---

Wersję modelu należy podnosić przy zmianie hiperparametrów - np. inny split, większa/mniejsza ilość iteracji, itp. lub przy zmianie datasetu, na którym trenowany był model, lub przy wprowadzeniu dowolnej zmiany w kodzie, która bezpośrednio będzie wpływać na działanie i skuteczność modelu.  

model_v1 - pierwsza wersja modelu split 80%/20%, 1000 iteracji  
informacje o modelu:  
Accuracy: 0.9722222222222222  
Precision: 0.9777777777777779  
Recall: 0.9761904761904763  
Wytrenowany na datasecie load_wine z biblioteki scikit-learn  

model_v2 - druga wersja modelu ... (w przyszłości)  

---

# Różnice między środowiskiem deweloperskim a produkcyjnym przy wdrażaniu modelu ML

| Środowisko deweloperskie | Środowisko produkcyjne | Przykład naprawy |
|---|---|---|
| Biblioteki instalowane lokalnie | Biblioteki muszą być identycznie odtworzone | zawarcie bibliotek w plikach `requirements.txt` lub w Dockerze |
| Trening modelu odbywa się raz na lokalnym zbiorze danych | Model jest trenowany regularnie na nowych/dodatkowych danych | dodanie pipeline i automatycznego retrainingu |
| Model zapisywany lokalnie | Model wersjonowany w systemie | Wersjonowanie modelu w GitHubie i tagowanie plików z modelem |
| Metryki sprawdzane na zbiorze testowym | Jakość modelu musi być sprawdzana w sposób ciągły | dodanie automatycznych tekstów i walidacji metryk |
| Brak potrzeby monitorowania danych po wytrenowaniu | Konieczność monitorowania jakości i zmian danych | monitorowanie metryk i wykrywanie problemów z danymi |
| Predykcja jest sprawdzana w oddzielnym skrypcie | Model działa przy użyciu np. API | Flask / dodanie lokalnego serwera |
| Skrypty są uruchamiane ręcznie | Skrypty są uruchamiane automatycznie | Dodanie CI/CD |
