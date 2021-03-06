from aufgaben.aufgabe_1 import division
# from loesungen.loesung_1 import division


class TestDivision:
    def test_a_1_division_a_durch_b_integer(self):
        assert division(9, 3) == 9 / 3
        assert division(9, 4) == 9 / 4

    def test_a_2_division_a_durch_b_floats(self):
        assert division(0.5, 2.5) == 1 / 5

    def test_a_3_division_a_durch_b_integer_und_float(self):
        assert division(8, 0.5) == 16
        assert division(2.5, 2) == 5 / 4

    def test_b_1_runde_das_ergebnis_mathematisch_auf_4_stellen_ab(self):
        assert division(1, 3) == 0.3333

    def test_b_2_runde_das_ergebnis_mathematisch_auf_4_stellen_auf(self):
        assert division(2, 3) == 0.6667

    def test_c_gib_none_zurueck_falls_a_oder_b_ein_string_ist(self):
        assert division("string", 2) is None
        assert division(2, "string") is None

    def test_d_gib_none_zurueck_falls_b_0_ist(self):
        assert division(99, 0) is None
