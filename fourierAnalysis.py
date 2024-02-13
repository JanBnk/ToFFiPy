from spectrum import pmtm
import math
from os.path import exists
import numpy as np
#%%

def calculate_mtmp(data_src): 

    # data_src = np.load('/Users/jan/Documents/Studia/AdvancedProgramming/project/ToFFiPy/src_proj.npy', allow_pickle=True).item()

    trials = data_src['trial'][0]
    n_trials = data_src['trial'][0].shape[0]
    n_src = data_src['trial'][0][0].shape[0]

#%%

    pow_spectra = np.empty((282, 5798), dtype=object)
    trial_idx = 0
    for i_trial in trials:
    
        for i_src in range(0,n_src):
            spectrum_windowed = pmtm(i_trial[i_src,:], NW=2.5, k=5, show=False, method='unity')[0]
            pow_spectrum_trial = abs(spectrum_windowed)**2
            pow_spectrum_trial = np.mean(pow_spectrum_trial,axis=0)
            pow_spectra[trial_idx, i_src] = pow_spectrum_trial[0:int(len(pow_spectrum_trial)/2)]
        #na wyjściu - zbiór power spectrum dla każdego źródła dla każdego sampla
        #uśrednianie 
        
        trial_idx += 1
    
#%%
    return pow_spectra
    

#%% 
    
#%%

def normalize_powers(pow_spectra):
    
    mean_pow_spectra_trials = np.mean(pow_spectra, axis=0)
    mean_pow_spectra_trials_and_vox = np.mean(mean_pow_spectra_trials)

    pow_spectra_normalized = np.empty((282, 5798), dtype=object)

    trial_idx = 0
    for i_trial in trials:
    
        for i_src in range(0,n_src):
            pow_spectra_normalized[trial_idx, i_src] = pow_spectra[trial_idx, i_src]/mean_pow_spectra_trials_and_vox
        
        trial_idx += 1
        
    return pow_spectra_normalized
    # np.save('/Users/jan/Documents/Studia/AdvancedProgramming/project/ToFFiPy/pow_spectra', pow_spectra)