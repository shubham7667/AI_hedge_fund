from EMA_strategy import EMAStrategy

import pandas as pd

data =pd.read_pickle('../Data/preprocessed_data/preprocessed_data.pkl')
strat = EMAStrategy(9,15)
result = strat.generate_signal(data)
print(result)





        
        
        
        
        
