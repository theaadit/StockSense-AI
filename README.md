# 📈 StockSense AI

### Multi-Model Stock Analysis & Financial Intelligence System

StockSense AI is a Python-based stock analysis project that combines **financial data, fundamental analysis, technical analysis, and multiple AI models** to provide a structured view of a company's financial and market condition.

The project is being developed incrementally, with each version adding a new layer of analysis and engineering.

---

# 🎯 Project Objective

The goal of StockSense AI is to analyze companies from multiple perspectives instead of relying on a single metric or AI model.

The system combines:

* Fundamental financial analysis
* Market data
* Technical indicators
* Multi-model AI analysis
* Model score comparison
* Rule-based decision logic

The project is primarily a learning-focused AI/ML engineering project exploring how financial data and AI can work together in a structured analysis pipeline.

---

# 🚀 Project Evolution

### Version 1 — Fundamental Analysis

The first version focused on traditional financial analysis using `yfinance`.

It analyzed metrics such as:

* Revenue and net income
* P/E and other valuation ratios
* ROE and ROA
* Debt and cash
* Free cash flow
* Liquidity
* Moving averages
* Company sector and industry

A rule-based scoring system was used to generate a fundamental assessment.

### Version 2 — Multi-Model AI Analysis

Version 2 introduced **Google Gemini and Groq** into the analysis pipeline.

Both models receive structured stock information and independently generate a **0–10 bullish-strength score**.

The scores are then compared using rule-based logic to produce classifications such as:

* STRONG BULLISH
* BULLISH
* BULLISH LEAN
* UNCERTAIN
* BEARISH LEAN
* BEARISH
* STRONG BEARISH

### Current Version — Improved Analysis Pipeline

The current implementation improves the data pipeline by organizing information into **fundamental, market, and technical sections**.

It also includes:

* One year of historical stock data
* RSI
* MACD
* Moving averages
* Volume
* Returns
* ATR
* Exchange-specific stock symbols such as `RELIANCE.NS`
* Improved stock validation and data handling
* More structured AI prompts
* Improved AI score parsing

---

# 🧠 How It Works

```text
             Stock Symbol
                  │
                  ▼
              yfinance
                  │
                  ▼
       ┌──────────┼──────────┐
       ▼          ▼          ▼
  Fundamental   Market    Technical
      Data       Data        Data
       │          │          │
       └──────────┼──────────┘
                  ▼
          Structured Dataset
                  │
          ┌───────┴───────┐
          ▼               ▼
       Gemini            Groq
          │               │
          ▼               ▼
      0–10 Score       0–10 Score
          │               │
          └───────┬───────┘
                  ▼
          Score Comparison
                  │
                  ▼
        Final Classification
```

---

# 🔧 Key Engineering Approach

A major design principle of StockSense AI is to let **Python handle deterministic calculations** while using AI models primarily for **interpretation and reasoning**.

For example, technical indicators such as RSI, MACD, and ATR are calculated from actual historical data before being provided to the AI models.

This helps keep the analysis more structured and consistent instead of asking AI models to calculate or assume missing information.

---

# 🛠️ Technology Stack

**Programming:** Python

**Financial Data:** `yfinance`

**AI:** Google Gemini API, Groq API

**Environment:** `python-dotenv`

**Analysis:** Fundamental analysis, technical indicators, rule-based decision logic

---

# 🔐 API Key Security

API keys are stored using environment variables.

```text
GEMINI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

The `.env` file should never be committed to GitHub.

---

# ⚠️ Limitations

StockSense AI is an educational and experimental project.

It:

* Does not guarantee future stock performance.
* Is not financial advice.
* Depends on external financial data.
* Uses rule-based logic and AI-generated analysis.
* Has not yet been extensively validated through historical backtesting.

AI outputs can also contain errors, so results should be treated as **decision-support information rather than guaranteed predictions**.

---

# 📚 What I'm Learning

Through this project, I am developing practical experience with:

* Python
* Financial data
* Fundamental and technical analysis
* API integration
* Data preprocessing
* Prompt engineering
* Multi-model AI systems
* Decision logic
* AI output parsing
* Git & GitHub
* AI/ML engineering

---

# 🏗️ Future Direction

The long-term goal is to evolve StockSense AI from a rule-based analysis system into a more rigorously evaluated machine-learning system.

---

## 👨‍💻 Author

**Aadit Khetarpal**

Computer Science Engineering — AI & Machine Learning

StockSense AI is an ongoing project for exploring artificial intelligence, financial analysis, data engineering, and machine learning through a real-world problem.

---

⭐ If you find the project interesting, consider starring the repository.

> **Disclaimer:** StockSense AI is an educational project and does not provide financial advice or guaranteed investment predictions.
