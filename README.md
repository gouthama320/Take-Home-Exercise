# SRE Health Check

This project implements a health check tool for monitoring the availability of HTTP endpoints. The program reads a YAML configuration file containing details of the endpoints to monitor, performs periodic health checks, and logs the cumulative availability percentage of each domain.

---

## Features

- **Periodic Health Checks:** Sends HTTP requests to endpoints every 15 seconds.
- **Availability Monitoring:** Tracks the availability percentage of each domain over time.
- **Customizable Configuration:** Accepts a YAML file describing the endpoints to monitor.
- **Latency Measurement:** Considers an endpoint "UP" only if the response is fast (latency < 500ms) and has a 2xx status code.
- **Graceful Exit:** Allows the program to be terminated manually via `CTRL+C`.

---

## Requirements

- Python 3.7 or higher installed on your system.
- Install the following Python libraries:
  - `requests`
  - `PyYAML`

To install the required libraries, run:
```bash
pip install requests pyyaml
```

---

## Usage

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Prepare a YAML Configuration File
Create a YAML file to define the endpoints to monitor. Use the following format:

```yaml
- headers:
    user-agent: fetch-synthetic-monitor
  method: GET
  name: Fetch Index Page
  url: https://example.com
- headers:
    user-agent: fetch-synthetic-monitor
  method: POST
  body: '{"key": "value"}'
  name: Fetch Example Endpoint
  url: https://example.com/api
```

Save this file to a known location, e.g., `config.yaml`.

### Step 3: Run the Program
Execute the script, providing the path to your YAML configuration file:

```bash
python sre_health_check.py /path/to/config.yaml
```

### Step 4: Monitor Logs
The program outputs the availability percentage of each domain to the console every 15 seconds. Example output:

```
example.com has 67% availability percentage
anotherdomain.com has 50% availability percentage
```

---

## Compatibility

This solution is cross-platform and should work on any operating system (Linux, macOS, or Windows) that supports Python 3.7 or higher. Ensure you have Python and pip installed and properly configured on your system.

### Installing Python
If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

### Verifying Python Installation
To verify Python and pip are installed, run:
```bash
python --version
pip --version
```

If these commands do not return valid version numbers, ensure Python is added to your system PATH.

---

## How It Works

1. **Parse Configuration:** The program reads the YAML file and extracts endpoint details.
2. **Send HTTP Requests:** Each endpoint is tested periodically based on the specified HTTP method, headers, and body.
3. **Evaluate Health:**
    - `UP` if the response code is 2xx and latency < 500ms.
    - `DOWN` otherwise.
4. **Log Results:** After every test cycle, the program calculates and logs the availability percentage of each domain.
5. **Repeat:** The process continues until the user manually exits.

---

## Example Output
For a configuration monitoring `https://example.com` and `https://example.org`, the program might output:

```
example.com has 75% availability percentage
example.org has 100% availability percentage
example.com has 80% availability percentage
example.org has 100% availability percentage
```

---

## Development

### Testing
You can simulate the functionality locally using mock endpoints such as `https://httpbin.org`. Adjust the configuration file to point to these endpoints for testing purposes.

### Mock Testing Example
Modify the script to use the `mock_send_request` function for a controlled environment:

```python
def mock_send_request(endpoint):
    if "status/200" in endpoint['url']:
        return "UP"
    return "DOWN"
```

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as needed.

