import json
import os
import matplotlib.pyplot as plt

# Sample data loading process
file_paths = [
    "assignments/03/baseline/result.txt",
    "assignments/03/lexical_model/result.txt"
]

# Initialize lists to hold data for plotting
configurations = []
scores = []

# Read data from files
for file_path in file_paths:
    with open(file_path, "r") as f:
        result_data = json.load(f)
        configurations.append(os.path.basename(os.path.dirname(file_path)))
        scores.append(result_data.get("score"))

# Create a bar plot
plt.figure(figsize=(8,6))
bars = plt.bar(configurations, scores, color='lightgreen')

# Adding the score values on top of each bar
for bar, score in zip(bars, scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x position
        bar.get_height(),                   # y position (height of the bar)
        f"{score}",                         # score as text
        ha='center',                        # center alignment
        va='bottom'                         # place text just above the bar
    )

# Labeling the plot
plt.xlabel("Configuration")
plt.ylabel("Score")
plt.title("BLEU Scores Comparison Between Baseline and Lexical model method")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
