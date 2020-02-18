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

### START FUNCTION
def stop_words_remover(df):
    
    # your code here
    stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', "in", "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together']}
    second_dict = {'option' :['please','in','of']}

    
    df['Without Stop Words'] = df['Tweets'].apply(str.split)

    for ref in range(len(twitter_df)):
        df['Without Stop Words'][ref] = [trial.lower() for trial in df['Without Stop Words'][ref] if trial not in stop_words_dict['stopwords']]
        df['Without Stop Words'][ref] = [option.lower() for option in df['Without Stop Words'][ref] if option not in second_dict['option']]
       
    return(df)

### END FUNCTION