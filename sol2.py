from skimage.feature import blob_log
import glob
from skimage.io import imread

picture= glob.glob('star2.jpg')[0]
im= imread(picture, as_grey=True)
blobs_log = blob_log(im, max_sigma = 30, num_sigma = 10, threshold = .1)
numrows = len(blobs_log)
print('количество звезд на фото:', numrows)