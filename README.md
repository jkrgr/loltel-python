Create auth token
===================

Signup for loltel and get your token at https://docs.loltelapi.com/#authentication-tokens


Set environmanet variable
==========================

```bash
echo "export LOLTEL_ACCESS_TOKEN='YOUR_API_KEY'" > loltel.env
echo "export LOLTEL_MSISDN='MSISDN'" >> loltel.env
echo "loltel.env" >> .gitignore
source ./loltel.env  ## or . ./loltel.env
```


Usage
======

Import the loltel module and construct a client object.::

```python
import loltel


client = loltel.Client()
```


```python
response = client.send_message({'from': 'Python', 'to': 'YOUR-NUMBER', 'text': 'Hello world'})

response = response['messages'][0]

if response['status'] == '0':
  print 'Sent message', response['message-id']

  print 'Remaining balance is', response['remaining-balance']
else:
  print 'Error:', response['error-text']

```

