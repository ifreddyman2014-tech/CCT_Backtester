import MetaTrader5 as mt5
import numpy as np

def load_data(symbol, timeframe, num_bars):
    """Load historical data from MetaTrader 5 with synthetic fallback."""
    
    # Attempt to initialize MetaTrader 5
    if not mt5.initialize():
        print("MetaTrader 5 initialization failed.")
        return generate_synthetic_data(num_bars)
    
    # Request historical data
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    
    # Disconnect from MetaTrader 5
    mt5.shutdown()

    if rates is None or len(rates) == 0:
        print("Failed to retrieve data, generating synthetic data.")
        return generate_synthetic_data(num_bars)
    
    return rates

def generate_synthetic_data(num_bars):
    """Generate synthetic price data for the specified number of bars."""
    synthetic_data = np.zeros(num_bars)
    # Simple synthetic data generation
    for i in range(num_bars):
        synthetic_data[i] = np.random.uniform(low=1.0, high=1.5)  # Random prices
    return synthetic_data
