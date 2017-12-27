from datetime import date, datetime
from collections import namedtuple
import os
import argparse
import requests
import whois


def get_filepath():
    parser = argparse.ArgumentParser(prog='Site Heath Check Program.')
    parser.add_argument('filepath',
                        help='Path to file with URLs list', type=str)
    path = parser.parse_args()
    return path


def load_urls4check(filepath):
    valid_urls, invalid_urls = [], []
    urls = {}
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_content:
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


def get_domain_expiration_date(domain_name):
    try:
        exp_date = whois.whois(url).expiration_date
        if exp_date is not None and isinstance(exp_date, datetime):
            raw_exp_date = exp_date
        elif exp_date is not None and isinstance(exp_date, list):
            raw_exp_date = exp_date[0]
        else:
            raw_exp_date = None
        if raw_exp_date is not None:
            formatted_exp_date = datetime.strftime(raw_exp_date, '%d-%m-%Y')
            remaining_days = (raw_exp_date.date() - date.today()).days
            dates_template = namedtuple('domain_dates',
                                        'expiration_date remaining_days')
            domain_dates_info = dates_template(formatted_exp_date,
                                               remaining_days)
            return domain_dates_info
    except whois.parser.PywhoisError:
        return None


def print_resource_health_data(
                               url,
                               status_code=None,
                               domain_info=None,
                               ):
    if status_code == 200:
        print('Resource %s is OK' % url)
    elif status_code != 200 or status_code is None:
        print('Resource %s is down: not 200OK code or wrong URL ' % url)
    if domain_info:
        if domain_info.remaining_days > 30:
            print('Available until %s' % domain_info.expiration_date)
        else:
            print('%s days left until expiration!' % domain_info.remaining_days)
    else:
        print('Cant get expiration date for current resource')


if __name__ == '__main__':
    urls_for_check = load_urls4check(get_filepath().filepath)
    if urls_for_check.get('valid'):
        for url in urls_for_check.get('valid'):
            print('---')
            status_code = get_server_response_code(url)
            domain_info = get_domain_expiration_date(url)
            print_resource_health_data(url,
                                       status_code,
                                       domain_info)
    if urls_for_check.get('invalid'):
        print('\n\nItems below are not checked. Specify protocol and try again.\n')
        for url in urls_for_check['invalid']:
            print(url)
