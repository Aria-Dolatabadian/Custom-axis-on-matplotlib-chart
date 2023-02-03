import numpy as np
import matplotlib.pyplot as plt
number = [3, 12, 5, 18, 25]
gene = ('RLK', 'RLP', 'NBS', 'CNL', 'TNL')
y_pos = np.arange(len(gene))
plt.bar(y_pos, number, color=(0.2, 0.4, 0.1, 0.8))
# Custom ticks
plt.tick_params(axis='x', colors='green', direction='out', length=10, width=2)
plt.tick_params(axis='y', colors='red', direction='out', length=10, width=2)
# use the plt.xticks function to custom labels
plt.xticks(y_pos, gene, color='blue', rotation=45, fontweight='bold', fontsize='10', horizontalalignment='right')
# Custom Axis title
plt.xlabel('Genes', fontweight='bold', color='purple', fontsize='10', horizontalalignment='center')
plt.ylabel('Number', fontweight='bold', color='gray', fontsize='10', horizontalalignment='center')
# Set the limit
# plt.xlim(0,20)
plt.show()
