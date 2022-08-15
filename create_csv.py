import os, csv
from absl import app
from absl import flags
import random

from nbformat import write

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
  'query_images', [],
  'List the query images seperated by a comma WITHOUT extension.'
)
flags.DEFINE_list(
  'index_images', [],
  'List the index images seperated by a comma WITHOUT extension. If none, all images besides query images will be selected.'
)
flags.DEFINE_integer(
  'random_query', 0,
  'Number of random images to query. Only used when no query_images specified and number higher than 0.',
  lower_bound = 0
)

def main(argv):
  query_images = FLAGS.query_images or []
  index_images = FLAGS.index_images or []

  # write specified query images to csv
  if len(query_images) > 0:
    write_to_file(FLAGS.query_path, query_images)
    print('%i images successfully saved as query: %s' % (len(query_images), str(query_images)))

  # if no query specified and random images > 0, choose random query images
  elif FLAGS.random_query > 0:
    for (root, dirs, files) in os.walk(FLAGS.images_path):
      files = random.sample(files, FLAGS.random_query)
      files.sort()
      for filename in files:
        filename = os.path.splitext(filename)[0]
        query_images.append(filename)
    write_to_file(FLAGS.query_path, query_images)
    print('%i random images successfully saved as query: %s' % (len(query_images), str(query_images)))
  
  # write specified index images to csv
  if len(index_images) > 0:
    write_to_file(FLAGS.index_path, index_images)
    print('%i images successfully saved as index: %s' % (len(index_images), str(index_images)))

  # else use all images besides query for index
  else:
    with open(FLAGS.index_path, 'w') as f:
      for (root, dirs, files) in os.walk(FLAGS.images_path):
        files.sort()
        for filename in files:
          filename = os.path.splitext(filename)[0]
          if not any(query_image in filename for query_image in query_images):
            index_images.append(filename)
      write_to_file(FLAGS.index_path, index_images)
      print('%i images successfully saved as index.' % (len(index_images)))

def write_to_file(path, files):
  with open(path, 'w') as f:
      for filename in files:
        csv.writer(f).writerow([filename])

if __name__ == '__main__':
  app.run(main)
  