from datetime import date
import numpy as np
import matplotlib.pyplot as plt

S0 = 178.40
v = 0.09
present = date.today()
expiration = date(2024, 12, 30)
T = (expiration-present).days/365
time_step = 7
X = 180.41
drift = .2
r = 0.07
v = 0.09
num_of_simulations = 100

def monte_carlo_simulation(spot_price, volatility, drift, T, time_steps, num_of_simulations):
    deltaT = T / time_steps
    time_array = np.empty(time_steps+1)
    t = deltaT
    final_stock_prices = np.empty(num_of_simulations)
    plt.title('Monte Carlo Stock Price Simulations')
    plt.xlabel('Time/365 days')
    plt.ylabel('Stock Price')
    for i in range(time_steps):
        time_array[i+1] = t
        t += deltaT
    for i in range(num_of_simulations):
        St = spot_price
        simulated_stock_prices = np.empty(time_steps+1)
        simulated_stock_prices[0] = St
        for j in range(time_steps):
            Zt = np.random.default_rng().standard_normal()
            Sdt = St + drift*St*deltaT + volatility*St*np.sqrt(deltaT)*Zt
            # Sdt = St * np.exp(drift*deltaT + volatility*np.sqrt(deltaT)*Zt)
            simulated_stock_prices[j+1] = Sdt
            St = Sdt
        plt.plot(time_array, simulated_stock_prices)
        final_stock_prices[i] = simulated_stock_prices[-1]
    plt.show()
    return final_stock_prices

final_stock_prices = monte_carlo_simulation(S0, v, drift, T, 1000, 200)

fair_option_price = 0
for i in range(100):
    St = final_stock_prices[i]
    fair_option_price += max(St-X, 0)

fair_option_price /= 100
fair_option_price *= np.exp(-r*T)
print(fair_option_price)
