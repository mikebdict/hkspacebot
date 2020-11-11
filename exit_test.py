import sys
haiku_spacebot_log_li = [
    ['masaoka shiki',
    'the sky draws near', 
    "the sky draws near\nsuch a bright sunrise\nNew Year's Day"
    ], 
        [['COISS_2024/data/1532374774_1532425248/N1532375151_1.IMG',
         'Cassini ISS', 
        '2006-07-23T19:14:36.556', 
        'Saturn Rings'], 
        'https://opus.pds-rings.seti.org/opus/__api/metadata_v2/co-iss-n1532375151.json', 
        'datadir/images/2020-11-10/co-iss-n1532375151.jpg'
        ], 
            'datadir/images/2020-11-10/composite/co-iss-n1532375151.jpg',

                ['chrome version 83.0.4103.116 loaded', 
                'Loaded page (2) Haikus from outer space - Home', 
                'Clicked create post', 
                'Message entered', 
                'Photo uploaded', 
                'Createing post failed'
                ]
]

facebook_poster_f_errors_li =   [
'Couldnt log in exiting',
'Couldnt click create post',
'Couldnt enter message',
'Couldnt upload image',
'Createing post failed',
                                ]

for x in haiku_spacebot_log_li[3]:
    if x in facebook_poster_f_errors_li:
        print('error encountered')
        sys.exit(1)