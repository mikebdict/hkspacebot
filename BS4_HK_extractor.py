from bs4 import BeautifulSoup
import glob
import pickle

# create a list of all of the pages with the poem that we want to extract
# the glob module allows the wildcard and takes care of spaces in the file names
all_hk_pages_li = glob.glob('datadir/html/HKs/*')

# create a list of each haiku poem from each page
haiku_li = []
for page in all_hk_pages_li:
    # open the page with beautiful soup
    soup_obj = BeautifulSoup(open(page), 'lxml')
    # isloate the poem text with the paragraph attribute 'text'
    # remove the html formatting characters from within the paragraph and remove excess
    # whitespace
    hk_str = soup_obj.find('p', attrs={'itemprop': 'text'}).get_text("\n").strip()
    # Save the title of the poem and author - the simplest (all in one) element
    # for this was the page title. Get only the 'content' part and split the 
    # author and title up into seperate list elements
    hk_title_author_li = soup_obj.find('meta', attrs={'name': 'keywords'})\
    ['content'].split(',')
    each_hk_li = [hk_title_author_li[1].strip()]+[hk_title_author_li[0]]+[hk_str]
    haiku_li.append(each_hk_li)
    # Since this loop is working on *a lot* of pages I want to see a bit of progress
    # as the program progresses.
    print('reached page: '+hk_title_author_li[0])

# Some of the Haiku's contain a 'translated by' line in the hk_str. Since this will
# look ugly in our final output, im removeing it. I used enumerate so I could find and 
# test a few of the more problematic ones. I use the second string first otherwise part
# of it would be deleted.

translationline_str_1 = '\nTranslated by'
translationline_str_2 = '\n \nTranslated by'
formatted_hk_li = []
for index, haiku in enumerate(haiku_li):
    if translationline_str_2 in haiku[2]:
        haiku[2] = haiku[2].split(translationline_str_2, 1)[0]
        print(f'string replaced in {index}')
    if translationline_str_1 in haiku[2]:
        haiku[2] = haiku[2].split(translationline_str_1, 1)[0]
        print(f'string replaced in {index}')
    formatted_hk_li.append(haiku)

# Save the list as a pickle so can open it in our other programs 
with open("hks.pickle", "wb") as f:
    pickle.dump(formatted_hk_li, f)