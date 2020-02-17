
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



    def number_of_tweets_per_day(df):
    twitter_df['Dates'] = df['Date'].apply(lambda x : x.split(' ')[0])
    twitter_dfs = twitter_df.groupby(twitter_df['Dates']).count()
    
    return(twitter_dfs)

    def stop_words_http_remover(df):
    
    stop_words_dict = {'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 
                                    'nothing', 'thereupon', 'may', 'why', '’s', 'therefore', 'you', 'with', 
                                    'towards', 'make', 'really', 'few', 'former', 'during', 'mine', 'do', 
                                    'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 'seeming', 
                                    'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 
                                    'to', 'their', 'various', 'thereafter', '‘d', 'above', 'put', 'sometime', 
                                    'moreover', 'whoever', 'although', 'at', 'four', 'each', 'among', 'whatever', 
                                    'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 'was', 'almost', 
                                    'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', '’ve', 'might', 'see', 
                                    'whose', 'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 
                                    'is', 'except', 'up', 'take', 'became', 'however', 'many', 'thence', 'onto', '‘m', 
                                    'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 'becomes', 'alone', 'due', 
                                    'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
                                    'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 
                                    'whether', 'yet', 'nor', 'against', 'whereupon', 'top', 'first', 'three', 'show', 
                                    'per', 'five', 'two', 'ourselves', 'whenever', 'get', 'thereby', 'noone', 'had', 
                                    'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 'so', 'both', 
                                    'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', '’d', 'under', 
                                    'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 
                                    'bottom', 'call', 'n’t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 
                                    'anyway', 'how', 'the', 'all', 'much', 'another', 'since', 'hundred', 'serious', 
                                    '‘ve', 'ever', 'out', 'full', 'themselves', 'been', 'in', "'d", 'wherever', 'part', 
                                    'someone', 'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most', 
                                    'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
                                    'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', '’ll', 'latterly', 
                                    'are', 'ten', 'hers', 'should', 'they', '‘s', 'either', 'am', 'be', 'perhaps', '’re', 
                                    'only', 'namely', 'sixty', 'made', "'m", 'always', 'those', 'have', 'again', 'her', 
                                    'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 'sometimes', 'your', 'yours', 
                                    'that', 'around', 'his', 'indeed', 'mostly', 'cannot', '‘ll', 'too', 'seems', '’m', 
                                    'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 
                                    'somehow', 'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 
                                    'via', 'but', 'often', 're', 'our', 'because', 'rather', 'using', 'without', 'throughout', 
                                    'on', 'she', 'never', 'eight', 'no', 'hereupon', 'them', 'whereafter', 'quite', 'which', 
                                    'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'n‘t', 'him', 'could', 'front', 
                                    'within', '‘re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 'same', 'were', 
                                    'it', 'every', 'third', 'together']}

    df['Without Stop Words'] = df['Tweets'].apply(str.lower).apply(str.split)

    for i in range(len(twitter_df)):
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if x not in stop_words_dict['stopwords']]
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if "http" not in x]
        
        return(df)