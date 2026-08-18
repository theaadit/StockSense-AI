
import yfinance as yf
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()



gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
grok_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


symbol = input("Enter Stock Symbol: ").upper()
stock = yf.Ticker(symbol)

if stock.history(period="5d").empty:
    print("❌ Invalid Stock Symbol")
    exit()

info = stock.info

stock_data = {
    "symbol": symbol,
    "company_name": info.get("longName"),
    "current_price": stock.fast_info.get("lastPrice"),
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
    "industry": info.get("industry"),
    "52_week_high": info.get("fiftyTwoWeekHigh"),
    "52_week_low": info.get("fiftyTwoWeekLow"),
    "50_day_average": info.get("fiftyDayAverage"),
    "200_day_average": info.get("twoHundredDayAverage"),
}


gemini_response =gemini_client.models.generate_content(
    model="gemini-3.5-flash",
    contents=f"""You are a professional stock-analysis scoring engine.

Analyze the stock data I provide and give a 0–10 score for the strength of the stock's potential to move UP over the specified timeframe.

Evaluate BOTH:

TECHNICALS
- Trend, momentum, RSI, MACD
- Moving averages
- Volume
- Support/resistance
- Breakouts/breakdowns
- Volatility and relative strength

COMPANY & FUNDAMENTALS
- What the company does and its business model
- Industry/sector and industry outlook
- Market position and competitive advantages
- Brand/reputation and management, if provided
- Revenue, earnings, margins, cash flow, debt and valuation
- Growth potential
- Competitive environment
- Catalysts, news and major risks

IMPORTANT:
- Judge the company according to its specific industry and business type.
- Combine all signals rather than relying on one indicator.
- Penalize conflicting signals, weak confirmation, poor fundamentals, excessive valuation and major risks.
- Consider the specified timeframe.
- Do not invent missing information; lower confidence when important data is missing.
- Do all analysis internally.

SCORING:
0/10 = Extremely bearish
5/10 = Neutral/uncertain
10/10 = Extremely bullish

Your score represents the overall bullish strength after considering technicals + company + industry + fundamentals + risks.
hee is the stock data={stock_data}
FINAL RESPONSE:
Reply with ONLY:


x/10

No explanation, no reasoning, no percentage, no buy/sell/hold recommendation, and no additional text.
just th score like this x/10"""
)

grok_response = grok_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{
        "role": "user",
        "content": f"""You are a professional stock-analysis scoring engine.

Analyze the stock data I provide and give a 0–10 score for the strength of the stock's potential to move UP over the specified timeframe.

Evaluate BOTH:

TECHNICALS
- Trend, momentum, RSI, MACD
- Moving averages
- Volume
- Support/resistance
- Breakouts/breakdowns
- Volatility and relative strength

COMPANY & FUNDAMENTALS
- What the company does and its business model
- Industry/sector and industry outlook
- Market position and competitive advantages
- Brand/reputation and management, if provided
- Revenue, earnings, margins, cash flow, debt and valuation
- Growth potential
- Competitive environment
- Catalysts, news and major risks

IMPORTANT:
- Judge the company according to its specific industry and business type.
- Combine all signals rather than relying on one indicator.
- Penalize conflicting signals, weak confirmation, poor fundamentals, excessive valuation and major risks.
- Consider the specified timeframe.
- Do not invent missing information; lower confidence when important data is missing.
- Do all analysis internally.

SCORING:
0/10 = Extremely bearish
5/10 = Neutral/uncertain
10/10 = Extremely bullish

Your score represents the overall bullish strength after considering technicals + company + industry + fundamentals + risks.
hee is the stock data={stock_data}
FINAL RESPONSE:
Reply with ONLY:


x/10

No explanation, no reasoning, no percentage, no buy/sell/hold recommendation, and no additional text.
just th score like this x/10"""
    }]
)
gemini_text = gemini_response.text
grok_text = grok_response.choices[0].message.content
gemini_score = int(gemini_text.split("/")[0].strip())
grok_score = int(grok_text.split("/")[0].strip())
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