from bs4 import BeautifulSoup
import requests
import os
import time

read_folderpath_str = 'datadir/html/HK_links'
write_folderpath_str = 'datadir/html/HKs'
# create a list of pages to loop through and parse for links to the poems
html_pages_li = []
for filename in os.listdir(read_folderpath_str):
   html_pages_li.append(os.path.join(read_folderpath_str, filename))

for html_page in html_pages_li:
   # open each page with beautiful soup
   soup_obj = BeautifulSoup(open(html_page), 'lxml')
   # isloate the table with all of the poem links
   linktable_html = soup_obj.find('table', attrs={'class': 'poems'})
   # save the poem links in a list
   link_li = linktable_html.find_all('a')
   for link in link_li:
      # create a list with a non-realative url to pass to requests,
      # and the link text to use for the saved file names
      link_with_text_li = ['https://www.poemhunter.com'+link['href'], link.text]
      try:
         html_page_request = requests.get(link_with_text_li[0])
         open(write_folderpath_str+'/{}.html'.format(link_with_text_li[1]), 'wb')\
         .write(html_page_request.content)
         # dont hammer the server :)
         time.sleep(5)
      except:
         print('Request failed')
      continue