

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

# from preprocessing import cifarnet_preprocessing
# from preprocessing import inception_preprocessing
# from preprocessing import vgg_preprocessing

from preprocessing import ssd_vgg_preprocessing

slim = tf.contrib.slim


def get_preprocessing(name, is_training=False):
    """Returns preprocessing_fn(image, height, width, **kwargs).

    Args:
      name: The name of the preprocessing function.
      is_training: `True` if the model is being used for training.

    Returns:
      preprocessing_fn: A function that preprocessing a single image (pre-batch).
        It has the following signature:
          image = preprocessing_fn(image, output_height, output_width, ...).

    Raises:
      ValueError: If Preprocessing `name` is not recognized.
    """
    preprocessing_fn_map = {
        'ssd_300_vgg': ssd_vgg_preprocessing,
        'ssd_512_vgg': ssd_vgg_preprocessing,
    }

    if name not in preprocessing_fn_map:
        raise ValueError('Preprocessing name [%s] was not recognized' % name)

    def preprocessing_fn(image, labels, bboxes,
                         out_shape, data_format='NHWC', **kwargs):
        return preprocessing_fn_map[name].preprocess_image(
            image, labels, bboxes, out_shape, data_format=data_format,
            is_training=is_training, **kwargs)
    return preprocessing_fn
