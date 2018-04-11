class Website:
    def __init__(self, host, domain, query=None):
        if query is None:
            query = []
        self.host = host
        self.domain = domain
        self.query = '&'.join([f'[{str(q)}]' for q in query])

    def build_url(self):
        return f'https://www.{self.host}.{self.domain}' if not self.query \
            else f'https://www.{self.host}.{self.domain}/query?={self.query}'


sites = []
line = input()
while line != 'end':
    parts = line.split(' | ')
    if len(parts) == 2:
        hosts, domains = parts
        sites.append(Website(hosts, domains))
    else:
        hosts, domains, queries = parts
        queries = queries.split(',')
        sites.append(Website(hosts, domains, queries))

    line = input()

for site in sites:
    print(site.build_url())
