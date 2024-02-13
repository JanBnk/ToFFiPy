import matplotlib.pyplot as plt

def visualizer(clusters, freqs, cluster_0_dur, cluster_1_dur, sub, isub, roi):
    plt.scatter(freqs[:120], clusters[0][:120], s=2, c='b')
    plt.scatter(freqs[:120], clusters[1][:120], s=2, c='r')
    
    roi = sub.atlas['tissuelabel'][roi-1]
    
    plt.scatter(freqs[:120], clusters[0][:120], s=2)
    plt.scatter(freqs[:120], clusters[1][:120], s=2, c='r')

    plt.xlabel("Frequencies")
    plt.ylabel("Normalized Power")
    plt.legend([f'Cluster 1 - duration = {cluster_0_dur}%', f'Cluster 2 - duration = {cluster_1_dur}%'])

    plt.title(f"Individual fingerprint for subject {isub}, {roi}")
    
    plt.savefig('./individual_fingerprint.png')