import dns.resolver

def MX_lookup( host ):
    answers = dns.resolver.query(host, 'MX')

    servers = []    # server name and preference for sorting
    for rdata in answers:
        servers.append( (rdata.preference, rdata.exchange) )

    return servers

if __name__ == '__main__':
    host = input( "Enter a domain name to look up: " )
    mail_servers = MX_lookup( host )
    for s in mail_servers:
        print(s)

#sort ascending
#show main email domain only