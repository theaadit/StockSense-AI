
import yfinance as yf
import pandas_ta as ta
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()



gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
grok_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


symbol = input("Enter Stock Symbol (e.g. RELIANCE.NS): ").upper()
stock = yf.Ticker(symbol)

history = stock.history(period="1y")

if history.empty:
    print("❌ Invalid Stock Symbol or no market data available")
    exit()



info = stock.info

market_details = {
    "symbol": symbol,
    "current_price": stock.fast_info.get("lastPrice"),
    "52_week_high": info.get("fiftyTwoWeekHigh"),
    "52_week_low": info.get("fiftyTwoWeekLow"),
    "50_day_average": info.get("fiftyDayAverage"),
    "200_day_average": info.get("twoHundredDayAverage"),
    "history": stock.history(period="1y"),}


fundamental_details = {
    "company_name": info.get("longName"),
    "market_cap": info.get("marketCap"),
    "pe_ratio": info.get("trailingPE"),
    "forward_pe": info.get("forwardPE"),
    "peg_ratio": info.get("pegRatio"),
    "price_to_book": info.get("priceToBook"),
    "price_to_sales": info.get("priceToSalesTrailing12Months"),
    "revenue": info.get("totalRevenue"),
    "profit": info.get("netIncomeToCommon"),
    "eps": info.get("trailingEps"),
    "roe": info.get("returnOnEquity"),
    "roa": info.get("returnOnAssets"),
    "profit_margin": info.get("profitMargins"),
    "operating_margin": info.get("operatingMargins"),
    "debt": info.get("totalDebt"),
    "cash": info.get("totalCash"),
    "debt_to_equity": info.get("debtToEquity"),
    "operating_cash_flow": info.get("operatingCashflow"),
    "free_cash_flow": info.get("freeCashflow"),
    "current_ratio": info.get("currentRatio"),
    "dividend_yield": info.get("dividendYield"),
    "sector": info.get("sector"),
    "industry": info.get("industry"),}


technical_details = {
    "rsi": ta.rsi(history["Close"], length=14).iloc[-1],

    "macd": ta.macd(history["Close"])["MACD_12_26_9"].iloc[-1],

    "macd_signal": ta.macd(history["Close"])["MACDs_12_26_9"].iloc[-1],

    "sma_20": history["Close"].rolling(20).mean().iloc[-1],

    "sma_50": history["Close"].rolling(50).mean().iloc[-1],

    "sma_200": history["Close"].rolling(200).mean().iloc[-1],

    "volume_ratio": (
        history["Volume"].iloc[-1] /
        history["Volume"].rolling(20).mean().iloc[-1]
    ),

    "return_1m": history["Close"].pct_change(22).iloc[-1] * 100,

    "return_3m": history["Close"].pct_change(66).iloc[-1] * 100,

    "return_6m": history["Close"].pct_change(132).iloc[-1] * 100,

    "atr": ta.atr(
        history["High"],
        history["Low"],
        history["Close"],
        length=14
    ).iloc[-1],
}


gemini_response =gemini_client.models.generate_content(
    model="gemini-3.5-flash",
    contents=f"""
You are a stock analysis scoring engine.

Your task is to evaluate the bullish strength of the stock based ONLY on the data provided below.

The goal is to estimate how strong the evidence is that the stock can move upward over the specified timeframe.

TIMEFRAME:
Short-to-medium term: approximately 1–3 months.

DATA:

FUNDAMENTAL DETAILS:
{fundamental_details}

MARKET DETAILS:
{market_details}

TECHNICAL DETAILS:
{technical_details}

ANALYSIS RULES:

1. FUNDAMENTALS
Evaluate:
- Revenue and profitability
- EPS
- Profit and operating margins
- ROE and ROA
- Debt, cash and debt-to-equity
- Operating cash flow and free cash flow
- Current ratio
- Valuation using P/E, forward P/E, PEG, price-to-book and price-to-sales
- Sector and industry

2. TECHNICALS
Evaluate:
- RSI
- MACD, MACD signal and MACD histogram
- 20/50/200-day moving averages
- Current price relative to moving averages
- Volume and volume ratio
- 1-month, 3-month and 6-month returns
- ATR and volatility
- 52-week high/low position
- Support and resistance

3. MARKET CONDITION
Evaluate:
- Current price trend
- Momentum
- Volume confirmation
- Trend alignment between moving averages
- Strength or weakness of recent price movement

SCORING:

0–2 = Extremely bearish
3–4 = Bearish
5 = Neutral / mixed
6–7 = Moderately bullish
8–9 = Strongly bullish
10 = Extremely bullish

IMPORTANT RULES:

- Use ONLY the information provided.
- Do NOT invent missing values, news, catalysts, events or company information.
- Do NOT calculate technical indicators yourself. The technical indicators have already been calculated.
- Treat missing or None values as unavailable information.
- Do not assume that a high score in one category automatically means the stock is bullish.
- Consider all available signals together.
- Penalize conflicting signals.
- Penalize excessive valuation.
- Penalize weak fundamentals.
- Penalize deteriorating momentum or bearish technical structure.
- Strong fundamentals alone should not produce a high short-term score if technicals are strongly bearish.
- Strong technicals alone should not produce a high score if fundamentals show major weaknesses.
- Give more importance to technical and market conditions for the 1–3 month timeframe, while still considering fundamentals.
- Do not use outside knowledge.
- Do not make a buy, sell, or hold recommendation.
- Return exactly ONE integer score from 0 to 10.

FINAL RESPONSE:
Return ONLY the number.

Example:
8

No explanation.
No reasoning.
No percentage.
No /10.
No additional text.
"""
)

