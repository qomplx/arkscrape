
# **arkscrape**
---

# Description

A tool to archive, identify, and enumerate different webapplications
and devices that are pertinent to investigations.

This tool, subsequent tools, are to be used ethically and we are not
responsible for any legal rammifications surrounding individuals using
this toolset.

# Requirements

* archivebox (https://github.com/ArchiveBox/ArchiveBox)
* gobuster (https://github.com/OJ/gobuster)
* Python3.9 (https://www.python.org/downloads/)
* pip (https://pip.pypa.io/en/stable/installing/)


# Installation

`$ pip install -r requirements.txt`

`$ python3 arkscrape.py --help`

# Usage

```
usage: arkscrape.py [-h] [--init] [--shodan SHODAN] [--server SERVER] [--domain DOMAIN]
                    [--scrape SCRAPE]

Archive websites, Shodan scan results, and webscraper per a domain

optional arguments:
  -h, --help       show this help message and exit
  --init           First run setup
  --shodan SHODAN  Shodan check: --shodan <archive folder>
  --server SERVER  Archive box server start: --server <archive folder>
  --domain DOMAIN  Target domain
  --scrape SCRAPE  Scrape Urls from a list: --scrape <archive folder>

```

## Archivebox

```
$ python3 --server <folder>

follow any of the other prompts to setup the archivebox
within that folder.

```

## Shodan

```
cp .env.example .env
```
__=== EDIT .env WITH YOUR SHODAN API KEY ===__

```
$ python3 --shodan <folder> --domain <domain/url>

```

## Gobuster

```
$ python3 --scrape <folder>  --domain <domain/url>
```
