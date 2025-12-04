url = input("Paste/Enter your URL here: ")

protocol = url.split("://")[0]
url = url.replace(protocol + "://", "")
subdomain = url.split(".")[0]
domain = url.split(".")[1]
url = url.replace(subdomain + "." + domain + ".", "")
top_level_domain = url.split("/")[0]
url = url.replace(top_level_domain + "/", "")
path = url.split("?")[0]
qurey_parameters = url.replace(path + "?", "")

print(f"Protocol: {protocol}\nSubdomain: {subdomain}\nDomain: {domain}\nTop Level Domain: {top_level_domain}\nPath: {path}\nQurey Parameters: {qurey_parameters}\n")

