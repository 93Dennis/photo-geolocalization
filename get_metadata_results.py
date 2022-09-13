###
#
# @Author:
# Dennis Przytarski: dennis.przytarski@gmx.de
#
# @Description: 
# This file reads the results, adds the corresponding lat & lon metadata
# provided by the the Landesmuseum Baden in json format to all results
# and saves it as new txt file
#
###

from absl import app
from absl import flags
# import ijson
import json 

FLAGS = flags.FLAGS

flags.DEFINE_string(
  'results_path', 'delg/workspace/results/final/BA 2020-00001-034_Scan01_result.txt',
  'Path to .text results file.'
)
flags.DEFINE_string(
  'json_path', 'delg/workspace/metadata/blmki_bildarchivstaufen.json',
  'Path to Baden\'s "Staufen" .json file with metadata.'
)
flags.DEFINE_string(
  'image_extension', '.jpg',
  'Extension of image files in json metadata.'
)

def main(argv):
  with open(FLAGS.results_path) as rf:
    new_results = []

    results = rf.readlines()
    for r in results: 
      r_name = r.rsplit('] ', 1)[1][:-2]
      with open(FLAGS.json_path, 'r') as json_file:
        # use ijson when everything in one line
        #for i in ijson.items(j, 'records.item.medium.item.name', multiple_values=True):
        data = json.load(json_file)
        loc_name, lat, lon = 'N/A', 'N/A', 'N/A'
        for record in data['records']:
          if 'medium' in record:
            for i in record['medium']:
              if i["name"] == r_name + FLAGS.image_extension:
                for o in record["ort"]:
                  if o["typ"] == 'Herstellungsort':
                    if 'term' in o:
                      loc_name = o["term"]
                    if 'lat' and 'lon' in o:
                      lat = o["lat"]
                      lon = o["lon"]
        new_results.append(r[:-2] + ' - location: ' + loc_name + ' - lat: ' + lat + ', lon: ' + lon + '\n')
    
    nf_path = FLAGS.results_path[:-4] + '_location.txt'
    nf = open(nf_path, "w")
    nf.writelines(new_results)
    nf.close()

  rf.close()
  print('Successfully created results with metadata: ' + nf_path) 
    	
if __name__ == '__main__':
  app.run(main)
