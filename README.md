# FBMarketHelper
FBMarketHelper is an simple web automation program that help you deal with the annoying "is this still available?" in facebook markpetlace

## Prepping envrioment
You'll need Google Chrome installed on your computer and the chrome webdriver where you can download [here](https://chromedriver.chromium.org/downloads)

You'll also need to add the chrome webdriver to your PATH, on Linux, you can do this by
```bash
PATH=$PATH:path_to_chrome_driver
```

## Configering
In the config.json file, you can adjust the settings of the program

The main field to change is the Email and Password field, replace them with your credentials to login to facebook messenger

## Running the program
```bash
python3 main.py
```

## How does this work?
The program login to facebook messenger and go to Facebook Marketplace chat.

The *TargetMsg* in *config.json* shows the substring the program tries to find, this is often "is this available?"

It constantly check (with small delay for performance) if the latest message of a conversation includes that substring

So if someone send your "Hi Samsara, is this still available?", that message would be the latest message of the conversation, which have the *TargetMsg* included as a substring, this will trigger the program and report a hit

When a hit happens, it will auto reply the *Respond* message in *config.json*, so you don't have to
