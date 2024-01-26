import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import argparse
from bs4 import BeautifulSoup
from colorama import init , Style, Back,Fore
import tldextract

parser = argparse.ArgumentParser(description="Website Exifmeta data perser")

parser.add_argument('-d','--domain',
                            help = "Enter Domain Name only e,g uber, careem, yahoo",
                            type = str,
                            required = True)

args = parser.parse_args()


def certsh(_company_):

        result = []
        api_url = "https://crt.sh/?q={}".format(_company_)
        req = requests.get(api_url)
        if req.status_code == 200:
                soup = BeautifulSoup(req.content, 'lxml')
                tds = soup.find_all('tr')
                for td in tds:
                        xd = td.get_text()
                        xf = xd.split("\n")
                        try:
                                x = (xf[5]).strip()
                                print(x)
                        except:
                                pass

        return result

def main ():

        hehe = []
        domains = certsh(args.domain)
        for domain in domains:
                if domain not in hehe:
                        hehe.append(domain)

        for dom in hehe:
                print(dom)

main()
