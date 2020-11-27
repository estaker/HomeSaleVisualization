import requests

url = 'https://cedarrapids.iowaassessors.com/results.php?mode={0}&ipin={1}&idba={2}&ihnum={3}&iaddr={4}&opRestrict={5}&ilegal={6}&iacre1={7}&iacre2={8}&iphoto={9}'

def create_url(mode='basic', ipin='', idba='', ihnum='', iaddr='', opRestrict='yes', ilegal='', iacre1='', iacre2='', iphoto='0'):
    global url
    return url.format(mode, ipin, idba, ihnum, iaddr, opRestrict, ilegal, iacre2, iacre2, iphoto)
    

if __name__ == "__main__":
    # execute only if run as a script
    m_url = create_url(ihnum='1814', iaddr='C+St+SW')
    r = requests.get(m_url)
    print(r.content)


    #print(m_url)