Create auth token
===================

Signup for loltel and get your token at https://docs.loltelapi.com/#authentication-tokens


Set environmanet variables
==========================

```bash
echo "export LOLTEL_ACCESS_TOKEN='YOUR_API_KEY'" > loltel.env
echo "export LOLTEL_MSISDN='MSISDN'" >> loltel.env
source ./loltel.env  # or . ./loltel.env
```


Usage
======

Import the loltel module and construct a client object.::

```python
import loltel


client = loltel.Client()
```


```python
response = client.sms_send(message='Goodbye, GSM!', to='47XXXXXXXX')
print response
```

