import os

# project paths

REPO_PATH = '/Users/imanwahle/Desktop/cfl_demo_repo'
DATA_PATH = os.path.join(REPO_PATH, 'data')
RESULTS_PATH = os.path.join(REPO_PATH, 'results')

# CFL hyperparameters

DATA_INFO = {'X_dims' : (10000, 5),
             'Y_dims' : (10000, 3),
             'Y_type' : 'continuous' #options: 'categorical' or 'continuous'
            }

CDE_PARAMS = {  'model'       : 'CondExpMod',
                'dense_units' : [50, DATA_INFO['Y_dims'][1]],
                'activations' : ['relu', 'linear'],
                'dropouts'    : [0, 0],
                'activity_regularizers' : [None] * 2,
                'kernel_regularizers' : [None] * 2,
                'bias_regularizers' : [None] * 2,               

                'batch_size'  : 32, # parameters for training
                'n_epochs'    : 80,
                'optimizer'   : 'adam',
                'opt_config'  : {'lr': 1e-4},
                'loss'        : 'mean_squared_error',
                'best'        : True,

                'verbose'     : 1, # amount of output to print
                'show_plot'   : True,
                'tb_path'     : os.path.join(REPO_PATH, 'logs'),

            }

CCLUSTER_PARAMS = {'model' : 'KMeans', 'n_clusters' : 4, 'verbose' : 0}

ECLUSTER_PARAMS = {'model' : 'KMeans', 'n_clusters' : 2, 'verbose' : 0}            