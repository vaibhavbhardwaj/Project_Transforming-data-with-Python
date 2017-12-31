import read

df = read.load_data()

number_of_domains = df['url'].value_counts()

domains = dict()

for name,row in number_of_domains.items():
    if name not in domains:
        domains[name] = row+1
domain_sorted = sorted(domains.items(), key=lambda value: value[1],reverse=True)
print((domain_sorted[1:]))