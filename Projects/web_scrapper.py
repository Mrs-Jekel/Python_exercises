import requests
import inflection
import beautifulsoup4

www.dailysmarty.com/topics/python

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for i in range (36, len(soup.findAll('a'))+1):
    one_a_tag - soup.finadAll('a'[i])
    link = one_a_tag['href']
    download_url = 'www.dailysmarty.com/topics/python' + link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])