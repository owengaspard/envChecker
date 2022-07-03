# envChecker
Python library to check your `.env` for missing variables by checking against `.env.example`.

# How to Install
```
pip install envchecker
```

## How to use
You can import the library and the checker function with these two lines:
```
import envChecker
from envChecker import envCheck
```

You can call the envChecker using this line:
```
envCheck.check()
```

## Licnese and Contributing
This repository is loosely based off the [Reddit Video Maker by Lewis Menelaws](https://github.com/elebumm/RedditVideoMakerBot) (specifically `checker.py`) which uses the GPL-3.0 license. In turn, this repository also uses the GPL-3.0 license. This means you are permitted to do anything you want with this code as long as you acknowledge that:
- There is NO warranty whatsoever
- No one but you is liable for anything you do with this
- If you choose to fork this repository or use any code in it, you MUST state your changes, give credit to the original work, use the same license, and give a disclaimer about the license.

If you would like to contribute, go ahead! Please make any PRs to the `development` branch so that it can serve as a place to test and improve before it goes to `main`.
