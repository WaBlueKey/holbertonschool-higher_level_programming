require 'open-uri'

# use personal token to access GitHub API.
extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 1e4494c05723340138ecb8ec379d6c1988e39ced'
}
# open the url
site = open('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
list = site.read
File.write('/tmp/29', list)

puts 'The file was saved!'
