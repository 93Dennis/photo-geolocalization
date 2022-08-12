# NOT FINALIZED and not needed right now
# this file reads the json data the Landesmuseum Baden provided
# and saves the index images with the corresponding metadata in a new json file

from absl import app
from absl import flags

#import ijson
import json 
import csv

FLAGS = flags.FLAGS

flags.DEFINE_string(
  'index_path', 'delg/workspace/data/index.csv',
  'Path to .csv file where all index images are listed, each in a separate row.'
)
flags.DEFINE_string(
  'json_path', 'delg/workspace/metadata/blmki_bildarchivstaufen.json',
  'Path to Baden\'s "Staufen" .json file with metadata.'
)
def main(argv):
  extension='.jpg'
  # jsonFile = open(FLAGS.json_path, 'rb')
    
  all_images=[]
  index_list = []

  with open(FLAGS.index_path) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader: # each row is a list
      index_list.append(row[0])
      # use ijson when everything in one line
      #for i in ijson.items(j, 'records.item.medium.item.name', multiple_values=True):
      """ for record in ijson.items(jsonFile, 'records.item', multiple_values=True):
        if 'medium' in record:
          for i in record['medium']:
            print(i)
            for image_name in index_list:
              if i["name"] == image_name+extension:
                image_name = i
                # loc_name = record['ort']
                hist_image = HistImage(name="i")
                all_images.append(hist_image)
                print(i)
        else:
          print(record['objektid']) """
      with open(FLAGS.json_path, 'r') as json_file:
        data = json.load(json_file)
        for record in data['records']:
          if 'medium' in record:
            for i in record['medium']:
              for image_name in index_list:
                if i["name"] == image_name+extension:
                  #image_name = i
                  # loc_name = record['ort']
                  for o in record["ort"]:
                    if o["typ"] == 'Herstellungsort' and 'lat' in o:
                      loc_name = o["term"]
                      lat = o["lat"]
                      lon = o["lon"]
                  
                  hist_image = {
                    "name": image_name,
                    "loc_name": loc_name,
                    "lat": lat,
                    "lon": lon,
                  }
                  # hist_image = HistImage(name="i")
                  all_images.append(hist_image)
                  print(hist_image)
          """ else:
            print(record) """
        
  print(all_images)            
            
class HistImage:
  def __init__(self, name="", loc_name="", lat=None, lon=None, construction="", demolition=""):
    self.image_name = name
    self.location_name = loc_name
    self.lat = lat
    self.lon = lon
    self.construction = construction
    self.demolition = demolition    	
    	
if __name__ == '__main__':
  app.run(main)
