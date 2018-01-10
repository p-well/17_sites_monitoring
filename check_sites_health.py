from datetime import date, datetime
from collections import namedtuple
from os.path import exists
import argparse
import requests
import whois

OK_STATUS_CODE = 200
DAYS_LIMIT = 30


def create_parser():
    parser = argparse.ArgumentParser(prog='Site Heath Check Program.')
    parser.add_argument('filepath', help='Path to URLs list file', type=str)
    return parser


def check_arguments(parser, args):
    if not exists(args.filepath):
        parser.error('File not found.')


def load_urls4check(filepath):
    valid_urls, invalid_urls = [], []
    urls = {}
    with open(filepath, 'r', encoding='utf-8') as file_content:
        for url in file_content.read().splitlines():
            if url.startswith('http'):
                valid_urls.append(url)
                urls['valid'] = valid_urls
            else:
                invalid_urls.append(url)
                urls['invalid'] = invalid_urls
        return urls


def fetch_server_response_code(url):
    try:
        return requests.get(url).status_code
    except requests.exceptions.RequestException:
        return None


def fetch_domain_expiration_date(domain_name):
    try:
        return whois.whois(url).expiration_date
    except whois.parser.PywhoisError:
        return None


def format_expiration_date(exp_date):
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


def check_resource_health(
        url,
        status_code,
        domain_info,
    ):
    if status_code == OK_STATUS_CODE:
        print('Resource %s is OK' % url)
    elif status_code != OK_STATUS_CODE or status_code is None:
        print('Resource %s is down: not 200OK code or wrong URL ' % url)
    if domain_info:
        if domain_info.remaining_days > DAYS_LIMIT:
            print('Available until %s' % domain_info.expiration_date)
        else:
            print('%s days until expiration!' % domain_info.remaining_days)
    else:
        print('Cant get expiration date for current resource.')


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    check_arguments(parser, args)
    urls_for_check = load_urls4check(args.filepath)
    if urls_for_check.get('valid'):
        for url in urls_for_check.get('valid'):
            print('---')
            status_code = fetch_server_response_code(url)
            exp_date = fetch_domain_expiration_date(url)
            domain_info = format_expiration_date(exp_date)
            check_resource_health(
                url,
                status_code,
                domain_info
            )
    if urls_for_check.get('invalid'):
        print('\n\nItems below are not checked. Specify protocol.\n')
        for url in urls_for_check['invalid']:
            print(url)
