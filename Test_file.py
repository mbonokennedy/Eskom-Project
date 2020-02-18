import numpy as np
import pandas as pd
### START FUNCTION 1
def dictionary_of_metrics(items):
    # your code here
    number = len(items)
    sorted_list = sorted(items)
    median = np.median(sorted_list)
    mean = sum(items)/number
    variance = sum((item - mean)**2 for item in items) / (number - 1)
    standard_deviation = variance ** (1/2)
    minimum = min(items)
    maximum = max(items)
    dictionary = {'mean': round(mean,2),'median': median,'var': round(variance,2),'std': round(standard_deviation,2),'min': minimum,'max': maximum}
    return(dictionary)

### END FUNCTION

### START FUNCTION 2
def five_num_summary(items):
    # your code here
    
    number = len(items)
    sorted_list = sorted(items)
    median = np.median(sorted_list)
    Quarter_1 = np.quantile(sorted_list,0.25,interpolation = 'linear')
    Quarter_3 = np.quantile(sorted_list,0.75,interpolation = 'linear')
    minimum = min(items)
    maximum = max(items)
    dictionary = {'max': maximum,'median': median,'min': minimum,'q1': Quarter_1,'q3': Quarter_3}
    return(dictionary)

### END FUNCTION