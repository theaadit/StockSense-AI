# 📈 StockSense AI

### Multi-Model Stock Analysis & Financial Intelligence System

StockSense AI is a Python-based stock analysis project designed to evaluate publicly traded companies using financial data, fundamental analysis, and multi-model AI reasoning.

The project is being developed incrementally, with each version introducing a new layer of analysis and engineering.

The current implementation includes **Version 1 — Fundamental Analysis** and **Version 2 — Multi-Model AI Analysis**.

---

## 🎯 Project Objective

The goal of StockSense AI is to build a structured system that can analyze a company from multiple perspectives rather than relying on a single financial indicator or a single AI model.

The system currently combines:

* Financial fundamentals
* Company financial health
* Valuation metrics
* Cash-flow analysis
* Multi-model AI analysis
* Model agreement
* Rule-based decision logic

The project is being developed as a learning-focused ML engineering project, with an emphasis on progressively improving the quality, structure, and reliability of the analysis.

---

# 🚀 Current Versions

## Version 1 — Fundamental Stock Analyzer

Version 1 focuses on traditional fundamental analysis.

The application retrieves financial information using `yfinance` and evaluates the company using a rule-based scoring system.

### 📊 Metrics Analyzed

* Current Stock Price
* Market Capitalization
* P/E Ratio
* Forward P/E
* PEG Ratio
* Price-to-Book Ratio
* Price-to-Sales Ratio
* Revenue
* Net Income
* EPS
* Return on Equity (ROE)
* Return on Assets (ROA)
* Profit Margin
* Operating Margin
* Total Debt
* Cash
* Debt-to-Equity Ratio
* Operating Cash Flow
* Free Cash Flow
* Current Ratio
* Dividend Yield
* 52-Week High
* 52-Week Low
* 50-Day Moving Average
* 200-Day Moving Average
* Sector
* Industry

### 🧠 Rule-Based Scoring

The system evaluates financial metrics and generates an overall fundamental assessment.

The analysis considers factors such as:

* Valuation
* Profitability
* Debt
* Cash flow
* Liquidity
* Company size

---

# 🤖 Version 2 — Multi-Model AI Analysis

Version 2 introduces two independent AI models into the analysis pipeline:

### Gemini

Gemini receives the structured stock dataset and evaluates the company's:

* Fundamentals
* Valuation
* Financial strength
* Growth potential
* Industry
* Business characteristics
* Technical context when available
* Potential risks

It produces a **0–10 bullish-strength score**.

### Groq

Groq independently analyzes the same structured dataset and produces its own **0–10 bullish-strength score**.

---

# 🔄 Version 2 Architecture

```text
                 User
                  │
                  ▼
          Enter Stock Symbol
                  │
                  ▼
             yfinance
                  │
                  ▼
        Structured Stock Data
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
         Decision Logic
                  │
                  ▼
          Final Classification
```

---

# 🧮 Decision System

The two AI scores are compared using rule-based logic.

Possible outputs include:

* **STRONG BULLISH**
* **BULLISH**
* **BULLISH LEAN**
* **UNCERTAIN**
* **BEARISH LEAN**
* **BEARISH**
* **STRONG BEARISH**

The system also measures the difference between the two model scores to identify agreement or disagreement.

---

# 🛠️ Technology Stack

### Programming

* Python

### Financial Data

* `yfinance`

### AI APIs

* Google Gemini API
* Groq API

### Environment & Security

* `python-dotenv`
* Environment variables for API credentials

---

# 🔐 API Key Security

API keys are loaded through environment variables rather than being hard-coded into the source code.

Example:

```text
GEMINI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

The `.env` file should never be committed to GitHub.

---

# 📂 Project Evolution

```text
Version 1
│
├── Financial Data Collection
├── Fundamental Analysis
├── Financial Metrics
└── Rule-Based Scoring
        │
        ▼
Version 2
│
├── Structured Stock Dataset
├── Gemini Analysis
├── Groq Analysis
├── Multi-Model Comparison
└── Final Decision Logic
```

The project is intentionally being developed incrementally so that each version can be tested and understood before adding another layer of complexity.

---

# 💡 Why This Project?

Financial analysis involves many different signals.

A company can have:

* Strong profitability but excessive valuation
* Strong growth but high debt
* Good fundamentals but weak market momentum
* Strong financials but significant industry risks

Therefore, relying on a single metric or a single model can produce an incomplete picture.

StockSense AI explores how **structured financial data and multiple independent AI analyses can be combined into a single decision-support system.**

---

# 🧪 Example Workflow

```text
Enter Stock Symbol
        ↓
Validate Stock
        ↓
Collect Financial Data
        ↓
Create Structured Dataset
        ↓
Send Dataset to Gemini
        ↓
Receive Gemini Score
        ↓
Send Dataset to Groq
        ↓
Receive Groq Score
        ↓
Compare Scores
        ↓
Generate Final Result
```

---

# 📌 Important Engineering Principle

StockSense AI is not designed around the idea that:

> "More AI models automatically means better predictions."

Instead, the project explores how different analytical components can be combined while keeping their outputs structured, measurable, and comparable.

Future improvements will focus on **validation, historical testing, feature engineering, and machine learning**, rather than simply adding more AI models.

---

# ⚠️ Current Limitations

This project is currently a learning and research-oriented system.

The current versions:

* Do not guarantee future stock performance.
* Do not constitute financial advice.
* Depend on the availability and quality of external financial data.
* Use rule-based scoring and LLM-generated assessments.
* Do not yet provide a statistically validated prediction of future returns.
* Version 2 does not independently verify every piece of information generated by an AI model.

These limitations are intentionally documented because reliable ML systems require proper evaluation rather than assuming that a model's output is automatically correct.

---

# 📚 What I Am Learning Through This Project

This project is helping me develop practical experience with:

* Python programming
* Financial data handling
* API integration
* Structured data
* Data preprocessing
* Fundamental analysis
* Technical-analysis concepts
* Prompt engineering
* Multi-model AI systems
* Decision logic
* Environment-variable security
* Git and GitHub
* Building software incrementally

---

# 🏗️ Development Philosophy

StockSense AI is being built **version by version**.

Instead of attempting to create a complex system immediately, each version introduces a specific capability and provides a foundation for the next stage.

The long-term focus is to transform the project from a rule-based financial analyzer into a properly evaluated machine-learning system.

---

# 📜 Disclaimer

StockSense AI is an educational and experimental software project.

It is **not financial advice**, and its outputs should not be treated as guaranteed predictions or recommendations to buy or sell securities.

Always perform independent research and consult a qualified financial professional before making investment decisions.

---

## 👨‍💻 Author

**Aadit Khetarpal**

Computer Science Engineering — AI & Machine Learning

This project represents an ongoing effort to learn and apply machine learning, artificial intelligence, data analysis, and software engineering concepts through a real-world problem.

---

⭐ If you find the project interesting, consider starring the repository.
