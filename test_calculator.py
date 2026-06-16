from calculator import sumar, restar, Dividir, Multiplicar
import pytest

def test_sumar():
    assert sumar(5, 5) == 10

def test_restar():
    assert restar(10, 5) == 5

def test_dividir():
    assert Dividir(10, 2) == 5

def test_dividir_cero():
    with pytest.raises(ZeroDivisionError):
        Dividir(10, 0)

def test_multiplicar():
    assert Multiplicar(5, 5) == 25