from pickle import load
from random import choice
import sys
from NASA_OPUS_downloader import OPUS_downloader_f
from pywand_image_combiner import img_combiner_f
from facebook_bot_selenium import facebook_poster_f

with open ('hks.pickle', 'rb') as f:
    haiku_li = load(f)

# Pick a random HK from the pickled list    
single_randomhk_li = choice(haiku_li)
facebook_formated_msg_str = f'{single_randomhk_li[2]}\n\n{single_randomhk_li[0]}\
- {single_randomhk_li[1]}'

# Open a list for the programs progress log
haiku_spacebot_log_li = []
haiku_spacebot_log_li.append(single_randomhk_li)

# Call the OPUS_downloader function and assign the returned list which we pass to
# img_combiner_f
picture_info_li = OPUS_downloader_f()
haiku_spacebot_log_li.append(picture_info_li)

# Call the pywand image combiner function assign the returned list which we pass to
# facebook_poster_f
folder_filename_str = img_combiner_f(picture_info_li)
haiku_spacebot_log_li.append(folder_filename_str)

# Call the selenium bot function add the returned list to the last bit of the log.
facebookpost_result = facebook_poster_f(facebook_formated_msg_str, folder_filename_str)
haiku_spacebot_log_li.append(facebookpost_result)

# I want the program to exit with an error if any of the try exceptions are encountered in selenium.
# This way cron will email me. Its normally beacuse an xpath changed.

facebook_poster_f_errors_li = [
'Couldnt log in exiting',
'Couldnt click create post',
'Couldnt enter message',
'Couldnt upload image',
'Createing post failed',
                            ]

for poster_status_str in haiku_spacebot_log_li[3]:
    if poster_status_str in facebook_poster_f_errors_li:
        print(haiku_spacebot_log_li)
        sys.exit(1)

print(haiku_spacebot_log_li)