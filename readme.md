# Setup project
```bash
# clone this repo
git clone https://github.com/abnvanand/ImageInpainting
# setup a virtual environment
python3 -m venv env
# install dependencies
pip install -r requirements.txt
```

Download rgb images from here: [Google Drive](https://drive.google.com/file/d/1tbFqV-VyZ2k58lBH10OB6Vi5KH1KAP4i/view?usp=sharing)  
Extract to project root
Directory structure after extracting should be
```
├── images
│   ├── greyscale
│   └── rgb
├── paper.pdf
```

# convert to grascale
```bash
python rgb_to_greyscale.py --source='../images/rgb/' --dest='../images/greyscale/'
```
