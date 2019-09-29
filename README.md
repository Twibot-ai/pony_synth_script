## Description
This is a script for deepvoice3 voice-synthesizer

## Usage
### Windows

`synthesize.exe "./checkpoint_step000200000_22hz_16bit.pth" "./20180505_deepvoice3_ljspeech.json" "This is a test of exe" "test.wav"`

### Linux

`./synthesize "./checkpoint_step000200000_22hz_16bit.pth" "./20180505_deepvoice3_ljspeech.json" \ "This is a test of exe" "test.wav"`

###Via Python

`main.py "./checkpoint_step000200000_22hz_16bit.pth" "./20180505_deepvoice3_ljspeech.json" \ "This is a test of exe" "test.wav"`

## How to build own

1. Install anaconda
2. Install python 3.5
3. Install requirements for your system
4. Install cmudict
```python
    import nltk
    nltk.download('cmudict')
```
5. Change PyInstaller NLTK-Hook (they have bug in it)
(If you installed via anaconda in linux)
In `~/anaconda3/envs/synth_pony/lib/python3.5/site-packages/PyInstaller/hook-nltk.py`
Change this:
```
for p in nltk.data.path:
    datas.append((p, "nltk_data"))
```
To this:

```
#for p in nltk.data.path:
#    datas.append((p, "nltk_data"))
datas.append(('~/nltk_data', "nltk_data"))
```
Or where nltk data is

6. Build

```
pyinstaller main.py --onefile \
    --hidden-import="sklearn.utils._cython_blas" \
    --hidden-import="sklearn.neighbors.typedefs" \
    --hidden-import="sklearn.neighbors.quad_tree" \
    --hidden-import="sklearn.tree"
```
    
7. (Optional) Some libraries could be requested to install.
Install them and also open an issue to update this instruction
