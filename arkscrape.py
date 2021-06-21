import os
import pandas
import json
from argparse import ArgumentParser
from dotenv import load_dotenv
from datetime import datetime

def today():

    return "{0}_{1}_{2}".format(
        datetime.now().date().year,
        datetime.now().date().month,
        datetime.now().date().day
        )

def first_run():
    archive_folder = input("Name for Archive Folder: ")
    shodan_key = os.getenv('SHODAN_API')

    if os.path.isdir('cases') == True:
        pass
    else:
        os.mkdir('cases')

    os.mkdir('cases/{}'.format(archive_folder))

    print("=== ARCHIVE SETUP ===")
    os.system("cd cases/{} && archivebox init --setup && archivebox config --set SAVE_ARCHIVE_DOT_ORG=false".format(archive_folder))

    os.system("cd ../../")

    print("=== SHODAN SETUP ===")
    os.system("shodan init {}".format(shodan_key))
    #
    # print("=== ENSURE GOBUSTER IS INSTALLED ON THE SYSTEM TO USE SCRAPING FUNCTIONS ===")
    #
    # return "=== SETUP COMPLETED ==="

def start_archivebox(folder):


    print("=== Starting Server ===")
    if os.path.isdir("cases/{}".format(folder)):
        pass
    else:
        os.mkdir("cases/{}".format(folder))

        os.system("archivebox init --setup")

        os.system("archivebox config --set SAVE_ARCHIVE_DOT_ORG=false")

    os.chdir("cases/{}".format(folder))

    os.system("archivebox server")


def get_shodan(domain, folder='default'):

    if os.path.isdir("cases/{}/shodan".format(folder)):
        pass
    else:
        os.mkdir("cases/{}/shodan".format(folder))


    try:
        os.system("cd cases/{}/shodan && shodan download {}-export domain {}".format(folder, today(), domain))
    except Exception as e:

        print("Exception {}".format(e))

    return "shodan done"

def scrape_domain(domain, folder):

    if os.path.isdir('cases/{}/scrape'.format(folder)) is False:
        os.mkdir('cases/{}/scrape'.format(folder))

    os.system("gobuster dir -u {} -w big.txt > cases/{}/scrape/{}-{}-scrape.txt".format(domain, folder, today(), domain))

    os.system("gobuster dns -d {} -w big.txt > cases/{}/scrape/{}-{}-scrape-dns.txt".format(domain, folder, today(), domain))

def archive_site(url):


    os.system("archivebox ")


def main():

    load_dotenv()

    archive_folder=""

    parser = ArgumentParser(description="Archive websites and Shodan scan results per a domain")

    parser.add_argument('--init', help="First run setup", action='store_true')
    parser.add_argument('--shodan', help="Shodan check: --shodan <archive folder>")
    parser.add_argument('--server', help="Archive box server start: --server <archive folder>")
    parser.add_argument('--domain', help="Target domain")
    parser.add_argument('--scrape', help="Scrape Urls from a list: --scrape <archive folder>")

    args = parser.parse_args()
    setup = args.init
    shodan = args.shodan
    domain = args.domain
    archive_server = args.server
    _scrape = args.scrape

    if setup:
        print(first_run())
    if archive_server:
        start_archivebox(archive_server)

    if domain is not None:
        if shodan:
            get_shodan(domain, shodan)
        if _scrape is not None:
            scrape_domain(domain, _scrape)

main()
