# AssetFinder

A recon tool that uses [crt.sh](https://crt.sh) certificate transparency logs to discover domains and subdomains associated with a target.

## Features

- **AssetFinder.py** — Finds unique root domains associated with a target domain
- **AssetFinderSubdomains.py** — Finds all subdomains (including wildcards) for a target domain
- Handles crt.sh errors gracefully with clear error messages and retry guidance

## Installation

```bash
git clone https://github.com/hassankhan/AssetFinder.git
cd AssetFinder
pip3 install -r requirements.txt
```

### Requirements

- Python 3
- Dependencies (installed via requirements.txt):
  - requests
  - beautifulsoup4
  - lxml
  - colorama
  - tldextract
  - urllib3

## Usage

### Find root domains

```bash
python3 AssetFinder.py -d walmart.com
```

This will output all unique root domains found in certificate transparency logs for the target.

### Find subdomains

```bash
python3 AssetFinderSubdomains.py -d walmart.com
```

This will output all unique subdomains (e.g., `api.walmart.com`, `*.walmart.com`) found for the target.

## Troubleshooting

crt.sh can sometimes be slow or unresponsive. If you see an error message like:

```
[!] Error: Could not connect to crt.sh. The site may be down or unreachable.
[*] Please try running the tool again.
```

Simply wait a moment and re-run the command. This is a known issue with crt.sh being overloaded.

## Happy hunting :)
