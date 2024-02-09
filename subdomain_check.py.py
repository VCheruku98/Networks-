import requests
import time
from tabulate import tabulate

# Subdomains
subdomains = ['google.com', 'youtube.com', 'twitter.com']

def subdomain_status(subdomains):# def function to check the status of the subdomains.
    table = []

    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}")
            status = 'UP' if response.status_code == 200 else 'DOWN'
        except requests.ConnectionError:
            status = 'DOWN'
        
        table.append([subdomain, status])

    return table

def print_status(table): # def function for the printing the status in table format.
    headers = ["Subdomain", "Status"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__": # main calling function.
    while True:
        table = subdomain_status(subdomains)
        print_status(table)
        time.sleep(120)
