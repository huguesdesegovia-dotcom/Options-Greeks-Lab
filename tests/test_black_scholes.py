import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from black_scholes import black_scholes_call, black_scholes_put, delta_call, delta_put, gamma, vega
import numpy as np


def test_put_call_parity():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20

    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)

    left_side = call - put
    right_side = S - K * np.exp(-r * T)

    assert abs(left_side - right_side) < 1e-10

def test_delta_bounds():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20

    dc = delta_call(S, K, T, r, sigma)
    dp = delta_put(S, K, T, r, sigma)

    assert 0 <= dc <= 1
    assert -1 <= dp <= 0


def test_delta_put_call_relationship():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20

    dc = delta_call(S, K, T, r, sigma)
    dp = delta_put(S, K, T, r, sigma)

    assert abs(dp - (dc - 1)) < 1e-10


def test_gamma_always_positive():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20

    g = gamma(S, K, T, r, sigma)

    assert g > 0


def test_gamma_max_at_the_money():
    T, r, sigma = 1, 0.05, 0.20

    gamma_atm = gamma(100, 100, T, r, sigma)   # at-the-money: S = K
    gamma_otm = gamma(150, 100, T, r, sigma)   # deep in-the-money

    assert gamma_atm > gamma_otm