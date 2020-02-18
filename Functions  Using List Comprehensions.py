
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

def dictionary_of_metrics(items):

  ### Code Here
        number = len(items)
        sorted_list = sorted(items)
        median = np.median(sorted_list)
        mean = sum(items)/number
        variance = np.var(sorted_list)
        standard_deviation = variance ** (1/2)
        minimum = min(items)
        maximum = max(items)
        dictionary = {'mean': round(mean,2),'median': median,'variance': round(variance,2),'standard deviation': round(standard_deviation,2),'min': minimum,'max': maximum}
        return(dictionary)

def five_num_summ(items):

  ### Code Here
    number = len(items)
    sorted_list = sorted(items)
    median = np.median(sorted_list)
    Quarter_1 = np.quantile(sorted_list,0.25,interpolation = 'lower')
    Quarter_3 = np.quantile(sorted_list,0.75,interpolation = 'lower')
    minimum = min(items)
    maximum = max(items)
    dictionary = {'max': maximum,'median': median,'min': minimum,'q1': Quarter_1,'q3': Quarter_3}
    return(dictionary)
    

def date_parser(list_dates):

  ### Code Here
    new_list = (dates[0:10] for dates in list_dates)
    answer = list(new_list)
    return(answer)

dates = ['2019-11-29 12:50:54',
         '2019-11-29 12:46:53',
         '2019-11-29 12:46:10',
         '2019-11-29 14:33:36',
         '2019-11-29 12:17:43',
         '2019-11-29 11:28:40']


def extract_municipality_hashtags(df):
    search = twitter_df["Tweets"].str.split()
    #solution = twitter_df["Tweets"].apply(lambda df: [municipality_dict[key] if key in list(municipality_dict.keys()) else np.nan for key in search])
    solution = twitter_df["Tweets"].apply(lambda df: [municipality_dict[key] for key in search if key in list(municipality_dict.keys())]).head(10)
    return(solution)


#FUNCTION 5
def number_of_tweets_per_day(df):
    twitter_df['Dates'] = df['Date'].apply(lambda x : x.split(' ')[0])
    twitter_dfs = twitter_df.groupby(twitter_df['Dates']).count()
    
    return(twitter_dfs)

#FUNCTION 6
def word_spliter(df):

    df['Split_Tweets']=df["Tweets"].str.lower() 
    df["Split_Tweets"]=df["Split_Tweets"].str.split()
    
    return(df)