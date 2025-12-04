from urllib.parse import urlparse

url = input("Paste/Enter your URL here: ")

parsed_url = urlparse(url)

protocol = parsed_url.scheme
domain_full = parsed_url.netloc
path = parsed_url.path.lstrip("/")
parameters = parsed_url.params if parsed_url.params else "(none)"
query = parsed_url.query if parsed_url.query else "(none)"
fragments = parsed_url.fragment if parsed_url.fragment else "(none)"

parts = domain_full.split(".")
if len(parts) == 3:
    subdomain, domain, tld = parts
elif len(parts) == 2:
    subdomain = "(none)"
    domain, tld = parts
else:
    subdomain = "(unknown)"
    domain = "(unknown)"
    tld = "(unknown)"


print(f"Protocol: {protocol}\nSubdomain: {subdomain}\nDomain: {domain}\nTop Level Domain: {tld}\nPath: {path}\nParameters: {parameters}\nQuery: {query}\nFragments: {fragments}\n")