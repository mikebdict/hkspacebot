import requests
import pandas 
from os import makedirs
from time import strftime

def OPUS_downloader_f():
    # Folder to save the images that we download
    today__dir_str = 'datadir/images/'+strftime('%Y-%m-%d')+'/'
    makedirs(today__dir_str, exist_ok=True)

    # Opening the big CSV file as a pandas object lets us pick a random entry
    #  without traveseing the whole list.     
    allcsv_pandas = pandas.read_csv('datadir/opus_csv/all.csv')
    random_OPUS_id = allcsv_pandas.sample(n=1)\
    .to_string(index_names=False, header=False, index=False).strip()
    
    # Create a list to save various bits of information from the JSON:
    picture_info_li = []

    opus_json_response = requests.get(
        'https://opus.pds-rings.seti.org/opus/__api/metadata_v2/'
        +random_OPUS_id+'.json').json()

    json_respose_images = requests.get(
        'https://opus.pds-rings.seti.org/opus/api/image/full/'
        +random_OPUS_id+'.json').json()

    json_respose_imageurl = json_respose_images['data'][0]['url']

    # [0] Some information about the picture we download
    OPUS_id_log =   [opus_json_response['PDS Constraints']['primaryfilespec'],
                    opus_json_response['General Constraints']['instrument'],
                    opus_json_response['General Constraints']['time1'],
                    opus_json_response['General Constraints']['target']
                    ]
    picture_info_li.append(OPUS_id_log)

    # [1] The JSON URL
    picture_info_li.append  (
        'https://opus.pds-rings.seti.org/opus/__api/metadata_v2/'
        +random_OPUS_id+'.json'
                            )
    
    # [2] The realative path of the saved image 
    picture_info_li.append  (
        today__dir_str+random_OPUS_id+'.jpg'
                            )
    
    # Save the picture 
    picture_bytes = requests.get(json_respose_imageurl)
    open(today__dir_str+'{}.jpg'.format(random_OPUS_id),
        'wb').write(picture_bytes.content)
    return picture_info_li