from absl import app
from absl import flags


import ijson
import csv

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'index_path', '/',
    'Path to .csv file where all index images are listed in a single row seperated by a comma'
    )
def main(argv):
  extension='.jpg'
  jsonFile = open('/home/valentin/Downloads/CUE_DATEN_Staufen/blmki_bildarchivstaufen.json', 'rb')
  #  json_data = json.load(j)
    
  allImages=[]

  with open(FLAGS.index_path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: # each row is a list
      index_list = row
      #for i in ijson.items(j, 'records.item.medium.item.name', multiple_values=True):
      for record in ijson.items(jsonFile, 'records.item', multiple_values=True):
        if 'medium' in record:
          for i in record['medium']:
            print(i)
            for imageName in index_list:
              if i["name"] == imageName+extension:
                imageName=i
                locationName=record['ort']:
                histImage = HistImage(name="i")
                allImages.append(histImage)
                print(i)
        else:
          print(record['objektid'])
        
  print(allImages)            
            
class HistImage:
  def __init__(self, name="", locName="", lat=None, lon=None, construction="", demolition=""):
    self.imageName = name
    self.locationName = locName
    self.lat = lat
    self.lon = lon
    self.construction = construction
    self.demolition = demolition    	
    	
if __name__ == '__main__':
  app.run(main)
