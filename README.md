# 🐎 BackToLay Ponies: A DOB In-Play Trading Engine

> “The horse doesn’t need to win — it just needs to run well enough to make people believe.”  
> — A Foolish Genius With a Dream (probably)

---

## 🎯 What is this?

A Python-based analytics engine that identifies **DOB** (Double or Bust) trading opportunities in UK horse racing markets.  
This project analyzes 2+ years of **in-play betting data** to locate **front-runners** with a history of significant mid-race price drops.

**Core Idea:**  
> Back horses priced between 9.0 and 20.0, and hedge once their in-play odds halve.

### ✅ Why It Works

- **Volatility** is highest when the gates fly open.
- Front-runners often trade down **even if they lose**.
- We're not betting on winners — we're trading on belief.

---

## 📊 Strategy Details

- Back horses with **Betfair Starting Price (BSP)** between 9.0 and 20.0.
- Monitor historic in-play low prices.
- Score based on **how often** and **how much** prices dropped.
- Create a shortlist of horses likely to drop **>50% in-play**, offering **low-risk hedge opportunities**.

---

## 🛠 How to Use

### 1. Prepare your dataset  
Get historical race data with at least:

- `HorseName`
- `RaceDate`
- `BSP`
- `InPlayLow`

> Tools like [In-Running Trading Tool by Proform](https://caanberry.com/in-running-trading-tool-review/) can help.

---

### 2. Load and Analyze

```bash
python dob_pony_bot.py
