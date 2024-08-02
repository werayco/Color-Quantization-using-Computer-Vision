## What this project is all about
in layman's term, Image Quantization is a technique which is used to reduce the number of colors in an image
## How to run the code
Run the "Quantization.py" in your terminal



## how the 'dvc workflow' works
- run this code in your terminal: dvc stage add -n quantization -d Quantization.py -o quantized_image.py python Quantization.py
- after that, a "dvc.yml" file will be created in your directory
- then run this also in your terminal: dvc repro
