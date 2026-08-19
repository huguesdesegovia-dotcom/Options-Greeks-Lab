from black_scholes import black_scholes_call, black_scholes_put


def straddle_cost(S, K, T, r, sigma):
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    return call + put


def straddle_payoff(S_at_expiry, K):
    return abs(S_at_expiry - K)


def straddle_pnl(S_at_expiry, K, S, T, r, sigma):
    cost = straddle_cost(S, K, T, r, sigma)
    payoff = straddle_payoff(S_at_expiry, K)
    return payoff - cost


def bull_call_spread_cost(S, K1, K2, T, r, sigma):
    long_call = black_scholes_call(S, K1, T, r, sigma)
    short_call = black_scholes_call(S, K2, T, r, sigma)
    return long_call - short_call


def bull_call_spread_payoff(S_at_expiry, K1, K2):
    long_payoff = max(S_at_expiry - K1, 0)
    short_payoff = max(S_at_expiry - K2, 0)
    return long_payoff - short_payoff


def bull_call_spread_pnl(S_at_expiry, K1, K2, S, T, r, sigma):
    cost = bull_call_spread_cost(S, K1, K2, T, r, sigma)
    payoff = bull_call_spread_payoff(S_at_expiry, K1, K2)
    return payoff - cost


if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20

    cost = straddle_cost(S, K, T, r, sigma)
    print("Straddle cost =", cost)

    for S_at_expiry in [70, 85, 100, 115, 130]:
        payoff = straddle_payoff(S_at_expiry, K)
        pnl = straddle_pnl(S_at_expiry, K, S, T, r, sigma)
        print(f"S_expiry={S_at_expiry} | payoff={payoff:.2f} | PnL={pnl:.2f}")

    K1 = 100
    K2 = 110
    spread_cost = bull_call_spread_cost(S, K1, K2, T, r, sigma)
    print("\nBull Call Spread cost =", spread_cost)

    for S_at_expiry in [80, 100, 105, 110, 130]:
        payoff = bull_call_spread_payoff(S_at_expiry, K1, K2)
        pnl = bull_call_spread_pnl(S_at_expiry, K1, K2, S, T, r, sigma)
        print(f"S_expiry={S_at_expiry} | payoff={payoff:.2f} | PnL={pnl:.2f}")