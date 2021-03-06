# Anleitung Aufgabe 1

Dies ist eine kleine Lerneinheit inkl. Selbstkontrolle. So gehst du vor:
**Installiere Pytest**
Installiere z.B. mit pip das Modul `pytest` durch die Eingabe von `pip install pytest`

**Bearbeite die Aufgaben**
Finde deinen Programmierfluss: alle Teilaufgaben auf einmal, oder nacheinander. Ganz wie du magst.

**Arbeite mit Eigenkontrolle**
Kontrolliere deine Egebnisse selbst durch ausführen deines Programms.

**Kontrolliere durch Testeinheiten**
Kontrolliere die Ergebnisse Mithilfe der vorliegenden Testeinheiten. ich empfehle dir die Akzeptanzkriterien einzeln zu prüfen. Solange der Test rot ist, ist dein Code nicht korrekt (oder der Test ist es nicht ;-) )

Kopiere dazu jeweils folgende Zeilen in dein Terminal:

_Kontrolle Aufgabe a:_
```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_a_1_division_a_durch_b_integer
```

```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_a_2_division_a_durch_b_floats
```

```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_a_3_division_a_durch_b_integer_und_float
```

_Kontrolle Aufgabe b:_
```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_b_1_runde_das_ergebnis_mathematisch_auf_4_stellen_ab
```

```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_b_2_runde_das_ergebnis_mathematisch_auf_4_stellen_auf
```

_Kontrolle Aufgabe c:_
```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_c_gib_none_zurueck_falls_a_oder_b_ein_string_ist
```

_Kontrolle Aufgabe d:_
```
pytest tests/test_aufgabe_1_division.py::TestDivision::test_d_gib_none_zurueck_falls_b_0_ist
```

_Kontrolle Total:_
```
pytest tests/test_aufgabe_1_division.py
```

_Funfact_: Das was du hier machst nennt sich Test Driven Development (TDD). In einigen Projekten ist es standart zuerst Kontrolleinheiten zu schreiben ehe man den Code schreibt. Ein Programm ans laufen zu kriegen bedeutet eben auch ein Programm am laufen zu halten ...

**Vergleiche Ergebnisse mit der Musterlösung**
Vergleiche deine Lösung mit der Musterlösung. Keine Sorge: Wenn deine Tests grün sind, hast du alles richtig gemacht. Die Lösung ist eben nur ein alternativer Weg genau wie es deine ist.
