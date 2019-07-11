from intuginehelper import intudb
import argparse
from subprocess import call


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', dest='start', help="Start date of generating the report in (DD/MM/YYYY)")
    parser.add_argument('-e', '--end', dest='end', help="End date of generating the report in (DD/MM/YYYY)")
    parser.add_argument('-t', '--type', dest='type', help="Billing type TRIPDAYS / TRIPPINGS")
    parser.add_argument('-o', '--output', dest='output', help="Output File Name")
    parser.add_argument('-u', '--username', dest='username', help="User Name")
    parser.add_argument('-c', '--client', dest='client', help="Client Name")
    parser.add_argument('-d', '--dir', dest='dir', help="Output Directory")
    parser.add_argument('-q', '--query', dest='query', help="Query")
    return parser.parse_args()


if __name__ == '__main__':
    options = get_args()
    all_users = set()
    for user in intudb.get_all_users():
        if 'config' in user.keys():
            config = user['config']
            if 'client' in config.keys():
                all_users.add(config['client'])
                continue
        all_users.add(user['username'])
    for user in all_users:
        print(user)
    # exit(0)
    call(['mkdir', 'all_users'])
    for user in all_users:
        call(['python3', 'main.py', '--dir=all_users', '-u={}'.format(user), '-s={}'.format(options.start),
              '-e={}'.format(options.end), '-o={}'.format(user)])
