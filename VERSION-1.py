import yfinance as yf

symbol = input("Enter Stock Symbol (Example: INFY.NS): ").upper()

stock = yf.Ticker(symbol)

data = stock.history(period="5d")

if data.empty:
    print("❌ Invalid Stock Symbol")
    exit()

info = stock.info

score = 0
max_score = 10

reasons = []

price = stock.fast_info.get("lastPrice")

print("\nCurrent Price :", price)

market_cap = info.get("marketCap")

print("Market Cap :", market_cap)

if market_cap is not None:
    if market_cap > 100_000_000_000:
        score += 1
        reasons.append("✓ Large Market Cap")
    else:
        reasons.append("✓ Small / Mid Cap")

pe = info.get("trailingPE")

print("P/E Ratio :", pe)

if pe is not None:
    if pe < 25:
        score += 1
        reasons.append("✓ Healthy P/E Ratio")
    else:
        reasons.append("✗ High P/E Ratio")

pb = info.get("priceToBook")

print("P/B Ratio :", pb)

if pb is not None:
    if pb < 5:
        score += 1
        reasons.append("✓ Healthy P/B Ratio")
    else:
        reasons.append("✗ High P/B Ratio")

roe = info.get("returnOnEquity")

if roe is not None:

    roe = roe * 100

    print("ROE :", roe, "%")

    if roe > 20:
        score += 2
        reasons.append("✓ Excellent ROE")

    elif roe > 15:
        score += 1
        reasons.append("✓ Good ROE")

    else:
        reasons.append("✗ Weak ROE")

de = info.get("debtToEquity")

print("Debt To Equity :", de)

if de is not None:

    if de < 50:
        score += 2
        reasons.append("✓ Low Debt")

    else:
        reasons.append("✗ High Debt")

cash = stock.cashflow

if "Operating Cash Flow" in cash.index:

    operating_cash = cash.loc["Operating Cash Flow"].iloc[0]

    print("Operating Cash Flow :", operating_cash)

    if operating_cash > 0:

        score += 2

        reasons.append("✓ Positive Operating Cash Flow")

    else:

        reasons.append("✗ Negative Operating Cash Flow")

else:

    print("Operating Cash Flow : Not Available")

    reasons.append("✗ Operating Cash Flow Not Available")

balance = stock.balance_sheet

if (
    "Current Assets" in balance.index and
    "Current Liabilities" in balance.index
):

    current_assets = balance.loc["Current Assets"].iloc[0]

    current_liabilities = balance.loc["Current Liabilities"].iloc[0]

    current_ratio = current_assets / current_liabilities

    print("Current Ratio :", round(current_ratio, 2))

    if current_ratio >= 1:

        score += 1

        reasons.append("✓ Healthy Current Ratio")

    else:

        reasons.append("✗ Weak Current Ratio")

else:

    print("Current Ratio : Not Available")

print("\n===============================")
print(" STOCK FUNDAMENTAL REPORT")
print("===============================")

print("Score :", score, "/", max_score)

print("\nReasons")

for reason in reasons:
    print(reason)

print("\nOverall Rating")

if score >= 9:
    print("★★★★★ Excellent Fundamentals")

elif score >= 7:
    print("★★★★ Strong Fundamentals")

elif score >= 5:
    print("★★★ Average Fundamentals")

elif score >= 3:
    print("★★ Weak Fundamentals")

else:
    print("★ High Financial Risk")