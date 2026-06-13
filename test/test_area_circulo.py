import math as M
import pytest
from AreaCirculo import AreaCirculo


# Caso correcto
def test_area_correcta():
    resultado = AreaCirculo(5)
    assert resultado == M.pi * 25


# Caso límite
def test_area_cero():
    resultado = AreaCirculo(0)
    assert resultado == 0


# Caso de error
def test_radio_negativo():
    with pytest.raises(ValueError):
        AreaCirculo(-5)