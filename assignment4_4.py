import dns.resolver
import json

def MX_lookup(host):
	answers = dns.resolver.query(host, 'MX')
	
	servers = []
	
	for rdata in answers:
		servers.append((rdata.preference, rdata.exchange))

	servers_pref_ascend = sorted(servers, key=lambda server: server[0])
	return servers_pref_ascend

def JSON_lookup(host):
	answers = dns.resolver.query(host, 'MX')
	
	servers = []
	
	for rdata in answers:
		servers.append((rdata.preference, rdata.exchange))

	data = json.dump(json.load(servers), indent=4)

	return data
	
if __name__ == '__main__':
	host = input("Enter a domain name to look up: ")
	mail_servers = MX_lookup(host)
	for s in mail_servers:
		print(s)