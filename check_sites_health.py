from datetime import date, datetime 
import argparse
import requests
import chardet
import whois
import os
import re

def return_args():
    parser = argparse.ArgumentParser(prog = 'Site Heath Check Program.',
                                     description = 'Console utility for checking URL resource responce code and domain expiration date.')
    parser.add_argument('filepath', help = 'Path to file containing URLs list', type = str)
    args = parser.parse_args()
    return args

def define_charset(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath,'rb') as ulrs_list_file:
        file_charset = chardet.detect(ulrs_list_file.read()).get('encoding')
    return file_charset

def load_urls4check(filepath, charset = 'utf-8'):
    valid_urls, invalid_urls = [], []
    urls = {}
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = charset) as file_content:
        for url in file_content.read().splitlines():
            if match(r'http',url) is not None:
                valid_urls.append(url)
                urls['valid'] = valid_urls 
            else:
                invalid_urls.append(url)
                urls['invalid'] = invalid_urls
        return urls
        
def get_server_response_code(url):
    try:
        response_code = requests.get(url).status_code
        return response_code
    except requests.exceptions.RequestException:
        return None

def check_domain_expiration_date(domain_name):
    domain_expiration_dt = whois.whois(url).expiration_date
    if type(domain_expiration_dt) == datetime:
        return domain_expiration_dt
    elif type(domain_expiration_dt) == list:
        return domain_expiration_dt[0]
    else:
        return None
    
if __name__ == '__main__':
    urls_loaded_from_file = load_urls4check(return_args().filepath,
                                           define_charset(return_args().filepath))
    if urls_loaded_from_file: 
        for count, url in enumerate(urls_loaded_from_file['valid'], start = 1):
            responce_code = get_server_response_code(url)
            expiration_date_raw = check_domain_expiration_date(url)
            expiration_date = datetime.strftime(expiration_date_raw, '%d-%m-%Y') 
            days_till_expiration = (expiration_date_raw.date() - date.today())
            print('{}. Resource: {} \n   Status code: {} \n   Expiration date: {} \n   Remaing time: {} days \n'
                 .format(count, url, responce_code, expiration_date, days_till_expiration.days))
            if days_till_expiration.days < 30:
                print('Warning! Domain expiration date is coming soon.')
        if urls_loaded_from_file['invalid']:
            print('The follwing items have not been checked. Specify protocop in URL and try again.')
            for count, url in enumerate(urls_loaded_from_file['invalid'], start = 1):
                print({}. {}).format(count, url)
    else:
        print('\nNo valid URLs or empty file')
