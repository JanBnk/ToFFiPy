import numpy as np

def get_roi(sub, roi, pow_spectra_normalized):
    roiNr = roi

    selROIvoxels = sub.atlas['tissue'] == roiNr
    selROIvoxels = selROIvoxels.flatten(order='F')

    tissue_idx = np.where(selROIvoxels==True)

    tissue_idx = tissue_idx[0].tolist()

    inside_idx = []
    for idx in range(len(sub.sourcemodel['inside'])):
        if sub.sourcemodel['inside'][idx] in tissue_idx:
            inside_idx.append(idx)
        


    roiPower = np.mean(pow_spectra_normalized[:,inside_idx], axis=1)

    #reshaping roiPower array for easier usage
    roiPower_r = np.empty((282,256), dtype=object)
    for itrial in range(len(roiPower)):
        for ipow in range(len(roiPower[itrial])):
            roiPower_r[itrial, ipow] = roiPower[itrial][ipow]
    roiPower = roiPower_r
    
    return roiPower