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
        manual_url = "https://crt.sh/?q=%25{}%25".format(_company_)
        try:
                req = requests.get(api_url, timeout=30)
        except requests.exceptions.ConnectionError:
                print(Fore.RED + "[!] Error: Could not connect to crt.sh. The site may be down or unreachable." + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                return result
        except requests.exceptions.Timeout:
                print(Fore.RED + "[!] Error: Connection to crt.sh timed out." + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                return result
        except requests.exceptions.RequestException as e:
                print(Fore.RED + "[!] Error: Request to crt.sh failed: {}".format(e) + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                return result

        if req.status_code != 200:
                print(Fore.RED + "[!] Error: crt.sh returned status code {} — the site may be experiencing issues.".format(req.status_code) + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                return result

        try:
                soup = BeautifulSoup(req.content, 'lxml')
                tds = soup.find_all('tr')
                if not tds:
                        print(Fore.YELLOW + "[!] Warning: crt.sh returned an empty response. The site may be overloaded." + Style.RESET_ALL)
                        print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                        return result
                for td in tds:
                        xd = td.get_text()
                        xf = xd.split("\n")
                        try:
                                x = (xf[5]).strip()
                                if "Logged At" not in x:
                                        result.append(x)
                        except Exception:
                                pass
        except Exception as e:
                print(Fore.RED + "[!] Error: Failed to parse crt.sh response: {}".format(e) + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)

        return result

def main ():

        hehe = []
        domains = certsh(args.domain)
        for domain in domains:
                if domain not in hehe:
                        hehe.append(domain)

        if not hehe:
                manual_url = "https://crt.sh/?q=%25{}%25".format(args.domain)
                print(Fore.YELLOW + "[!] No subdomains found for '{}'. This could be a crt.sh issue.".format(args.domain) + Style.RESET_ALL)
                print(Fore.YELLOW + "[*] Please try running the tool again or manually query: " + manual_url + Style.RESET_ALL)
                return

        for dom in hehe:
                print(dom)

main()
