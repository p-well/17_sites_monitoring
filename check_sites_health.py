import argparse
#import requests
import chardet
import os

def return_arg():
    parser = argparse.ArgumentParser(prog = 'Site Heath Check Program.',
                                     description = 'Console utility for checking resource responce and domain payment.')
    parser.add_argument('filepath', help = 'Path to file containing URLs list', type = str)
    args = parser.parse_args()
    return args

def define_charset(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath,'rb') as ulrs_list_file:
        file_charset = chardet.detect(ulrs_list_file.read()).get('encoding')
    return file_charset

def load_urls4check(filepath, charset):
    all_urls_data = []
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = charset) as file_content:
        #return file_content.read().splitlines()
        print(file_content.read().splitlines())
    
def get_server_response(url):
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



if __name__ == '__main__':
    #path = return_arg().filepath

    load_urls4check(return_arg().filepath, define_charset(return_arg().filepath))


        #     url = line.replace('\n','')
        #     url_info = {}
        #     url_info['url'] = url
        #     url_info['status_code'] = None
        #     url_info['reason_phrase'] = None
        #     url_info['payment'] = None
        #     all_urls_data.append(url_info)
        # print(all_urls_data) 
    #return opened_urls_list
