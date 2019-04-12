import os
import zipfile
import wget

with open('files.txt', 'r') as fp:
    files = [ x.strip() for x  in fp.readlines()]

for f in files:

    if ".zip" in f:
        shortname = f
        fullname = f
    else:
        shortname = '{}_sync.zip'.format(f)
        fullname = '{}/{}'.format(f, shortname)
    
    url = "https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/{}".format(fullname)
    
    drive_date = "{}_{}_{}".format(*f.split('_')[0:3])
    
    extracted_dir = os.path.join(drive_date, '{}_sync'.format(f))
    if not os.path.exists(extracted_dir):
        print("Downloading {}".format(url))
        #wget.download(url)
        os.system('wget {}'.format(url))

        with zipfile.ZipFile("{}".format(shortname),"r") as zip_ref:
           zip_ref.extractall()
    else:
        print("Skipping {}".format(fullname))