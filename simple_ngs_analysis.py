import matplotlib.pyplot as plt
import random

def simulate_ngs_data():
    read_lengths = [random.randint(50, 150) for _ in range(1000)]
    return read_lengths

def plot_read_length_distribution(read_lengths):
    plt.hist(read_lengths, bins=30, color='blue', edgecolor='black')
    plt.title('read length distribution')
    plt.xlabel('read length')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    simulated_read_lengths = simulate_ngs_data()

    plot_read_length_distribution(simulated_read_lengths)
    