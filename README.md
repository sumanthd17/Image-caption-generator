# Image Caption Generator

### The goal of the project is to generate captions for images by learning visual representations from Images

## Implementation: 
> MS COCO dataset has 5 captions for each image in the dataset. These are rich dense captions which contains information about the image (descriptive and positional). This project used a ResNet50 backbone for obtaining the visual features and LSTM Decoder for generating the captions.

## Dataset
> MS COCO - Image Captioning Dataset

## Task List
 - [x] Generate caption with CNN Encoder & LSTM Decoder
 - [x] Create Web App for Inference
 - [ ] Use visual Attention

## Technology Stack:
> PyTorch

<!-- ## Install dependencies
``` pip install -r dev-requirements.txt ``` -->
## Acknowledgement:
- [Rupesh Somana](https://www.linkedin.com/in/rupesh-somana-9ab826173/) For the Web Interface

## Web Interface
![Web Interface](https://github.com/sumanthd17/Image-caption-generator/blob/master/ui.png?raw=true)

## Contributing ##
### Code Style ###

Code is formatted using the [black](https://github.com/ambv/black) style. Merges to master are prevented if code does not conform.

To apply black to your code, run black from the root Prefect directory:

```
black .
```
Formatting can be easy to forget when developing, so you may choose to install a pre-push hook for black, as follows:

```
pre-commit install --hook-type pre-push
```

Once installed, you won't be allowed to `git push` without passing black.

In addition, a number of extensions are available for popular editors that will automatically apply black to your code.