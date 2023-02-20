# zoom-recording-downloader

Zoom bulk recording downloader using JWT Authentication

Get JWT token here https://marketplace.zoom.us/develop/create

configuration that should be changed are in akun.py

multiple account at once currently not available, please enable only one jwt token

## Installation ##

_Attention: You will need [Python 3.6](https://www.python.org/downloads/) or greater_

```sh
$ git clone https://github.com/PGRjoystick/zoom-recording-downloader.git
$ cd zoom-batchdl
$ pip3 install -r requirements.txt
```
## Running ##

Edit a file **akun.py** and paste your JWT token under `JWT_TOKEN` variable:

    JWT_TOKEN = 'PASTE_TOKEN_DISINI'

- Set these variables to the earliest recording date you wish to download, within a six month period (default is June 17st, 2020)

      RECORDING_START_YEAR = 2020
      
      RECORDING_START_MONTH = 6
      
      RECORDING_START_DAY = 17

- Specify the folder name where the recordings will be downloaded (default = account1).

      DOWNLOAD_DIRECTORY = 'account1'

Run command:

```sh
python3 zoom-recording-downloader.py
```
