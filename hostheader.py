import requests

# Target URL (Change this)
TARGET_URL = "http://testingURL.tld"

# List of malicious Host headers to test
HOST_HEADERS = [
    "evil.com",
    "attacker.com",
    "vaibhav.com",
    "example.com",
    "google.com",
    "phishing-site.com"
]

def test_host_header_injection():
    print(f"[*] Testing Host Header Injection on {TARGET_URL}")

    for host in HOST_HEADERS:
        headers = {"Host": host}
        try:
            response = requests.get(TARGET_URL, headers=headers, allow_redirects=False, timeout=5)

            if "Location" in response.headers:
                redirect_url = response.headers["Location"]
                print(f"[+] Host Header Injection Possible! Redirected to: {redirect_url}")
            else:
                print(f"[-] No redirection for Host: {host}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error testing Host: {host} - {e}")

if __name__ == "__main__":
    test_host_header_injection()
