# zzz – sleep computer

Feeling tired? Why not stay up and hack together a machine to help you experience [lucid dreams](https://en.wikipedia.org/wiki/Lucid_dream).

![zzz in operation](https://github.com/mirthturtle/zzz/blob/main/bedside.jpg "zzz in operation")

`zzz` uses a trigger-style mouse to play distinctive sounds. Wear it during sleep and test your reality in dreams by squeezing your finger or thumb. If you hear the sounds, you can recognize that you're asleep and take control of the dream.

## Equipment

You will need:
- A [Raspberry Pi](https://www.raspberrypi.com/)
- An ergonomic handheld trigger mouse
- Speaker or headphones

## Setup

Clone the repo to your Pi. Install Python and dependencies:
```
sudo apt update
sudo apt install python3 python3-pip python3-pygame alsa-utils libasound2-plugins
Install python packages:
```
pip3 install pygame evdev
```
Depending on your Pi OS version you may need to add `--break-system-packages` here; this is fine if your Pi will be a dedicated `zzz` machine and you don't care about your Python environment; otherwise, create a virtual environment.

Put sounds in the `sound` directory and link them to your desired buttons in `zzz.py`.

Adjust volume with `alsamixer`.

Make run script executable: `chmod +x run.sh`

## Running

In the project directory:

`./run.sh`

Ctrl-C to exit.

Timestamped logs are collected in `sleep.log`.

## License

This program is licensed by GPL-3.0.
