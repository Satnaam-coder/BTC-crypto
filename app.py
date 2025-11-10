# Load last 60 days real BTC price (if available)
try:
    import yfinance as yf
    btc = yf.download('BTC-USD', start='2015-01-01')
    btc = btc[['Close']]
    btc = btc.dropna()
    data = btc['Close'][-60:]
except Exception as e:
    data = None

# Load predicted 30-day BTC prices
pred = pd.read_csv("btc_pred.csv")
pred['date'] = pd.to_datetime(pred['date'])

st.title('Bitcoin (BTC) Price Prediction')
st.write('Last 60 Real Days (Blue) — Next 30 Predicted Days (Orange)')

fig, ax = plt.subplots()
if data is not None:
    ax.plot(data.index, data.values, label='Actual (last 60)')
ax.plot(pred['date'], pred['pred'], label='Predicted (next 30)')
ax.set_xlabel('Date')
ax.set_ylabel('BTC Price')
ax.legend()
st.pyplot(fig)

st.write('Predicted Prices Table:')
st.dataframe(pred)