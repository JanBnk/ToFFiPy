from os.path import exists
import sys
from DataWrap import *
import numpy as np

isub = int(sys.argv[1])

roi = 5

print('Preparing data...','\n')

data_dir = "/Users/jan/Documents/Studia/AdvancedProgramming/project/ToFFi_Toolbox-master/ToFFi_Toolbox-20211013/DATA_PREPARATION/HCP_DATA_PREP/output/000000_RENAMED"

atlas_dir = '/Users/jan/Documents/Studia/AdvancedProgramming/project/ToFFi_Toolbox-master/ToFFi_Toolbox-20211013/commonData/Schaefer2018_100Parcels_7Networks_ATLAS_interpolated_on_8mm_HCP_template.mat'

template_dir = '/Users/jan/Documents/Studia/AdvancedProgramming/project/ToFFi_Toolbox-master/ToFFi_Toolbox-20211013/commonData/templategrid_HCP_8mm.mat'


#loading and preparing subject data 
sub = DataWrap(data_dir=data_dir, sub=isub, sourcemodel=template_dir, atlas=atlas_dir)

#checking for data after source projection
if exists('./src_proj.npy'):
    print('Source projection array already exists, loading...\n')
    data_src = np.load('./src_proj.npy', allow_pickle=True).item()
    
else: #if doesn't exist compute it
    print('Source projection array does not exist, generating...\n')
    from sourceProjection import sourceProjection
    data_src = sourceProjection(sub.data, sub.lcmv)
    np.save('./src_proj', data_src)
    

print('Calculating fourier transform...')    
#checking if data after fourier transform exists
if exists('./pow_spectra_norm.npy'):
    print('Exists, loading...\n')
    pow_spectra_norm = np.load('./pow_spectra_norm.npy', allow_pickle=True)
    
else:
    print('Does not exist, generating...\n')
    from fourierAnalysis import *
    
    pow_spectra = calculate_mtmp(data_src)
    
    print('Normalizing powers...')
    pow_spectra_norm = normalize_powers(pow_spectra)
    
    np.save('./pow_spectra_norm', pow_spectra_norm)
    
print('Getting powers for voxels in ROI... \n')

from gettingROI import get_roi

roiPower = get_roi(sub, roi, pow_spectra_norm)

print('Calculating k-means...\n')

from clusteringPowers import *

clusters, freqs, cluster_0_dur, cluster_1_dur = clusteringPowers(roiPower)

from visualizer import visualizer

print('Plotting...')

visualizer(clusters, freqs, cluster_0_dur, cluster_1_dur, sub, isub, roi)


