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

### START FUNCTION 3
def date_parser(dates):
    # your code here
    
    new_list = (dates[0:10] for dates in dates)
    answer = list(new_list)
    return(answer)

### END FUNCTION

### START FUNCTION 4
def extract_municipality_hashtags(df):
    # your code here
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane'}
    
    
    df["municipality"] = df["Tweets"].apply(lambda df: ''.join([municipality_dict[key] for key in df.split() if key in municipality_dict.keys()]))
    df["hashtags"] = df["Tweets"].apply(lambda df: [word.lower() for word in df.split() if word[0]=='#'])
    df['municipality'] = df['municipality'].apply(lambda y: np.nan if len(y) == 0 else y)
    df['hashtags'] = df['hashtags'].apply(lambda y: np.nan if len(y) == 0 else y)

    return df

### END FUNCTION

### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
    #Write into a column  called dates and split the time and date
    df['Date'] = df['Date'].apply(lambda ref : ref.split(' ')[0])
    #Drop both columns
    trial = df.drop(columns=['Date'],axis = 1)
    #Count the number of tweets per date
    twitter_dfs = trial.groupby(df['Date']).count()
    
    return(twitter_dfs)#.iloc[])

### END FUNCTION

### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
    #Write into a column  called dates and split the time and date
    df['Date'] = df['Date'].apply(lambda ref : ref.split(' ')[0])
    #Drop both columns
    trial = df.drop(columns=['Date'],axis = 1)
    #Count the number of tweets per date
    twitter_dfs = trial.groupby(df['Date']).count()
    
    return(twitter_dfs)#.iloc[])

### END FUNCTION

### START FUNCTION
def word_splitter(df):
    # your code here
    #Copy the tweets in the column Tweets to Split_Tweets and make them lower case
    df['Split Tweets']=df['Tweets'].str.lower() 
    #Split the tweets in Split_Tweets 
    df['Split Tweets']=df['Split Tweets'].str.split()
    
    return(df)

### END FUNCTION