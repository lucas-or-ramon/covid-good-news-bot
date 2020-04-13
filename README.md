<h1 align="center">
  <img alt="Logo - COVID-19 Good News Bot" src="./logo-covid-19-bot.png">
</h1>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8.2-brightgreen">
  <img alt="Twilio Sandbox" src="https://img.shields.io/badge/twilio-sandbox-brightgreen">
  <img alt="Whatsapp" src="https://img.shields.io/badge/messenger-whatsapp-brightgreen">
  <img alt="AWS Lambda" src="https://img.shields.io/badge/aws-lambda-brightgreen">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>

During this COVID-19 pandemic, we have been receiving a lot of bad news from all over
the world. How about receive directly on your Whatsapp one good news per day and try to forget
a little bit the other ones?

## Getting Started

This is a simple Python script to send a WhatsApp message using **News API** and **Twilio Sandbox**.  
To run it every day at a certain time, I added the code on the **AWS** (Amazon Web Services) cloud.

## Running this project  

Clone or download this repository and create your `secrets.py` file:

```python
#from https://newsapi.org/
news_org_api_key = 'XXXXXXXXXXXX'

#from https://www.twilio.com/
twilio_account_sid = 'XXXXXXXXXXXX'
twilio_auth_token = 'XXXXXXXXXXXX'

#contacts to receive messages
contact_dict = {'contact' 'whatsapp:+0000000000000'}
```

1. In `whatsapp.py` change the News API variables to get what you want - check News API
[documentation](https://newsapi.org/docs) for all options:

```python
news = newsapi.get_everything(q=key_word, #keywords to search
                              from_param=yesterday, #start date to start the search
                              to=today, #end date to the search
                              language='pt', #news' language i.e. 'en' = English, 'es' = Spanish
                              sort_by='relevancy',
                              page=1)
```

2. Change the `send_good_news function` with your Twilio Sandbox number: `from_='whatsapp:+14155238886'`.
Check Twilio's [documentation](https://www.twilio.com/docs/whatsapp/api) for more information.

3. Change the list of good news with the words you find relevant.

4. Now, unzip the `aws-lambda-deployment.zip` folder, update the files changed, and zip the folder again.

## Deployment

To run the script everyday, I added the script to **AWS Lambda Services**. To do that, I uploaded the
zipped filder with all files and dependencies to AWS and created a **Cloud Watch Event** to trigger.
Read more about lambda functions [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html).

## Built using

- [Python 3.8.2](https://www.python.org/)
- [News API](https://newsapi.org/)
- [Twilio](https://www.twilio.com/)
- [AWS Lambda](https://us-east-2.console.aws.amazon.com/lambda/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Inspiration**: [I Wrote a Script to WhatsApp My Parents Every Morning in Just 20 Lines of Python Code](https://medium.com/better-programming/i-wrote-a-script-to-whatsapp-my-parents-every-morning-in-just-20-lines-of-python-code-5d203c3b36c1)
