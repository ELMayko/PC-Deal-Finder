# PC Deal Finder

Searches 'buildapcsales' forum on Reddit.com for the latest pc component deals. If deals that match your search criteria are found, the script will automatically send you an email containing the search results.

## Getting Started

### Prerequisites

#### Register your script with Reddit

Follow [these](https://github.com/reddit-archive/reddit/wiki/oauth2) instructions under the 'Getting Started' section in order to create an application and receive a client id and secret for your application. This will allow Reddit to identify your application and grant it access to Reddit's API. Fill out the form as shown using 'pc deal finder v.1.0 (by /u/r_mcmichaels)' as the client agent and 'http://localhost:8080' for the redirect uri. Be sure to select 'script' for the app type.

![Create App]('/images/CreateApp.png')

Note: You must have a Reddit account in order to access Reddit's API


#### Change G-Mail account settings

To have your search results emailed to you, you must add your email credentials to the praw.ini file. This will allow the script to establish a connection and authenticate with google's SMTP server and compose emails to your own account.


 Note: For the script to work, you must change the security settings in your gmail account to allow access for less secure apps. This can be done by going to https://www.google.com/settings/security/lesssecureapps, going to the 'Less secure app access' section and clicking 'turn on access'.

![Less Secure App Setting]('/images/LessSecureAppSetting.png')

### Installing

Clone the repository then run pip command from the root directory to install dependencies 

```
$ pip -r install requirements.txt
```


### Usage
After installing dependencies and filling in the praw.ini file with the appropriate settings, run the script by typing into the command line within the project directory:

```
$ python3 -m main
```

You should see output such as this if the script finds matches:

```
$ python -m main  
Title: [RAM] G.SKILL Ripjaws V Series 16GB 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Desktop Memory Model F4-3200C16S-16GVK (1 x 16GB) $60.99 Price: $60.99
Title: [RAM] XPG Spectrix RGB DDR4 3600 CL18 - $79.99 + FS Price: $79.99
Title: [RAM] Team T-FORCE DARK Z 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3200 (PC4 25600) Intel XMP 2.0 Desktop Memory Model TDZRD416G3200HC16CDC01 $62.99 Price: $62.99  
```

And you can expect to see output such as this when no matches are found:

```
$ python -m main
No matches found for cpu under $200
```

## Running the tests

to run tests : 

```
$ python -m unittest test_dealfind.py
```

## Built With

* [PRAW](https://praw.readthedocs.io/en/latest/#) - Python Reddit Wrapper API


## Authors

* **Michael Marrero**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details