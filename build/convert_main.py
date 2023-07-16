import os
from ipynb2md import Notebook2MD
import glob
import shutil

SOURCE_DIR='source'
TARGET_DIR='target'

COPY_TO_DICT = {
    'jupyterlab': 'tools',
    'pandas':  'bigdata',
    'pyspark':  'bigdata',
    'python':  'bigdata',
    '大数据之路': 'bigdata',
    'networkx': 'bigdata',

    # 'css': 'web',
    # 'javascript': 'web',
}

if __name__ == '__main__':
    outdir = os.path.join(os.path.dirname(__file__), TARGET_DIR)
    files = glob.glob(os.path.join(os.path.dirname(__file__), SOURCE_DIR, '*.ipynb'))
    for filepath in files:

        nb2md = Notebook2MD(notebook_path=filepath, output_dir=outdir)
        nb2md.convert()
        print(nb2md)

        findDir = COPY_TO_DICT.get(nb2md.basename)
        if findDir is None:
             continue
        
        dst_dir = f"{os.path.dirname(__file__)}/../{findDir}/"
        dst_dir = os.path.abspath(dst_dir)
        dst_filepath = os.path.abspath(f"{dst_dir}/{nb2md.basename}.md")
        dst_images_dir = os.path.join(dst_dir, os.path.basename(nb2md.output_images_dir))

        print(f"markdown move {nb2md.output_md_path} to {dst_filepath}...")
        shutil.move(nb2md.output_md_path, dst_filepath)
        if os.path.exists(nb2md.output_images_dir):
               print(f"images move {nb2md.output_images_dir} to {dst_dir}...")
               shutil.rmtree(dst_images_dir, ignore_errors=True)
               shutil.move(nb2md.output_images_dir, dst_dir)
