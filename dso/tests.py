import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module='numpy.*')
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow.*')

# from dso.PDE_discover import SymEqOptimizer, DeepSymbolicOptimizer
from dso import DeepSymbolicOptimizer_PDE

# data_name = 'KdV'
config_file_path = "./dso/config/MODE1/config_pde_KdV.json"

# data_name = 'KdV'
# config_file_path = "./dso/config/MODE1/config_pde_Burgers.json"

# data_name = 'KdV'
# config_file_path = "./dso/config/MODE1/config_pde_Chafee.json"
#
# data_name = 'KdV'
# config_file_path = "./dso/config/MODE1/config_pde_Compound.json"
#
# data_name = 'KdV'
# config_file_path = "./dso/config/MODE1/config_pde_Divide.json"

# config_file_path = "./dso/config/MODE1/config_pde_chem.json"

# config_file_path = "./dso/config/MODE2/config_pde_Burgers2_noise_0.50.json"

model = DeepSymbolicOptimizer_PDE(config_file_path)

result = model.train()