grok_response = grok_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{
        "role": "user",
        "content": f"""
You are a stock analysis scoring engine.

Your task is to evaluate the bullish strength of the stock based ONLY on the data provided below.

The goal is to estimate how strong the evidence is that the stock can move upward over the specified timeframe.

TIMEFRAME:
Short-to-medium term: approximately 1–3 months.

DATA:

FUNDAMENTAL DETAILS:
{fundamental_details}

MARKET DETAILS:
{market_details}

TECHNICAL DETAILS:
{technical_details}

ANALYSIS RULES:

1. FUNDAMENTALS
Evaluate:
- Revenue and profitability
- EPS
- Profit and operating margins
- ROE and ROA
- Debt, cash and debt-to-equity
- Operating cash flow and free cash flow
- Current ratio
- Valuation using P/E, forward P/E, PEG, price-to-book and price-to-sales
- Sector and industry

2. TECHNICALS
Evaluate:
- RSI
- MACD, MACD signal and MACD histogram
- 20/50/200-day moving averages
- Current price relative to moving averages
- Volume and volume ratio
- 1-month, 3-month and 6-month returns
- ATR and volatility
- 52-week high/low position
- Support and resistance

3. MARKET CONDITION
Evaluate:
- Current price trend
- Momentum
- Volume confirmation
- Trend alignment between moving averages
- Strength or weakness of recent price movement

SCORING:

0–2 = Extremely bearish
3–4 = Bearish
5 = Neutral / mixed
6–7 = Moderately bullish
8–9 = Strongly bullish
10 = Extremely bullish

IMPORTANT RULES:

- Use ONLY the information provided.
- Do NOT invent missing values, news, catalysts, events or company information.
- Do NOT calculate technical indicators yourself. The technical indicators have already been calculated.
- Treat missing or None values as unavailable information.
- Do not assume that a high score in one category automatically means the stock is bullish.
- Consider all available signals together.
- Penalize conflicting signals.
- Penalize excessive valuation.
- Penalize weak fundamentals.
- Penalize deteriorating momentum or bearish technical structure.
- Strong fundamentals alone should not produce a high short-term score if technicals are strongly bearish.
- Strong technicals alone should not produce a high score if fundamentals show major weaknesses.
- Give more importance to technical and market conditions for the 1–3 month timeframe, while still considering fundamentals.
- Do not use outside knowledge.
- Do not make a buy, sell, or hold recommendation.
- Return exactly ONE integer score from 0 to 10.

FINAL RESPONSE:
Return ONLY the number.

Example:
8

No explanation.
No reasoning.
No percentage.
No /10.
No additional text.
"""
    }]
)
gemini_text = gemini_response.text
grok_text = grok_response.choices[0].message.content
gemini_score = int(gemini_text)
grok_score = int(grok_text)
print("*"*20)
print("Gemini:", gemini_text)
print("*"*20)
print("Grok:", grok_text)
print("*"*20)
difference = abs(gemini_score - grok_score)

if gemini_score >= 8 and grok_score >= 8:
    result = "STRONG BULLISH"

elif gemini_score >= 7 and grok_score >= 7:
    result = "BULLISH"

elif gemini_score >= 7 and grok_score >= 5 and difference <= 3:
    result = "BULLISH LEAN"

elif gemini_score <= 3 and grok_score <= 3:
    result = "STRONG BEARISH"

elif gemini_score <= 4 and grok_score <= 4:
    result = "BEARISH"

elif gemini_score <= 5 and grok_score <= 6 and difference <= 3:
    result = "BEARISH LEAN"

else:
    result = "UNCERTAIN"

print("*" * 20)
print("FINAL RESULT:", result)