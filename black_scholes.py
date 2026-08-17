import numpy as np
from scipy.stats import norm


def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def black_scholes_call(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(D1) - K * np.exp(-r * T) * norm.cdf(D2)


def black_scholes_put(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    return K * np.exp(-r * T) * norm.cdf(-D2) - S * norm.cdf(-D1)


if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.50

    print("d1 =", d1(S, K, T, r, sigma))
    print("d2 =", d2(S, K, T, r, sigma))
    print("Call price =", black_scholes_call(S, K, T, r, sigma))
    print("Put price =", black_scholes_put(S, K, T, r, sigma))