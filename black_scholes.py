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


def delta_call(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))


def delta_put(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma)) - 1


def gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * np.sqrt(T))


def vega(S, K, T, r, sigma):
    return S * norm.pdf(d1(S, K, T, r, sigma)) * np.sqrt(T)


def theta_call(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    term1 = -(S * norm.pdf(D1) * sigma) / (2 * np.sqrt(T))
    term2 = -r * K * np.exp(-r * T) * norm.cdf(D2)
    return term1 + term2


def theta_put(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    term1 = -(S * norm.pdf(D1) * sigma) / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T) * norm.cdf(-D2)
    return term1 + term2


def rho_call(S, K, T, r, sigma):
    D2 = d2(S, K, T, r, sigma)
    return K * T * np.exp(-r * T) * norm.cdf(D2)


def rho_put(S, K, T, r, sigma):
    D2 = d2(S, K, T, r, sigma)
    return -K * T * np.exp(-r * T) * norm.cdf(-D2)

if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20

    print("d1 =", d1(S, K, T, r, sigma))
    print("d2 =", d2(S, K, T, r, sigma))
    print("Call price =", black_scholes_call(S, K, T, r, sigma))
    print("Put price =", black_scholes_put(S, K, T, r, sigma))
    print("Delta call =", delta_call(S, K, T, r, sigma))
    print("Delta put =", delta_put(S, K, T, r, sigma))
    print("Gamma =", gamma(S, K, T, r, sigma))
    print("Vega =", vega(S, K, T, r, sigma))
    print("Theta call =", theta_call(S, K, T, r, sigma))
    print("Theta put =", theta_put(S, K, T, r, sigma))
    print("Rho call =", rho_call(S, K, T, r, sigma))
    print("Rho put =", rho_put(S, K, T, r, sigma))


