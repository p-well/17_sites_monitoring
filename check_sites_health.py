from datetime import datetime
import argparse
#import requests
#import chardet
#import whois
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
            if re.compile('http').match(url) is not None:
                valid_urls.append(url)
                urls['valid'] = valid_urls 
            else:
                invalid_urls.append(url)
                urls['invalid'] = invalid_urls
        #return urls
        print(urls)
        if urls is True:
            print('Yes')
        else:
            print('False')
def get_server_response_code(url):
    try:
        response_code = requests.get(url).status_code
        return response_code
    except requests.exceptions.RequestException:
        return None

def check_domain_expiration_date(domain_name):
    domain_expiration_dt = whois.whois(url).expiration_date
    if type(domain_expiration_dt) == datetime:
        return domain_expiration_dt.date() 
    elif type(domain_expiration_dt) == list:
        return domain_expiration_dt[0].date()
    else:
        return None
        
#remainig_subscription_days = (domain_expiration_dt[0] - datetime.now()).date()

if __name__ == '__main__':
    load_urls4check(return_args().filepath)
    
#if __name__ == '__main__':
#    urls_loaded_from_file = load_urls4check(return_args().filepath,
#                                            define_charset(return_args().filepath))
#    if urls_loaded_from_file: 
#       for url in urls_loaded_from_file['valid']:
#           responce_code = get_server_response_code(url)
#           expiration_date = check_domain_expiration_date(url)
#           days_till_expiration = expiration_date - datetime.now()).date() 
#               
#    else:
#       print('No valid URLs or empty file')    
