import pandas as pd
from backtest.backtest_engine import BackTest
from backtest.metrics import GetMetrics
from strategies.EMA_strategy import EMAStrategy
data = pd.read_pickle('Data/preprocessed_data/preprocessed_data.pkl')


strategy = EMAStrategy(9,15)

class BackTestCaller:

    def __init__(self, amount):
        self.backtester = BackTest(amount)
        

    def call(self, data, strategy):
        try:
            return self.backtester.back_test_engine(data, strategy)
        except Exception as e:
            return str(e)
   
        
        
caller = BackTestCaller(1000)
state_history = caller.call(data,strategy)
print(state_history)

class Metrics:
    def __init__(self,state_history):
        self.get_metrics = GetMetrics(state_history)
        
    def get_metrices(self):
        try:
            return self.get_metrics.metrics()
        except Exception as e:
             return str(e)
        
metric_result = Metrics(state_history)
get_matric_result = metric_result.get_metrices()
print(get_matric_result)