import pandas as pd

# Data for both in-domain and out-of-domain translations
data = {
    'Domain': ['In-domain', 'Out-of-domain'],
    'BLEU Score': [14.7, 0.6],
    '1-gram Precision': [35.4, 16.8],
    '2-gram Precision': [18.1, 2.1],
    '3-gram Precision': [10.8, 0.2],
    '4-gram Precision': [6.7, 0.0],
    'BP (Brevity Penalty)': [1.000, 1.000],
    'Ratio': [1.465, 1.464],
    'Hyp Length': [10192, 21389],
    'Ref Length': [6957, 14614]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
print(df)
