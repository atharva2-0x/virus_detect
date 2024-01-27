import sys
import hashlib
import json
from virus_total_apis import PublicApi as public_api

n = len(sys.argv)


def file_input(file_name):
	file = open(file_name,"rb")
	output = file.read()
	return output


api_key = "xxxxx"
content = file_input(sys.argv[1])
md5_sum = hashlib.md5()
md5_sum.update(content)
digest = md5_sum.hexdigest()

vt = public_api(api_key)
response = vt.get_file_report(digest)
print(json.dumps(response,sort_keys=False,indent=4))
