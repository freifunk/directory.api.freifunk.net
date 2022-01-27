#/usr/bin/python3

import requests
import json
import threading
import sys
import jsondiff
import queue
import threading
from pathlib import Path
import glob
import jsonschema
import ast

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'application/json,text/javascript,application/jsonrequest;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive'
}

ff_api_specs = {}

def read_url(url, queue):
    try:
        req = requests.get(url, headers = headers)
        req.raise_for_status()
        api_content = json.loads(req.content)

        validation = jsonschema.Draft7Validator(ff_api_specs[api_content['api']])
        errors = sorted(validation.iter_errors(api_content), key = str)

        if errors:
            text_result = "\n\t".join("Error in {}: {}\n".format("->".join(str(path) for path in err.path), err.message) for err in errors)
            text_result = "Validation error in the community file {}:\n\t{}".format(api_content['name'], text_result)
            print(text_result)
            queue.put(url)
            return
    
    except ValueError as e:
        print("Value error while paring JSON:", url)
        print(e)
        queue.put(url)

    except KeyError as e:
        if api_content['api']:
            print("Invalid or unknown API version {}: {}".format(api_content["api"], url))
        else:
            print("Invalid or unknown API version", url)
        print(e)
        queue.put(url)

    except requests.exceptions.SSLError as e:
        print("SSLError", url)
        queue.put(url)

    except requests.exceptions.HTTPError as e:
        print("Http Error", e)
        queue.put(url)

    except requests.exceptions.ConnectionError as e:
        print("Connection Error", url)
        queue.put(url)

    except requests.exceptions.RequestException as e:
        print("Error while fetching",url)
        print(e)
        queue.put(url)

def fetch_parallel(urls):
    result = queue.Queue()
    threads = [threading.Thread(target = read_url, args = (url, result)) for comm, url in urls.items()]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result


def fetch_master_branch():
    print("[*] Fetching Master...", end = "")
    try:
        dir_master = requests.get("https://raw.githubusercontent.com/freifunk/directory.api.freifunk.net/master/directory.json")
        if dir_master.status_code != 200:
            print("[+] Can't fetch master branch of directory")
            sys.exit(1)
    except Exception as e:
        print("[+] Error while fetching master branch of directory")
        raise e
    print("Done!!")
    return json.loads(dir_master.content)


def main():
    f = open("./directory.json").read()
    directory = json.loads(f)
    directory_master  = fetch_master_branch()
    changes = json.loads(jsondiff.diff(directory_master, directory, syntax = "explicit", dump = True))
    
    spec_dir = './api.freifunk.net/specs/*.json'
    spec_files = glob.glob(spec_dir)
    for file in spec_files:
        file_content = open(file).read()
        ff_api_specs[Path(file).stem] = json.loads(file_content)

    # print("specs",ff_api_specs)

    urls_to_load = {}

    if "$insert" in changes:
        print("Found new entries")
        for comm,url in changes["$insert"].items():
            urls_to_load[comm] = url

    if "$update" in changes:
        print("Found update entries")
        for comm,url in changes["$update"].items():
            urls_to_load[comm] = url

    if not urls_to_load:
        print("nothing is added or updated, Checking all files")
        urls_to_load = directory_master

    # for i,j in urls_to_load.items():
        # print(i,j)

    result = fetch_parallel(urls_to_load)

    if result.empty():
        print("Result: All the URLs are valid :)")
        sys.exit(0)
    else:
        print("Result: Invalid URLs found :/")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        raise e
