import os, csv
from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string(
  'images_path', './images',
  'Path to all images to be used.'
)
flags.DEFINE_string(
  'index_path', './index.csv',
  'Path to index.csv file where all index images will be listed.'
)
flags.DEFINE_string(
  'query_path', './query.csv',
  'Path to query.csv file where the query images will be listed.'
)
flags.DEFINE_list(
  'query_images', '',
  'List the query images seperated by a comma WITHOUT extension.'
)

def main(argv):
  with open(FLAGS.index_path, 'w') as f:
    writer = csv.writer(f)
    names_row = ''
    for (root, dirs, files) in os.walk(FLAGS.images_path):
      files.sort()
      for filename in files:
        filename = os.path.splitext(filename)[0]
        if not any(query_image in filename for query_image in FLAGS.query_images):
          """ names_row += filename + ', ' """
          writer.writerow([filename])
    """ writer.writerow([names_row]) """
  
  if len(FLAGS.query_images) > 0:
    with open(FLAGS.query_path, 'w') as f:
      for filename in FLAGS.query_images:
        csv.writer(f).writerow([filename])

if __name__ == '__main__':
  app.run(main)
  