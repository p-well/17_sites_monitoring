from datetime import date, datetime
import os
import argparse
import requests
import chardet
import whois


def return_args():
    parser = argparse.ArgumentParser(prog = 'Site Heath Check Program.')
    parser.add_argument('filepath', \
                        help = 'Path to file with URLs list', type = str)
    args = parser.parse_args()
    return args

    
def define_charset(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath,'rb') as ulrs_list_file:
        file_charset = chardet.detect(ulrs_list_file.read()).get('encoding')
    return file_charset

    
def load_urls4check(filepath, charset='utf-8'):
    valid_urls, invalid_urls = [], []
    urls = {}
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding=charset) as file_content:
        for url in file_content.read().splitlines():
            if url.startswith('http'):
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
    if isinstance(domain_expiration_dt, datetime):
        return domain_expiration_dt
    elif isinstance(domain_expiration_dt, list):
        return domain_expiration_dt[0]
    else:
        return None
 
 
if __name__ == '__main__':
    urls_from_file = load_urls4check(return_args().filepath,
                                     define_charset(return_args().filepath))
    if urls_from_file:
        for count, url in enumerate(urls_from_file['valid'], start=1):
            response_code = get_server_response_code(url)
            exp_date_raw = check_domain_expiration_date(url)
            days_till_expiration = (exp_date_raw.date() - date.today())
            exp_date_formated = datetime.strftime(exp_date_raw, '%d-%m-%Y')
            
            print('{}. Resource: {} \n   Status code: {} \n   Expiration date: {} \n   Remaing time: {} days \n'
                 .format(count, url, response_code, expiration_date, days_till_expiration.days))
            if days_till_expiration.days < 30:
                print('Warning! Domain name will expire soon.')
        if urls_from_file['invalid']:
            print('The follwing items have not been checked. Specify protocop in URL and try again.')
            for count, url in enumerate(urls_from_file['invalid'], start=1):
                print({}. {}).format(count, url)
    else:
print('\nNo valid URLs or empty file')



def collect_resource_info(url, status_code=None,
                          expiration_date = None
                          remaining_days=None):
    if status_code == 200:
        print("""Resource: {} Status Code: {},  
    
    """)
    



if __name__ == '__main__':
    urls_from_file = load_urls4check(return_args().filepath,
                                     define_charset(return_args().filepath))
    if urls_from_file['valid']:
        for url in urls_from_file:
