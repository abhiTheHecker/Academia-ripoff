import argparse
from getpass import getpass
from pprint import pprint

from web import get_data, get_token

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, help="SRM netID username")

parser.add_argument("--password", type=str,
                    help="SRM password, leave blank for secure password entry")
args = parser.parse_args()
username = args.username

if not username:
    print("Enter a username and continue")
    exit()

if not args.password:
    password = getpass()
else:
    password = args.password


token = get_token(username=username, password=password)
data = get_data(token_dict=token)

pprint(data)

# TODO: Account for errors such as 404, 302, 500, etc.
