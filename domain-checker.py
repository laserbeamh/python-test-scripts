import re

text = input("Enter domain: ")
domain_list = []
#pattern = r"((http(s)?)://)?(www)?(.\w+\..\w+)"
#pattern = r"(\w+\..\w+(.\w+)?)"
pattern = r"([\w\.-]+\.[\w\.]+)"
domains = re.findall(pattern,text)
for domain in domains:
	print(domain)
