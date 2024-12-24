# MACD Oscillator Trading Strategy

## Overview

The **MACD Oscillator** is a fundamental trading strategy often referred to as "Trading Strategy 101." **MACD** stands for **Moving Average Convergence/Divergence**. It is a momentum-based strategy rooted in the belief that upward/downward momentum affects short-term moving averages more significantly than long-term moving averages.

This strategy is widely popular among non-professional traders due to its simplicity and effectiveness. In behavioral economics, it is observed that the more people adopt a strategy, the more impactful it can become. However, caution must be exercised, as widespread use does not guarantee success in every market scenario (e.g., the 2008 financial crisis).

### How the Strategy Works
- Compute **long-term moving average** and **short-term moving average** of a stock's closing price.
- Compare the two moving averages:
  - When the **short-term moving average** is above the **long-term moving average**, it signals an **uptrend**, and the stock is "longed."
  - When the **short-term moving average** is below the **long-term moving average**, it signals a **downtrend**, and the position is cleared (or the stock is "shorted").

This strategy is so simple that even individuals with no finance background can implement it in under five minutes. Despite its simplicity, it remains one of the most common strategies among traders.

---

## Features

1. **Simple Moving Average Calculation:**
   - Computes short-term and long-term moving averages for a stock’s closing price.

2. **Signal Generation:**
   - Generates buy/sell signals based on the relationship between short-term and long-term moving averages.

3. **Visualization:**
   - Plots:
     - Closing price with Buy/Sell markers.
     - Oscillator (difference between moving averages).
     - Short-term and long-term moving averages.

4. **User Input:**
   - Allows users to specify:
     - Periods for short-term and long-term moving averages.
     - Date range for historical stock data.
     - Stock ticker symbol.
     - Data slicing for cleaner visualization.

---

## Requirements

- Python 3.x
- Required libraries:
  - `matplotlib`
  - `numpy`
  - `pandas`
  - `yfinance` (replace `fix_yahoo_finance` with this updated package)

To install the required libraries:
```bash
pip install matplotlib numpy pandas yfinance
```

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/macd-oscillator-strategy.git
   ```

2. Navigate to the project directory:
   ```bash
   cd macd-oscillator-strategy
   ```

3. Run the script:
   ```bash
   python macd_strategy.py
   ```

4. Input the required parameters when prompted:
   - **`ma1`**: Short-term moving average period (e.g., `12`).
   - **`ma2`**: Long-term moving average period (e.g., `26`).
   - **`start date`**: Start date for fetching historical data (format: `yyyy-mm-dd`).
   - **`end date`**: End date for fetching historical data (format: `yyyy-mm-dd`).
   - **`ticker`**: Stock ticker symbol (e.g., `AAPL`).
   - **`slicing`**: Number of rows to slice for cleaner visualization (e.g., `100`).

5. View the generated plots for:
   - Stock price with Buy/Sell signals.
   - Oscillator and moving averages.

---

## Code Explanation

### Main Components

1. **`macd(signals)`**:
   - Computes short-term and long-term moving averages using rolling windows on the stock’s closing price.

2. **`signal_generation(df, method)`**:
   - Generates trading signals based on the relationship between moving averages.
   - Calculates the oscillator as the difference between the moving averages.

3. **`plot(new, ticker)`**:
   - Visualizes:
     - Stock price with Buy/Sell markers.
     - Oscillator (as a bar chart).
     - Moving averages (as line plots).

4. **`main()`**:
   - Collects user inputs.
   - Fetches historical stock data using `yfinance`.
   - Calls `signal_generation` to compute signals.
   - Calls `plot` to visualize the results.

---

## Example Run

### User Input:
```plaintext
ma1: 12
ma2: 26
start date in format yyyy-mm-dd: 2010-01-01
end date in format yyyy-mm-dd: 2020-01-01
ticker: AAPL
slicing: 50
```

### Output:
1. A plot showing:
   - Apple Inc. (AAPL) closing price with Buy/Sell signals.

  

   - Oscillator and moving averages.
  
    

1. Clear visualization of trading signals for backtesting.

---

## References

- **More on MACD Oscillator:** [Investopedia - MACD](https://www.investopedia.com/terms/m/macd.asp)


