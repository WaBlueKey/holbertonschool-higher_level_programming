# this is a python script that displays a list of the full names of the 30 most popular Python projects on GitHub.

from urllib2 import urlopen
from json import loads

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 1e4494c05723340138ecb8ec379d6c1988e39ced'
}

address = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
content = urlopen(address).read()
json_content = loads(content)
for fullname in json_content["items"]:
    print fullname["full_name"]
