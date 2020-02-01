"""
sort the list and print the second value of each tuple.
sort through each mail server and get its preference, and compare it
if the preference of the first mail server is less than or equal with the second one, print it
if not, bring it down and compare it again
and print only the second value of each tuple

"""

import dns.resolver

def MX_lookup( host ):
    answers = dns.resolver.query(host, 'MX')

    servers = [] # server name and preference for sorting
	preference = []
    for rdata in answers:
		preference.append((rdata.preference))
		
	preference_ascending = sorted(preference, key=int)
	servers.append((preference_ascending))
	
    return servers

if __name__ == '__main__':
    host = input( "Enter a domain name to look up: " )
    mail_servers = MX_lookup( host )
        print(s)