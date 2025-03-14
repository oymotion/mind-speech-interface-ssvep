# mind-speech-interface-ssvep

Mind-Speech Interface for NeuroTechX Student Clubs Competition 2022

![WLOUTRO_AdobeExpress (1)](https://user-images.githubusercontent.com/34819737/199123399-dfecfffb-84dd-4d42-a0aa-7affcd69d9f5.gif)

This repository includes offline data collection and analysis tools for SSVEP, trainable models for SSVEP prediction, as well as an SSVEP text/speech interface.

Platform Support: Currently our tools support Windows 10 and up. MacOS is technically supported but is not recommended. For Mac devices with ARM SOCs (M1, M2 etc) you will need to run our tools in a Rosetta emulated terminal.

## Credit

Some of our models and signal processing methods were adapted from the following repositories:

- <https://github.com/aaravindravi/Brain-computer-interfaces>

- <https://github.com/eugeneALU/CECNL_RealTimeBCI>

## Requirements

To install requirements, make sure you have Python 3.10 with virtual environment installed, then run

```python
pip install -r requirements.txt
```

Make sure to run the command from the base directory (mind-speech-interface-ssvep) of the Git repo

## General Hardware Setup

Our software tools support OYMotion EEG devices for EEG data capturing.

- <https://oymotion-developer.readthedocs.io/>

When setting up the device please make sure the channel numbers correspond to the following 10-20 electrode locations.
Note that this image is viewed as if you were looking at the back of someone's head.

![image](https://user-images.githubusercontent.com/34819737/178824314-7b1296b8-cdd2-424b-86ef-b65fec7e2d6e.png)

## OFFLINE SSVEP BCI

### Offline SSVEP Data Collection

To run the offline data-collection demo, copy and paste the following commands:

```python
cd mind-speech-interface-ssvep
```

Regardless of if you are or are not using active electrodes, continue here:

NOTE: SSVEP-Data-Collection/configs.py --> This is set to 8 by default. Open this file in a text editor and ensure the NUM_STIMS value is set to your desired # of stimuli (4 or 6 or 8), then save and exit.

Now you should be able to run the data collection tool!

for OYMotion OB5000-7H (7EEG+1ECG) channel

```python
python ./SSVEP-Data-Collection/run_demo.py --board-id=59 --mac-address=24:71:89:EF:27:8F --timeout=10
```

for OYMotion OB5000Max 8EEG channel

```python
python ./SSVEP-Data-Collection/run_demo.py --board-id=60 --mac-address=C4:64:E3:D8:E4:F1 --timeout=10
```

### Offline SSVEP Data Analysis

To visualize the csv created from data collection, in your terminal run:

```python
jupyter notebook
```

Then in the browser window navigate to the notebook under EEG-Data-Visualization:

![image](https://user-images.githubusercontent.com/34819737/177415768-4630ae1e-c9fb-4b94-b82f-02cc252556d5.png)

Insert the csv name of the recording you want to visualize in this section:

![image](https://user-images.githubusercontent.com/34819737/177419300-542e8df2-8f5a-4344-a61d-9f73770efc00.png)

Then click:

![image](https://user-images.githubusercontent.com/34819737/177414726-94eec197-3778-4231-90ac-487477b04ebf.png)

And averaged FFT plots of every stimuli response for each electrode will appear at the bottom and look like this:

![image](https://user-images.githubusercontent.com/34819737/177415446-e1ec3b81-8d0d-49e0-97e5-822074659387.png)

## FBCCA-KNN Model Training/Testing

Training models is relatively simple using the training script!

The only default parameters to pass would be:

- data: The path to your data. The data path can be a folder of folders of csvs or a path to the csv itself. Both should be fine.
- output-path: The directory where a model will be saved.
- output-name: The name of the saved model.
- model-type: Specify the type of model to train here.
- window-length: Window length of example taken from particular trial.
- shift-length: Shift between example windows.

The window and shift lengths exist to allow us to manufacture more unique examples the KNN can train on.

There are some handy flags:

- train: Whether to train a model
- eval: Whether to evaluate model using train/test split.
- verbose: Whether to output metrics information like accuracy and a confusion matrix to the terminal.

To train a FBCCA-KNN model, navigate to `mind-speech-interface-ssvep/` and run

```python
python -m eeg_ai_layer.models.train --data=<YOUR_DATA_PATH> --train --output-path=<YOUR_MODEL_OUTPUT_PATH> --output-name=<YOUR_MODEL_NAME> --model-type=fbcca_knn --shift-length=<SECONDS> --window-length=<SECONDS> --no-zero
```

If you'd like to see some metrics, pass the `--verbose` flag like so:

```python
python -m eeg_ai_layer.models.train --data=<YOUR_DATA_PATH> --train --output-path=<YOUR_MODEL_OUTPUT_PATH> --output-name=<YOUR_MODEL_NAME> --model-type=fbcca_knn --shift-length=<SECONDS> --window-length=<SECONDS> --no-zero --verbose 
```

For example:
python -m eeg_ai_layer.models.train --data=./SSVEP-Data-Collection/demo_data/073_2025_435217.csv --train --output-path=./savedmodels --output-name=test1 --model-type=fbcca_knn --shift-length=0.1 --window-length=0.4 --no-zero

## ONLINE SSVEP BCI

### GPT-3 API Key Setup

In order to use GPT-3, create a ```.env``` file within the mind-speech-interface-ssvep folder.

Within this document create a variable called ```OPENAI_KEY```, and set it to your OpenAI API key. Ensure that the key is in quotation marks.

Now, GPT-3 should work with the SSVEP GUI!

### Twitter API Key Setup

To use the twitter api refer to the readme in "mind-speech-interface-ssvep/SSVEP-Interface/server/".

### Text To Speech Setup

Please follow the readme in "mind-speech-interface-ssvep/SSVEP-Interface/_TTS/".

This feature allows you to train a voice model on samples of your own voice to use with the interface. It is not required for operation of the GUI.

### Speech To Text WebApp for Prompt Input

Please follow the readme in "mind-speech-interface-ssvep/SSVEP-Interface/web-app/".

### Online SSVEP Interface

After ensuring GPT-3, Twitter, and TTS features are setup, you will be ready to run our fully integrated SSVEP interface, copy and paste the following commands:

```python
cd mind-speech-interface-ssvep
```

#### for OYMotion OB5000MAX (8EEG) channel

```python
python ./SSVEP-Interface/Data_Streamer.py --model-type=fbcca --board-id=59 --mac-address=24:71:89:EF:27:8F --timeout=10
```

#### Alternatively1

```python
python ./SSVEP-Interface/Data_Streamer.py --model-type=fbcca_knn --board-id=59 --mac-address=24:71:89:EF:27:8F --timeout=10
```

#### Alternatively2

```python
python ./SSVEP-Interface/Data_Streamer.py --model-type=fbcca_knn --model-path=eeg-ai-layer/models/savedmodels/modelname.model  --board-id=60 --mac-address=C4:64:E3:D8:E4:F1 --timeout=10
```
