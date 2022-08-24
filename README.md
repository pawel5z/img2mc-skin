# img2mc-skin

A Python program pasting chosen image into Minecraft skin.

## Prerequisites

Choose any of the following.

<details>
<summary>Global Python installation</summary>

```
pip3 install pillow numpy
```

</details>

<details>
<summary>Python virtual environment</summary>

```
python3 -m venv pyenv
source pyenv/bin/activate
pip3 install -r requirements.txt
```

</details>

## Usage

```
usage: img2skin.py [-h] [-o OUT] [-t TEMPLATE | -c COLOR] front back

positional arguments:
  front                 Image that will be in front of the skin.
  back                  Image that will in the back of the skin.

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     File name the skin will be saved to.
  -t TEMPLATE, --template TEMPLATE
                        Optional skin template. If absent, a default one will be used.
  -c COLOR, --color COLOR
                        Set the fill color of skin's sides. Provided in hex format: rrggbbaa.
```
