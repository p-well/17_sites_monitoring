import argparse
#import requests
#import chardet
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
    with open(filepath,'rb') as file_with_unknown_charset:
        file_charset = chardet.detect(file_with_unkwown_charset.read()).get('encoding')
    return file_charset

def load_urls4check(filepath):
    all_urls_data = []
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'utf-8') as file_content:
        for line in file_content:
            url = line.replace('\n','')
            url_info = {}
            url_info['url'] = url
            url_info['status_code'] = None
            url_info['reason_phrase'] = None
            url_info['payment'] = None
            all_urls_data.append(url_info)
        print(all_urls_data) 
    #return opened_urls_list
    
def is_server_respond_with_200(url):
    for url_info in load_urls4check(filepath):
        
    
    pass 
    

def get_domain_expiration_date(domain_name):
    pass

if __name__ == '__main__':
    #path = return_arg().filepath
    load_urls4check(return_arg().filepath)
    
    #[{'url':'devman.org','code_200':'type_boolean_here', 'domain_payment > 1 month': 'type_boolean_here'}, {}, {}]
    
