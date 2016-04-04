# this is a python script that writes the response of the most popular Python projects on GitHub into a file.

from urllib2 import urlopen

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 1e4494c05723340138ecb8ec379d6c1988e39ced'
}

address = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
content = urlopen(address).read()
file = open("/tmp/29", "w")
file.write(content)
file.close()
print "The file was saved!"
