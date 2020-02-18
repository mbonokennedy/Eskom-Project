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

### START FUNCTION 3
### Updated the function as per request
def date_parser(dates):
    # your code here
    
    new_list = (dates[0:10] for dates in dates)
    answer = list(new_list)
    return(answer)

### END FUNCTION