import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/electrification_by_province.csv'
ebp = pd.read_csv(url)

for col, row in ebp.iloc[:,1:].iteritems():
    ebp[col] = ebp[col].str.replace(',','').astype(int)

limpopo = ebp['Limpopo'].to_list()
limpopo = [float(x) for x in limpopo]

mpumalanga = ebp['Mpumalanga'].to_list()
mpumalanga = [float(x) for x in mpumalanga]

north_west = ebp['North west'].to_list()
north_west = [float(x) for x in north_west]

free_state = ebp['Free State'].to_list()
free_state = [float(x) for x in free_state]

kwazulu_natal = ebp['Kwazulu Natal'].to_list()
kwazulu_natal = [float(x) for x in kwazulu_natal]

eastern_cape = ebp['Eastern Cape'].to_list()
eastern_cape = [float(x) for x in eastern_cape]

western_cape = ebp['Western Cape'].to_list()
western_cape = [float(x) for x in western_cape]

northern_cape = ebp['Northern Cape'].to_list()
northern_cape = [float(x) for x in northern_cape]

gauteng = ebp['Gauteng'].to_list()
gauteng = [float(x) for x in gauteng]

url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv'
twitter_df = pd.read_csv(url)

dates = twitter_df['Date'].to_list()


# In[11]:

## Function 1
def dictionary_of_metrics(items):

  ### Code Here
        number = len(items)
        sorted_list = sorted(items)
        median = np.median(sorted_list)
        mean = sum(items)/number
        ## Updated Variance formula because np.var does not work
        variance = sum((item - mean)**2 for item in items) / (number - 1)
        standard_deviation = variance ** (1/2)
        minimum = min(items)
        maximum = max(items)
        dictionary = {'mean': round(mean,2),'median': median,'var': round(variance,2),'std': round(standard_deviation,2),'min': minimum,'max': maximum}
        return(dictionary)


# In[12]:


dictionary_of_metrics(gauteng)


# In[15]:

## Function 2
def five_num_summary(items):

  ### Code Here
    number = len(items)
    sorted_list = sorted(items)
    median = np.median(sorted_list)
    ## Changed your interpolation to be more accurate
    Quarter_1 = np.quantile(sorted_list,0.25,interpolation = 'linear')
    Quarter_3 = np.quantile(sorted_list,0.75,interpolation = 'linear')
    minimum = min(items)
    maximum = max(items)
    dictionary = {'max': maximum,'median': median,'min': minimum,'q1': Quarter_1,'q3': Quarter_3}
    return(dictionary)