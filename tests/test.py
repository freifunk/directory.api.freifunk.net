#!/usr/bin/python2

import sys
import json
import urllib2
import threading
import Queue
import glob
import os
import jsonschema
from jsondiff import diff

hdr = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'application/json,text/javascript,application/jsonrequest;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive' }

ff_api_specs = {} 

def read_url(url, queue):
    req = urllib2.Request(url, headers=hdr)
    try:
        res = urllib2.urlopen(req, None, 12)
        api_content = {}
        api_content = json.loads(res.read())
        validator = jsonschema.validators.validator_for(ff_api_specs[api_content['api']]['schema']) 
        validator.check_schema(ff_api_specs[api_content['api']]['schema'])
        v = validator(ff_api_specs[api_content['api']]['schema'])
        result = v.iter_errors(api_content)
        has_error = False
        text_result = ''
        for error in sorted(result,key=str):
            if not has_error:
                text_result = 'ValidationError in community file %s:\n' % (api_content['name'])
            has_error = True
            text_result = '%s\t Error in %s: %s\n' % (text_result, '->'.join(str(path) for path in error.path), error.message)

        if has_error:
            text_result = '%s\t Url: %s\n' %(text_result, url)
            print(text_result)
            queue.put(url)

    except urllib2.HTTPError as e:
        print('HTTPError: %s: %s' % (e.code, url))
        queue.put(url)
    except urllib2.URLError as e:
        print('URLError: %s: %s' % (e.reason, url))
        queue.put(url)
    except ValueError as e:
        print('Value error while paring JSON: %s' % (url))
        print(e)
        queue.put(url)
    except KeyError as e:
        if api_content['api']:
                print('Invalid or unknown API version %s: %s' % (api_content['api'], url))
        else:
                print('Invalid or unknown API version: %s' % (url))
        queue.put(url)
#    else:
#        print 'OK %s: %s' % (api_content['api'], url)

def fetch_parallel(urls_to_load):
    result = Queue.Queue()
    threads = [threading.Thread(target=read_url, args = (url, result)) for url in urls_to_load]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result

def get_directory_from_master_branch():
    directory_master_branch_url = "https://raw.githubusercontent.com/freifunk/directory.api.freifunk.net/master/directory.json"
    try:
        dir_master = urllib2.urlopen(directory_master_branch_url, None, 12)
        dir_master_content = {}
        dir_master_content = json.loads(dir_master.read())
    except:
        print('Error fetching directory from master branch')
        raise
    return dir_master_content

def main():
    j = open('./directory.json').read()
    directory = json.loads(j)
    directory_master = get_directory_from_master_branch()
    directory_diff = {}
    directory_diff = json.loads(diff(directory_master, directory, syntax='explicit', dump=True))
    spec_dir = './api.freifunk.net/specs/*.json'
    spec_files = glob.glob(spec_dir)
    for spec_file in spec_files:
        spec_content = open(spec_file).read()
        ff_api_specs[os.path.splitext(os.path.basename(spec_file))[0]] = json.loads(spec_content)

    urls_to_load = []
    invalid_urls = []

    if "$insert" in directory_diff:
        print("check inserted entries")
        for x in directory_diff["$insert"]:
            urls_to_load.append(directory_diff["$insert"][x])
    
    if "$update" in directory_diff:
        print("check updated entries")
        for x in directory_diff["$update"]:
            urls_to_load.append(directory_diff["$update"][x])

    if urls_to_load == []:
        print("check all files, as nothing else changed")
        for x in directory_master:
            urls_to_load.append(directory_master[x])

    result = fetch_parallel(urls_to_load)

    if result.empty():
        print('Result: All URLs are valid :-)')
        sys.exit(0)
    else:
        print('\nResult: Invalid URLs found :-(')
        sys.exit(1)

if __name__ == '__main__':
    main()
