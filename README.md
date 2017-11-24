# Sites Monitoring Utility

This scripts helps you to check website "health" by 2 features:
- HTTP status code 
- Domain name expiration days left

Based on [Requests](https://docs.python-requests.org/en/master) and [python-whois](https://pypi.python.org/pypi/python-whois) libraries.

Pavel Kadantsev, 2017. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment.


# Usage

To execute the script run the command ```python check_sites_health.py <arguments>``` in your OS console/terminal.


# Example of Scripts Launch

```
>python check_sites_health.py .\urls.txt

Resource: https://stackoverflow.com/ | Status Code: 200 | Available until: 02-02-2018

Resource http://imwerden.de/cat/modules.php is OK but expiration date in not available!

Resource: https://tesla.com | Status Code: 200 | Available until: 03-11-2018

Resource: https://python.org | Status Code: 200 | Available until: 28-03-2018

Resource: https://devman.org | Status Code: 200 | Available until: 28-08-2018

Resource https://www.amazon.com FAILED with status code 503

Resource: https://www.tinkoff.ru/ | Status Code: 200 | Available until: 31-08-2018

Resource: http://keratin.su/ | Status Code: 200 | Available until: 23-04-2018

Resource: http://www.boeing.com/ | Status Code: 200 | Available until: 01-09-2022

Resource: http://www.moscowpython.ru/ | Status Code: 200 | Available until: 20-04-2018


The following items are not checked. Specify protocop and try again.

drive2.ru
pythonworld.ru
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)