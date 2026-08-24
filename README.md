# Options Greeks Lab

🚀 **[Live Demo](https://options-greeks-lab-eubayybf4jvymzqprve3nh.streamlit.app)**

A Python quantitative finance project implementing the Black-Scholes option pricing model, Greeks calculations, and options strategy analysis — with an interactive Streamlit dashboard.

## Overview

This project prices European options, computes their sensitivities (the "Greeks"), and analyzes multi-leg options strategies (straddle, bull call spread, strangle). It was built from scratch to deepen my understanding of derivatives pricing ahead of a career in market finance.

## Features

- Black-Scholes pricing for European calls and puts
- All 5 Greeks: Delta, Gamma, Vega, Theta, Rho (calls and puts)
- Options strategies: Straddle, Bull Call Spread, Strangle — with cost, payoff, and PnL calculations
- Automated test suite (pytest) validating pricing formulas via put-call parity and known Greek properties
- Interactive dashboard (Streamlit + Plotly) to visualize strategy payoffs and Greeks in real time

## Project structure

Options-Greeks-Lab/
- black_scholes.py — Core pricing engine: d1, d2, call/put prices, Greeks
- strategies.py — Multi-leg strategies: straddle, bull call spread, strangle
- dashboard.py — Interactive Streamlit dashboard
- tests/test_black_scholes.py — pytest suite
- requirements.txt
- README.md

## The math

### Black-Scholes formula

C = S0 * N(d1) - K * e^(-rT) * N(d2)

P = K * e^(-rT) * N(-d2) - S0 * N(-d1)

where:

d1 = [ln(S0/K) + (r + sigma^2/2) * T] / (sigma * sqrt(T))

d2 = d1 - sigma * sqrt(T)

Key assumptions: constant volatility and risk-free rate, no dividends, European exercise, no arbitrage, frictionless markets, log-normal price distribution.

### Greeks

| Greek | Measures | Call | Put |
|---|---|---|---|
| Delta | Sensitivity to S | N(d1) | N(d1) - 1 |
| Gamma | Rate of change of Delta | N'(d1) / (S * sigma * sqrt(T)) | same as call |
| Vega | Sensitivity to sigma | S * N'(d1) * sqrt(T) | same as call |
| Theta | Time decay | negative (generally) | negative (generally) |
| Rho | Sensitivity to r | positive | negative |

### Strategies

- Straddle: buy call + put, same strike — bets on a large move in either direction
- Bull Call Spread: buy call K1, sell call K2 (K1<K2) — bets on a moderate rise, capped gain/loss, lower cost
- Strangle: buy OTM call + OTM put, different strikes — cheaper alternative to the straddle, wider breakeven range

## Running the project

Install dependencies: pip3 install -r requirements.txt

Run the tests: pytest

Launch the dashboard: streamlit run dashboard.py

## Tech stack

Python, NumPy, SciPy, pandas, Plotly, Streamlit, pytest

## What I learned

Building this project deepened my understanding of:
- Why option prices depend on volatility, not just direction (asymmetric payoff)
- The economic intuition behind each Greek (hedge ratios, time decay acceleration, rate sensitivity)
- Why gamma and vega are identical for calls and puts (via put-call parity)
- Trade-offs in strategy design: cost vs. probability of profit (straddle vs. strangle)

## Next steps

- Add more strategies (butterfly, iron condor)
- Extend to American options / dividend-paying stocks
- Add implied volatility calibration from market data