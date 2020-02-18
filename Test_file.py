{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This is the Test File"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Financial Year (1 April - 30 March)</th>\n",
       "      <th>Limpopo</th>\n",
       "      <th>Mpumalanga</th>\n",
       "      <th>North west</th>\n",
       "      <th>Free State</th>\n",
       "      <th>Kwazulu Natal</th>\n",
       "      <th>Eastern Cape</th>\n",
       "      <th>Western Cape</th>\n",
       "      <th>Northern Cape</th>\n",
       "      <th>Gauteng</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>2000/1</td>\n",
       "      <td>51860</td>\n",
       "      <td>28365</td>\n",
       "      <td>48429</td>\n",
       "      <td>21293</td>\n",
       "      <td>63413</td>\n",
       "      <td>49008</td>\n",
       "      <td>48429</td>\n",
       "      <td>6168</td>\n",
       "      <td>39660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2001/2</td>\n",
       "      <td>68121</td>\n",
       "      <td>26303</td>\n",
       "      <td>38685</td>\n",
       "      <td>20928</td>\n",
       "      <td>64123</td>\n",
       "      <td>45773</td>\n",
       "      <td>38685</td>\n",
       "      <td>10359</td>\n",
       "      <td>36024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2002/3</td>\n",
       "      <td>49881</td>\n",
       "      <td>11976</td>\n",
       "      <td>28532</td>\n",
       "      <td>10316</td>\n",
       "      <td>63078</td>\n",
       "      <td>55748</td>\n",
       "      <td>28532</td>\n",
       "      <td>6869</td>\n",
       "      <td>32127</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2003/4</td>\n",
       "      <td>42034</td>\n",
       "      <td>33515</td>\n",
       "      <td>34027</td>\n",
       "      <td>16135</td>\n",
       "      <td>60282</td>\n",
       "      <td>47414</td>\n",
       "      <td>34027</td>\n",
       "      <td>10976</td>\n",
       "      <td>39488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>2004/5</td>\n",
       "      <td>54646</td>\n",
       "      <td>16218</td>\n",
       "      <td>21450</td>\n",
       "      <td>5668</td>\n",
       "      <td>37811</td>\n",
       "      <td>42041</td>\n",
       "      <td>21450</td>\n",
       "      <td>6316</td>\n",
       "      <td>18422</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Financial Year (1 April - 30 March)  Limpopo  Mpumalanga  North west  \\\n",
       "0                              2000/1    51860       28365       48429   \n",
       "1                              2001/2    68121       26303       38685   \n",
       "2                              2002/3    49881       11976       28532   \n",
       "3                              2003/4    42034       33515       34027   \n",
       "4                              2004/5    54646       16218       21450   \n",
       "\n",
       "   Free State  Kwazulu Natal  Eastern Cape  Western Cape  Northern Cape  \\\n",
       "0       21293          63413         49008         48429           6168   \n",
       "1       20928          64123         45773         38685          10359   \n",
       "2       10316          63078         55748         28532           6869   \n",
       "3       16135          60282         47414         34027          10976   \n",
       "4        5668          37811         42041         21450           6316   \n",
       "\n",
       "   Gauteng  \n",
       "0    39660  \n",
       "1    36024  \n",
       "2    32127  \n",
       "3    39488  \n",
       "4    18422  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'\n",
    "ebp_df = pd.read_csv(ebp_url)\n",
    "\n",
    "for col, row in ebp_df.iloc[:,1:].iteritems():\n",
    "    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)\n",
    "\n",
    "ebp_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tweets</th>\n",
       "      <th>Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>@BongaDlulane Please send an email to mediades...</td>\n",
       "      <td>2019-11-29 12:50:54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>@saucy_mamiie Pls log a call on 0860037566</td>\n",
       "      <td>2019-11-29 12:46:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>@BongaDlulane Query escalated to media desk.</td>\n",
       "      <td>2019-11-29 12:46:10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Before leaving the office this afternoon, head...</td>\n",
       "      <td>2019-11-29 12:33:36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...</td>\n",
       "      <td>2019-11-29 12:17:43</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Tweets                 Date\n",
       "0  @BongaDlulane Please send an email to mediades...  2019-11-29 12:50:54\n",
       "1         @saucy_mamiie Pls log a call on 0860037566  2019-11-29 12:46:53\n",
       "2       @BongaDlulane Query escalated to media desk.  2019-11-29 12:46:10\n",
       "3  Before leaving the office this afternoon, head...  2019-11-29 12:33:36\n",
       "4  #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...  2019-11-29 12:17:43"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'\n",
    "twitter_df = pd.read_csv(twitter_url)\n",
    "twitter_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# gauteng ebp data as a list\n",
    "gauteng = ebp_df['Gauteng'].astype(float).to_list()\n",
    "\n",
    "# dates for twitter tweets\n",
    "dates = twitter_df['Date'].to_list()\n",
    "\n",
    "# dictionary mapping official municipality twitter handles to the municipality name\n",
    "mun_dict = {\n",
    "    '@CityofCTAlerts' : 'Cape Town',\n",
    "    '@CityPowerJhb' : 'Johannesburg',\n",
    "    '@eThekwiniM' : 'eThekwini' ,\n",
    "    '@EMMInfo' : 'Ekurhuleni',\n",
    "    '@centlecutility' : 'Mangaung',\n",
    "    '@NMBmunicipality' : 'Nelson Mandela Bay',\n",
    "    '@CityTshwane' : 'Tshwane'\n",
    "}\n",
    "\n",
    "# dictionary of english stopwords\n",
    "stop_words_dict = {\n",
    "    'stopwords':[\n",
    "        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', \n",
    "        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', \n",
    "        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', \n",
    "        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', \n",
    "        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', \n",
    "        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', \n",
    "        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', \n",
    "        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', \n",
    "        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', \n",
    "        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', \n",
    "        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', \n",
    "        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', \n",
    "        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', \n",
    "        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', \n",
    "        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', \n",
    "        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', \n",
    "        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', \n",
    "        'been', 'in', \"'d\", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', \n",
    "        \"'s\", \"'re\", 'most', 'one', \"n't\", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', \n",
    "        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', \n",
    "        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', \n",
    "        'made', \"'m\", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', \n",
    "        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', \n",
    "        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', \n",
    "        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', \"'ve\", 'say', 'via', 'but', 'often', 're', 'our', \n",
    "        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', \n",
    "        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',\n",
    "        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', \n",
    "        'same', 'were', 'it', 'every', 'third', 'together'\n",
    "    ]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
