# !pip install pandas-datareader
# !pip install yfinance
# !pip install quandl

import numpy as np
import yfinance as yf
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

# %matplotlib inline
#from pandas_datareader import data as wb
#import quandl

training_horizon = 100
testing_horizon = 50

#Change the ticker according the company you want to backtest the model on
ticker = 'PG'
data = yf.download(ticker, start='2007-01-01')['Close']
#The company we will use for our analysis will be Apple. 
#The timeframe under consideration reflects the past 17 years, starting from January the 1st 2007.

#Why Use Adjusted Prices Instead of Raw Closing Prices?
#For financial calculations such as returns, volatility, or trend analysis, 
#the adjusted prices ensure accuracy by normalizing the data. 
#Without this, the raw closing price (Close) may show artificial jumps or drops 
#that don’t represent actual market behavior.


#Monte Carlo Simulation
def monte_carlo_simulation(data, testsize = 0.4, simulation = 1000, training_horizon = 100, testing_horizon = 50):
    #step 1: train test data set split
    data = np.array(data)
    train_size = int(len(data)*(1-testsize))
    train_data = data[:train_size]
    test_data = data[train_size:]

    #step 2: log returns calculation
    pct_changes = (train_data[1:] - train_data[:-1]) / train_data[:-1]  # Element-wise percentage change
    log_returns = np.log(1 + pct_changes)


    #step 3: Calculate drift(mu) and volatility(sigma or standard deviation)
    mu = log_returns.mean()
    sigma = log_returns.std()

    #step 4: store predictions
    simulations = {}

    #step 5: perform simulations
    for i in range(simulation):
        S_0 = train_data[-1] #last price in training set
        simulated_prices = [S_0]

        for t in range(training_horizon+testing_horizon):
            #geometric brownian motion
            Z_t = norm.rvs()
            next_price = simulated_prices[-1] * np.exp((mu - 0.5 * sigma**2)+ sigma*Z_t)
            simulated_prices.append(next_price)

        simulations[i] = simulated_prices

    
    #step 6: calculate std dev of each simulation and compare with actual data
    min_std_dev = float('inf')
    best_simulation = None

    for sim_key, sim_values in simulations.items():
        #compare forecast with actual test data
        forecast = np.array(sim_values[training_horizon+1:])
        actual = np.array(test_data[:testing_horizon])

        #compute std dev
        std_dev = np.std(forecast - actual)

        if std_dev < min_std_dev:
            min_std_dev = std_dev
            best_simulation = sim_key
    return simulations[best_simulation], min_std_dev

#I have kept the test size as 0.4, which means that 40% of the data will be used for testing, 
# training horizon as 100, and testing horizon as 50. We can change these parameters and see that the model doesn't get any better.

best_simulation_data, min_std_dev = monte_carlo_simulation(data)
print('Best Simulation Data:', best_simulation_data)
print('Min Std Dev:', min_std_dev)

# Extract the portion of test data for the comparison
test_size = int(len(data) * 0.4)
test_data = data[-test_size:]  # Last 40% of the data

# Align the lengths of simulated data and actual test data
testing_horizon = len(best_simulation_data)  # Use the length of the best simulation data
actual_test_data = test_data[:testing_horizon]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(range(len(actual_test_data)), actual_test_data, label="Actual Test Data", color='blue', linewidth=2)
plt.plot(range(len(best_simulation_data)), best_simulation_data, label="Best Simulation Data", color='orange', linestyle='--', linewidth=2)

# Add labels, title, and legend
plt.title("Comparison of Simulated Data vs Actual Test Data")
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()



##remove this if not necessary
