"""
ASSIGNMENT 4

ARIF ZUHAIRI BIN MOHD BASRI
16BT02033
LECTURER: EN KHAIRIL ASHRAF BIN ELIAS

A list of servers. 
The servers should be sorted by the domains's priorities as specified in their DNS MX records.
"""
# python 3
import dns.resolver

def MX_lookup(host):
	answers = dns.resolver.query(host, 'MX')
	
	servers = []
	
	for rdata in answers:
		servers.append((rdata.preference, rdata.exchange))

	servers = sorted(servers, key=lambda server: server[0])
	return servers
	
if __name__ == '__main__':
	host = input("Enter a domain name to look up: ")
	mail_servers = MX_lookup(host)
	for s in mail_servers:
		print(s[1])