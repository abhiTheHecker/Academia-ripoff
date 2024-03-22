import argparse
from getpass import getpass
from pprint import pprint

from web import get_data, get_token

"""This is the CLI for the Academia ripoff. It will provide all the obtainable details of a student in json/dictionary format"""

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, help="SRM netID username")

parser.add_argument("--password", type=str,
                    help="SRM password, leave blank for secure password entry")

parser.add_argument("--output", help="Outputs the data into a file", type=str)

parser.add_argument(
    "--json", choices=[0, 1], type=int, help="Enter 1 to output it as json")
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

if args.json:
    import json
    with open(args.output, mode="w", encoding='utf-8') as file:
        json.dump(data, file)

else:
    if args.output:
        with open(args.output, mode="w", encoding='utf-8') as file:
            file.write(str(data))


# TODO: Account for errors such as 404, 302, 500, etc.
# TODO: Web Interface and database models.
