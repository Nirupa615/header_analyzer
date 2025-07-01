import requests
from termcolor import colored

def trace_redirects(url):
    try:
        print(colored(f"Checking: {url}", "blue"))
        response = requests.get(url, allow_redirects=True, timeout=10)
        history = response.history
        print(colored("Redirect Chain:", "yellow"))
        for r in history:
            print(colored(f"{r.status_code} → {r.url}", "blue"))
        print(colored(f"Final URL: {response.status_code} → {response.url}", "green"))
    except Exception as e:
        print(colored(f"Error: {e}", "red"))

if __name__ == "__main__":
    url = input("Enter a URL to trace redirects: ")
    trace_redirects(url)
