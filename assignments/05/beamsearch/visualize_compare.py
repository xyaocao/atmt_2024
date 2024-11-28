import os
import json
import matplotlib.pyplot as plt

# Define the base directory and folders
base_directory = 'assignments/05/beamsearch'
folders = ['beam5', 'beam15', 'beam20', 'beam25']
beam_sizes = [5, 15, 20, 25]
bleu_scores = []
brevity_penalties = []

# Parse the data from each folder
for folder in folders:
    file_path = os.path.join(base_directory, folder, 'result.txt')
    with open(file_path, 'r') as f:
        data = json.load(f)
        bleu_scores.append(data['score'])
        bp = float(data['verbose_score'].split('(')[1].split('=')[1].split()[0])
        brevity_penalties.append(bp)

# Create the plot
fig, ax1 = plt.subplots()

# Plot BLEU score on the left y-axis
ax1.set_xlabel('Beam Size')
ax1.set_ylabel('BLEU Score', color='tab:blue')
ax1.plot(beam_sizes, bleu_scores, marker='o', label='BLEU Score', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot Brevity Penalty on the right y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Brevity Penalty', color='tab:orange')
ax2.plot(beam_sizes, brevity_penalties, marker='s', label='Brevity Penalty', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Add title and grid
plt.title('Comparison of BLEU Score and Brevity Penalty with Beam Size')
fig.tight_layout()
plt.grid(True)
plt.show()
