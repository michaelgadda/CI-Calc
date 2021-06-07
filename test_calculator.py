import calculator


class TestCAlculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiply(self):
        assert 10 == calculator.multiply(2, 5)

    def test_divide(self):
        assert 5 == calculator.divide(10, 2)
