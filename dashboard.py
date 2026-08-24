import streamlit as st
import numpy as np
import plotly.graph_objects as go

from strategies import (
    straddle_cost, straddle_pnl,
    bull_call_spread_cost, bull_call_spread_pnl,
    strangle_cost, strangle_pnl,
)
from black_scholes import delta_call, gamma, vega

st.set_page_config(page_title="Options Greeks Lab", page_icon="📈", layout="wide")

st.title("📈 Options Greeks Lab — Strategy Visualizer")
st.markdown("Interactive pricing, Greeks and strategy payoff explorer built with Black-Scholes.")

st.divider()

col_controls, col_chart = st.columns([1, 2])

with col_controls:
    strategy = st.selectbox("Choose a strategy", ["Straddle", "Bull Call Spread", "Strangle"])

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

    else:
        K1 = st.slider("Put strike (K1)", 50, 150, 90)
        K2 = st.slider("Call strike (K2)", 50, 150, 110)
        cost = strangle_cost(S, K1, K2, T, r, sigma)
        S_range = np.linspace(K1 - 50, K2 + 50, 200)
        pnl_values = [strangle_pnl(s, K1, K2, S, T, r, sigma) for s in S_range]

    st.metric(label=f"{strategy} cost", value=f"{cost:.2f} €")

with col_chart:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=S_range, y=pnl_values, mode='lines', name='PnL',
        line=dict(color="#4DA3FF", width=3),
        fill='tozeroy', fillcolor="rgba(77, 163, 255, 0.15)"
    ))
    fig.add_hline(y=0, line_dash="dash", line_color="#8FA3BF")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0B1F3A",
        plot_bgcolor="#0B1F3A",
        xaxis_title="Stock price at expiry",
        yaxis_title="Profit / Loss (€)",
        title=f"{strategy} — Payoff at expiry",
        height=450,
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.header("📊 Greeks visualization")

K_greeks = st.slider("Strike for Greeks (K)", 50, 150, 100, key="K_greeks")

S_range_greeks = np.linspace(50, 150, 200)
delta_values = [delta_call(s, K_greeks, T, r, sigma) for s in S_range_greeks]
gamma_values = [gamma(s, K_greeks, T, r, sigma) for s in S_range_greeks]
vega_values = [vega(s, K_greeks, T, r, sigma) for s in S_range_greeks]

fig_greeks = go.Figure()
fig_greeks.add_trace(go.Scatter(x=S_range_greeks, y=delta_values, mode='lines', name='Delta (call)', line=dict(color="#4DA3FF", width=3)))
fig_greeks.add_trace(go.Scatter(x=S_range_greeks, y=gamma_values, mode='lines', name='Gamma', line=dict(color="#FFB84D", width=3)))
fig_greeks.add_trace(go.Scatter(x=S_range_greeks, y=vega_values, mode='lines', name='Vega', line=dict(color="#7CE38B", width=3)))
fig_greeks.add_vline(x=K_greeks, line_dash="dash", line_color="#8FA3BF", annotation_text="K")

fig_greeks.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0B1F3A",
    plot_bgcolor="#0B1F3A",
    xaxis_title="Stock price (S)",
    yaxis_title="Greek value",
    height=450,
)

st.plotly_chart(fig_greeks, use_container_width=True)