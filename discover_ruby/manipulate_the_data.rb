require 'open-uri'
require 'json'
require 'pp'
# use personal token to access GitHub API.
extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 1e4494c05723340138ecb8ec379d6c1988e39ced'
}
# open the url
site = open('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
file = site.read
result = JSON.parse(file)
list = result["items"]
list.each{|x| puts x["full_name"]}
