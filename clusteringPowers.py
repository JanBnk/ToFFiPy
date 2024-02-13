from scipy.cluster.vq import vq, kmeans2
import numpy as np

def clusteringPowers(roiPower):
    k = 2 #number of centroids

    roiPower = roiPower.astype(float)

    clusters, labels = kmeans2(roiPower, k)

    cluster_0_dur = round((np.bincount(labels)[0]/282)*100) #percentage of all values in first cluster
    cluster_1_dur = round((np.bincount(labels)[1]/282)*100)

    freqs = [x*0.99 for x in range(0,256)]
    
    return clusters, freqs, cluster_0_dur, cluster_1_dur