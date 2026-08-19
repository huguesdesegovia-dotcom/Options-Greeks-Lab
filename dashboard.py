import streamlit as st
import numpy as np
import plotly.graph_objects as go

from strategies import (
    straddle_cost, straddle_pnl,
    bull_call_spread_cost, bull_call_spread_pnl,
    strangle_cost, strangle_pnl,
)

st.title("Options Greeks Lab — Strategy Visualizer")

strategy = st.selectbox(
    "Choose a strategy",
    ["Straddle", "Bull Call Spread", "Strangle"]
)

S = st.slider("Current stock price (S)", 50, 150, 100)
T = st.slider("Time to expiry (years)", 0.1, 2.0, 1.0)
r = st.slider("Risk-free rate", 0.0, 0.10, 0.05)
sigma = st.slider("Volatility", 0.05, 1.0, 0.20)

if strategy == "Straddle":
    K = st.slider("Strike (K)", 50, 150, 100)
    cost = straddle_cost(S, K, T, r, sigma)
    S_range = np.linspace(K - 50, K + 50, 200)
    pnl_values = [straddle_pnl(s, K, S, T, r, sigma) for s in S_range]

elif strategy == "Bull Call Spread":
    K1 = st.slider("Lower strike (K1)", 50, 150, 100)
    K2 = st.slider("Upper strike (K2)", 50, 150, 110)
    cost = bull_call_spread_cost(S, K1, K2, T, r, sigma)
    S_range = np.linspace(K1 - 50, K2 + 50, 200)
    pnl_values = [bull_call_spread_pnl(s, K1, K2, S, T, r, sigma) for s in S_range]

else:  # Strangle
    K1 = st.slider("Put strike (K1)", 50, 150, 90)
    K2 = st.slider("Call strike (K2)", 50, 150, 110)
    cost = strangle_cost(S, K1, K2, T, r, sigma)
    S_range = np.linspace(K1 - 50, K2 + 50, 200)
    pnl_values = [strangle_pnl(s, K1, K2, S, T, r, sigma) for s in S_range]

st.write(f"**{strategy} cost:** {cost:.2f}€")

fig = go.Figure()
fig.add_trace(go.Scatter(x=S_range, y=pnl_values, mode='lines', name='PnL'))
fig.add_hline(y=0, line_dash="dash", line_color="gray")
fig.update_layout(
    xaxis_title="Stock price at expiry",
    yaxis_title="Profit / Loss (€)",
)

st.plotly_chart(fig)