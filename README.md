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

To execute the script run the command ```python check_sites_health.py <filepath>``` in your OS console/terminal.

The only argument you need to specify is the path to ```.txt``` file with list of websites you want to check. <br />
Place each URL in your list on a new string.

Script will reject URLs without specified protocol - see example below.

# Example of Scripts Launch

<pre>
<b>>python check_sites_health.py .\urls.txt</b>

---
Resource https://stackoverflow.com/ is OK
23 days until expiration!
---
Resource http://imwerden.de/cat/modules.php is OK
Cant get expiration date for current resource.
---
Resource https://tesla.com is OK
Available until 03-11-2018
---
Resource https://some-strange-url.com is down: not 200OK code or wrong URL
Cant get expiration date for current resource.
---
Resource https://python.org is OK
Available until 28-03-2018
---
Resource https://devman.org is OK
Available until 28-08-2018
---
Resource https://www.amazon.com is down: not 200OK code or wrong URL
Available until 31-10-2022
---
Resource https://www.tinkoff.ru/ is OK
Available until 31-08-2018
---
Resource http://keratin.su/ is OK
Available until 23-04-2018
---
Resource http://www.boeing.com/ is OK
Available until 01-09-2022
---
Resource http://www.moscowpython.ru/ is OK
Available until 20-04-2018


Items below are not checked. Specify protocol.

drive2.ru
pythonworld.ru
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
