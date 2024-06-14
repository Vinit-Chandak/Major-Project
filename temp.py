import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Without System Prompt', 'With System Prompt']
gemini_values_total_wrong = [15.2, 10.8]
gpt4o_values_total_wrong = [12.2, 10.6]
claude_values_total_wrong = [29.5, 26.6]

x = np.arange(len(categories))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()

bars1 = ax.bar(x - width, gemini_values_total_wrong, width, label='Gemini-1')
bars2 = ax.bar(x, gpt4o_values_total_wrong, width, label='GPT-4o')
bars3 = ax.bar(x + width, claude_values_total_wrong, width, label='Claude 3 Opus')

# Add values on the bars
ax.bar_label(bars1, padding=3, fmt='%.1f')
ax.bar_label(bars2, padding=3, fmt='%.1f')
ax.bar_label(bars3, padding=3, fmt='%.1f')

ax.set_ylabel('Percentage')
ax.set_title('Total Wrong Responses with and without System Prompts')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, 100)
ax.legend()

fig.tight_layout()
plt.show()