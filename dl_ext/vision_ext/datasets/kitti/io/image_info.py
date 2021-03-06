import os
import pickle
from typing import Union

from tqdm import tqdm
import numpy as np


class _ImageInfoCache:
    instance = None

    def __init__(self):
        raise SyntaxError('can not instance, please use get_instance')

    @staticmethod
    def get_instance(root, split):
        if _ImageInfoCache.instance is None:
            _ImageInfoCache.instance = object.__new__(_ImageInfoCache)
            _ImageInfoCache.instance.post_init(root, split)
        return _ImageInfoCache.instance

    def post_init(self, root, split):

        cache_dir = os.path.expanduser('~/.dl_ext/vision_ext/datasets/kitti/image_info')
        self.cache_path = os.path.join(cache_dir, f'{split}.pkl')
        os.makedirs(cache_dir, exist_ok=True)
        self.root = root
        self.split = split
        self.infos = self.load_info()

    def load_info(self):
        if os.path.exists(self.cache_path):
            return pickle.load(open(self.cache_path, 'rb'))
        else:
            print('Image info cache not found. Generating...')
            from .image_2 import load_image_2
            img_shapes = []
            n = len(os.listdir(os.path.join(self.root, 'object', self.split, 'image_2')))
            for i in tqdm(range(n), leave=False):
                img2 = np.array(load_image_2(self.root, self.split, i))
                img_shapes.append(img2.shape)
            pickle.dump(img_shapes, open(self.cache_path, 'wb'))
            print('Done.')
            return img_shapes


def load_image_info(kitti_root: str, split: str, imgid: Union[int, str]):
    if not isinstance(imgid, int):
        imgid = int(imgid)
    img_info = _ImageInfoCache.get_instance(kitti_root, split)
    return img_info.infos[imgid]
