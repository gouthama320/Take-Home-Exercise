import argparse
import time
import yaml
import requests
from collections import defaultdict

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def send_request(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET').upper()
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = (time.time() - start_time) * 1000  # Convert to ms

        if 200 <= response.status_code < 300 and latency < 500:
            return 'UP'
        else:
            return 'DOWN'
    except requests.RequestException:
        return 'DOWN'

def calculate_availability(stats):
    availability = {}
    for domain, (up_count, total_count) in stats.items():
        availability[domain] = round(100 * (up_count / total_count))
    return availability

def main():
    parser = argparse.ArgumentParser(description="HTTP Endpoints Health Checker")
    parser.add_argument('config_file', help="Path to the YAML configuration file")
    args = parser.parse_args()

    endpoints = load_config(args.config_file)
    domain_stats = defaultdict(lambda: [0, 0])  # {domain: [up_count, total_count]}

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint['url'].split('/')[2]  # Extract domain
                result = send_request(endpoint)

                if result == 'UP':
                    domain_stats[domain][0] += 1
                domain_stats[domain][1] += 1

            availability = calculate_availability(domain_stats)
            for domain, percentage in availability.items():
                print(f"{domain} has {percentage}% availability percentage")

            time.sleep(15)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
