# Image resizer for chrome extension
- Python image resizer for chrome extension

## Required
- Python 3.9+
- Conda (optional)


## How to use
### Local setup
- I assume you have python 3.9+ installed and conda installed
```
$ make env
$ conda activate 99-image-resizer
$ make setup
```

### Before run
- Icons should generally be in PNG format
- They can, however, be in any format supported by WebKit, including BMP, GIF, ICO, and JPEG.
- 16x16 / 48x48 / 128x128
```
"icons": { "16": "icon16.png",
           "48": "icon48.png",
          "128": "icon128.png" },
```


### Run
```
$ python main.py --image-path <image_path> --output-path <output_path>

# Example
$ python main.py --image-path ./samples/image.jpeg --output-path ./results

```