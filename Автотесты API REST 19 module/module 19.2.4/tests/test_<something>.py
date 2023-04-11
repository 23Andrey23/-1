import pytest

from app.calculator import Calculator

class TestCalc:

    def setup(self):
        """Инициализируем приложение калькулятор"""
        self.calc = Calculator

    def test_adding_addition(self):
        """Проверяем возможеость сложения"""
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_multiply(self):
        """Проверяем возможеость умножения"""
        assert self.calc.multiply(self, 1, 7) == 7

    def test_adding_subtraction(self):
        """Проверяем возможеость вычитания"""
        assert self.calc.subtraction(self, 7, 5) == 2

    def test_adding_division(self):
        """Проверяем возможеость деление"""
        assert self.calc.division(self, 2, 2) == 1

    def teardown(self):
        print('Выполняется метод teardown')
