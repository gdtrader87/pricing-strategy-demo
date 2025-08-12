import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def generate_data(n=50, noise_scale=100):
    """Generate a synthetic price/quantity dataset."""
    np.random.seed(42)
    price = np.linspace(5, 50, n)
    quantity = 1000 - 10 * price + np.random.normal(scale=noise_scale, size=n)
    quantity = np.maximum(quantity, 0)
    return pd.DataFrame({'price': price, 'quantity': quantity})


def estimate_demand(df: pd.DataFrame) -> LinearRegression:
    """Fit a simple linear demand curve Q = a + b * P using least squares."""
    X = df[['price']]
    y = df['quantity']
    model = LinearRegression()
    model.fit(X, y)
    return model


def compute_price_elasticity(model: LinearRegression, price: float) -> float:
    """Compute price elasticity of demand at a specific price point."""
    slope = model.coef_[0]
    quantity = model.predict(np.array([[price]]))[0]
    # elasticity = (dQ/dP) * (P / Q)
    return slope * price / quantity if quantity != 0 else 0


def plot_revenue_curve(df: pd.DataFrame, model: LinearRegression, filename: str = 'revenue_vs_price.png') -> float:
    """Plot revenue as a function of price and mark the revenue-maximizing price."""
    price_range = np.linspace(df['price'].min(), df['price'].max(), 100)
    quantity_pred = model.predict(price_range.reshape(-1, 1))
    revenue = price_range * quantity_pred
    optimal_idx = int(np.argmax(revenue))
    optimal_price = price_range[optimal_idx]
    # Plot
    plt.figure()
    plt.plot(price_range, revenue, label='Revenue vs Price')
    plt.axvline(optimal_price, color='r', linestyle='--', label=f'Optimal price: {optimal_price:.2f}')
    plt.xlabel('Price')
    plt.ylabel('Revenue')
    plt.title('Revenue vs Price')
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return optimal_price


if __name__ == '__main__':
    # Generate synthetic demand data
    df = generate_data()
    # Estimate demand curve
    model = estimate_demand(df)
    # Plot revenue curve and compute optimal price
    opt_price = plot_revenue_curve(df, model)
    elasticity_at_opt = compute_price_elasticity(model, opt_price)
    print(f"Optimal price: {opt_price:.2f}")
    print(f"Price elasticity at optimal price: {elasticity_at_opt:.2f}")
