import dns.resolver

answers = dns.resolver.query('kuis.edu.my', 'MX')
for rdata in answers:
	print('Host', rdata.exchange, 'haspreference', rdata.preference)