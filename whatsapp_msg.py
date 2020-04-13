#import libraries
from newsapi import NewsApiClient
import datetime
from twilio.rest import Client
from secrets import *

def send_good_news(event=None, context=None):
    '''
    Uses a dictionary of contacts (name: number) to send the composed message using
    Twilio's API.

    Params:
    message: str. The message to be sent

    Return:
    The Twilio SID.
    '''

    def get_news (news_org_api_key, key_word):
        '''
        Search through millions of articles from over 30,000 large and small news sources and blogs
        from https://newsapi.org/ and return a dictionary with 'Everything news' endpoint
        from the last 24 hours from Brazil with a certain keyword.

        Params:
        - api_key: str. Your API key from newsapi.org.
        - key_word: str. Key word from the news piece you want to retreive.

        Return:
        JSON response as nested Python dictionary.
        '''
        #init with API
        newsapi = NewsApiClient(api_key=news_org_api_key)

        #get dates
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        #get news
        news = newsapi.get_everything(q=key_word,
                                      from_param=yesterday,
                                      to=today,
                                      language='pt',
                                      sort_by='relevancy',
                                      page=1)

        return news

    #get news
    news = get_news (news_org_api_key, 'covid')

    #good words bow
    positive_words = ['bom', 'boa', 'bons', 'boas', 'feliz', 'felizes', 'positiva', 'alegre', 'alegria', 'amor', 'esperança',
                      'doar', 'doação', 'doam', 'doa', 'melhora', 'melhor', 'aplauso', 'aplausos', 'exemplo']

    def filter_news(news_dict, words_list):
        '''
        Filter the descriptions of the dictionary returned from https://newsapi.org/
        using a list of targeted words.

        Params:
        - news_dict: dict. The result dictionary from News API.
        - words_list: list. The list with strings to filter news.

        Return:
        A list only with news that have the words in words_list in their description.
        '''
        filtered_news = []

        for i in range(len(news['articles'])):
            for key, value in news['articles'][i].items():
                if key == 'description':
                    if any(word in value for word in words_list):
                        filtered_news.append(news['articles'][i])

        return filtered_news

    filter_news = filter_news(news, positive_words)

    def compose_message(filter_news):
        '''
        If there is at least one good news, it composes message with the title and url of the news piece.
        If no news was filtered that day, it return a standard message.

        Params:
        filter_news = list. The list with all the good news.

        Result:
        str. A message to be sent through Twilio.
        '''

        if len(filter_news) > 0:
            message = ''.join(['Bom dia! Aqui está sua boa notícia do dia: ' +
                               filter_news[0]['title'] + ' | ' + filter_news[0]['url']])
        else:
            message = 'Bom dia! Desculpa, hoje não achei uma notícia!'

        return message

    message = compose_message(filter_news)

    #access info from Twilio
    account_sid = twilio_account_sid
    auth_token = twilio_auth_token

    whatsapp_client = Client(account_sid, auth_token)

    contacts = contact_dict

    for key, value in contacts.items():
        good_news = whatsapp_client.messages.create(
            to=value,
            from_='whatsapp:+14155238886',
            body=message)

            print(good_news.sid)
