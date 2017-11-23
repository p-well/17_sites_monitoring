from datetime import date, datetime
import os
import argparse
import requests
import whois


def return_args():
    parser = argparse.ArgumentParser(prog='Site Heath Check Program.')
    parser.add_argument('filepath',
                        help='Path to file with URLs list', type=str)
    args = parser.parse_args()
    return args


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
    domain_expiration_dt = whois.whois(url).expiration_date
    if isinstance(domain_expiration_dt, datetime):
        return domain_expiration_dt
    elif isinstance(domain_expiration_dt, list):
        return domain_expiration_dt[0]
    else:
        return None


def print_resource_health_data(url, status_code=None,
                               expiration_date=None,
                               remaining_days=None,
                               valid_urls=None,
                               invalid_urls=None):
    if status_code == 200:
        print("\nResource: {} | Status Code: {} | Available until: {}"
              .format(url, status_code, expiration_date))
    else:
        print('\nResource %s FAILED with status code %s' % (url, status_code))
    if remaining_days < 30:
        print('Warning! Domain name will expire in %s days' % remaining_days)


if __name__ == '__main__':
    urls_for_check = load_urls4check(return_args().filepath)
    if urls_for_check.get('valid'):
        for url in urls_for_check['valid']:
            response_code = get_server_response_code(url)
            exp_date_raw = get_domain_expiration_date(url)
            remaining_days = (exp_date_raw.date() - date.today()).days
            exp_date_formatted = datetime.strftime(exp_date_raw, '%d-%m-%Y')
            print_resource_health_data(url, response_code,
                                       exp_date_formatted,
                                       remaining_days)
    if urls_for_check.get('invalid'):
        print('\n\nThe following items are not checked. Specify protocop \
and try again.\n')
        for url in urls_for_check['invalid']:
            print(url)
