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
    urls_list = []
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'utf-8') as file_content:
        for url_line in file_content:
            url = url_line.replace('\n','')
            opened_urls_list.append(url)
    print(opened_urls_list) 
    #return opened_urls_list
    
def is_server_respond_with_200(url):
    pass 
    

def get_domain_expiration_date(domain_name):
    pass

if __name__ == '__main__':
    #path = return_arg().filepath
    load_urls4check(return_arg().filepath)
    
    [{'url':'devman.org','code_200':'type_boolean_here', 'domain_payment > 1 month': 'type_boolean_here'}, {}, {}]
