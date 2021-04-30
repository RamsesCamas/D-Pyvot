import os

LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

"""if not os.path.exists(LABELIMG_PATH):
    os.system(f'mkdir {LABELIMG_PATH}')
    os.system(f'git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}')"""

if os.name =='nt':
    os.system(f'cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc')