import dns.resolver

def MX_lookup(host):
	answers = dns.resolver.query(host, 'MX')
	
	servers = []
	preference = []
	
	for rdata in answers:
		preference.append((rdata.preference))
	
	preference_ascending = sorted(preference, key=int)
	servers.append((preference_ascending))
	
	return servers
	
if __name__ == '__main__':
	host = input("Enter a domain name to look up: ")
	mail_servers = MX_lookup(host)
	for s in mail_servers:
		print(s)