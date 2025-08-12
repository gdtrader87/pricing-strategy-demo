import pandas as pd
import numpy as np


def generate_data():
    """Generate synthetic pipeline and usage data with parent/child companies."""
    np.random.seed(42)
    parents = {
        'General Mills': ['Cheerios Subsidiary', 'Betty Crocker Subsidiary', 'Haagen‑Dazs Division'],
        'Disney': ['Disney+ Subsidiary', 'Marvel Entertainment', 'Pixar Animation Studios'],
        'Toyota': ['Lexus Division', 'Daihatsu Division', 'Hino Motors'],
        'General Motors': ['Chevrolet', 'GMC', 'Cadillac'],
        'Microsoft': ['Xbox Division', 'Azure Cloud', 'Office Division']
    }
    regions = ['Americas', 'EMEA', 'APAC']
    solutions = ['CCE', 'DCE', 'CCE Pro', 'Stock', 'Sign', 'Substance', 'XD']
    sales_motions = ['Growth on renewal', 'New', 'True Up']
    rows = []

    for parent, subs in parents.items():
        for child in subs:
            region = np.random.choice(regions)
            for solution in solutions:
                for motion in sales_motions:
                    # Generate pipeline and forecast values
                    pipe_actual = np.random.randint(1_000_000, 20_000_001)
                    qrf = pipe_actual * (0.8 + np.random.rand() * 0.4)  # QRF within 80–120% of pipe_actual
                    # Generate seat metrics
                    entitlement = np.random.randint(1000, 5001)
                    assigned = int(entitlement * np.random.uniform(0.5, 1.2))
                    assigned = min(assigned, entitlement)
                    activated = int(assigned * np.random.uniform(0.3, 1.0))
                    # Quick, minimal and reduced minimal activations
                    qal = np.random.randint(0, activated + 1)
                    mal = np.random.randint(0, activated - qal + 1)
                    rmal = max(activated - qal - mal, 0)
                    tickets = np.random.poisson(5)
                    # Compose row
                    row = {
                        'parent_company': parent,
                        'child_company': child,
                        'region': region,
                        'solution': solution,
                        'sales_motion': motion,
                        'pipe_actual': pipe_actual,
                        'qrf': qrf,
                        'pipe_gap': qrf - pipe_actual,
                        'pipe_gap_ratio': (qrf - pipe_actual) / qrf if qrf != 0 else 0,
                        'entitled_seats': entitlement,
                        'assigned_seats': assigned,
                        'activated_seats': activated,
                        'assignment_rate': assigned / entitlement if entitlement > 0 else 0,
                        'activation_rate': activated / assigned if assigned > 0 else 0,
                        'qal': qal,
                        'mal': mal,
                        'rmal': rmal,
                        'support_tickets': tickets,
                    }
                    rows.append(row)

    df = pd.DataFrame(rows)

    def health(row):
        """Derive a simple health indicator based on activation rate and pipeline coverage."""
        coverage = row['pipe_actual'] / row['qrf'] if row['qrf'] != 0 else 0
        if row['activation_rate'] >= 0.7 and coverage >= 1.0:
            return 'Green'
        elif row['activation_rate'] >= 0.5:
            return 'Yellow'
        else:
            return 'Red'

    df['customer_health'] = df.apply(health, axis=1)
    return df


if __name__ == '__main__':
    df = generate_data()
    # Save synthetic dataset to CSV for further analysis
    df.to_csv('synthetic_pricing_dataset.csv', index=False)
    print(df.head())
