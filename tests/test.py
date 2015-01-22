import sys
import json
import urllib2

hdr = {
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'application/json,text/javascript,application/jsonrequest;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Content-Type': 'application/json',
       'Connection': 'keep-alive'
      }

def url_valid(x):
	req = urllib2.Request(x,headers=hdr)
	try:
		urllib2.urlopen(req)
		return True
	except Exception:
		return False

def main():
	j = open('./directory.json').read()
	obj = json.loads(j)
	invalid_urls = []
	for x in obj:
		url = obj[x]
		if not url_valid(url):
			invalid_urls.append(url)

	if len(invalid_urls) > 0:
		print "\nThe following urls are invalid: "
		print "\n".join(invalid_urls)
		sys.exit(1)
	else:
		sys.exit(0)

if __name__ == '__main__':
	main()