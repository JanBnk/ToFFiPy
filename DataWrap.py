from scipy.io import loadmat

class DataWrap:
    '''Class for loading data in matlab format
    
    - Obligatory data structures with fields:
        - Data: self.sig['data']
            - trial 
            - time
            - label
            - fsample
        - spatial filter: self.lcmv['spatialFilter']
        - brain atlas
            - sourceAtlas:
                - dim: [20 25 22]
                - transform: [4×4 double] 
                - unit: 'cm'
                - tissue: [20×25×22 double]
                - tissuelabel: {1×100 cell}
        - common source grid = sourcemodel = template grid = commonData/templategrid_HCP_8mm.mat
            - xgrid
            - ygrid
            - zgrid
            - dim
            - pos
            - inside
            - outside
    
    '''
    
    
    def __init__(self, data_dir: str, sub: int, sourcemodel: str, atlas: str):
        self.data_dir = data_dir #loading the data directory path
        self.cov = loadmat(f'{data_dir}/Sub_{sub}/data_clean_covmat_HCP_att2_{sub}.mat', simplify_cells=True) #loading covariance matrix
        self.sig = loadmat(f'{data_dir}/Sub_{sub}/data_clean_HCP_att2_{sub}.mat', simplify_cells=True) #loading data frame - MGE signal etc.
        self.lcmv = loadmat(f'{data_dir}/Sub_{sub}/flt_LCMV_HCP_att2_{sub}.mat', simplify_cells=True) #loading lcmv filter
        self.template = loadmat(f'{sourcemodel}', simplify_cells=True)
        
        self.data = self.sig['data']
        
        # self.fsample = self.sig['data']['fsample']
        # self.trial = self.sig['data']['trial']
        # self.time = self.sig['data']['time']
        # self.label = self.sig['data']['label']
        
        self.atl = loadmat(atlas, simplify_cells=True)
        self.atlas = self.atl['sourceAtlas']
        # self.dim = self.atlas['dim']#[0][0][0][0]
        # self.transform = self.
        
        self.sourcemodel = self.template['sourcemodel']