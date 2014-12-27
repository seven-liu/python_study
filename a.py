import os.path as osp

def yield_filenames(path,ignore_hide_file=True, ignore_prefix=(), ignore_suffix=()):
        """other params may be useful in future"""
        path = osp.expanduser(path)
        path = osp.abspath(path)
        if not path or not osp.isdir(path):
            return

        for root, dirs, fnames in os.walk(path):
            for f in fnames:
                if ignore_hide_file and f.startswith('.'):
                    continue
                if f.endswith(ignore_suffix):
                    continue
                if f.startswith(ignore_prefix):
                    continue

                yield osp.join(root, f)


dir='d:\\test'
list1=[]
list1=yield_filenames(dir)
print list1