# macOS Launchd Run-As-User Starter Script

## Description

This is a universal Python starter script designed for running Python code as a specified user within a specific virtual environment. It is particularly useful for macOS users who wish to integrate Python scripts with `launchd`.

## How it Works

The script takes four or more command-line arguments:

1. `username`: The username under which the script should be executed.
2. `venv-python-path`: The path to the Python interpreter in the virtual environment.
3. `python-script`: The path to the Python script that should be executed.
4. `[arg1, arg2, ...]`: Additional arguments to pass to the Python script.

It sets up the environment for the specified user and runs the Python script within that user's context.

## Usage

Run the script like so:

```bash
python starterscript.py <username> <venv-python-path> <python-script> [arg1 arg2 ...]
```

## Example: Monitoring ~/Downloads using launchd

You can use this script to monitor a folder, such as `~/Downloads`, and trigger an action when something changes. Create a `.plist` file under `~/Library/LaunchAgents/`, for example, `com.example.monitorDownloads.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.example.monitorDownloads</string>

  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python</string>
    <string>/path/to/starterscript.py</string>
    <string>username</string>
    <string>/path/to/.venv/bin/python</string>
    <string>/path/to/your/script.py</string>
  </array>

  <key>WatchPaths</key>
  <array>
    <string>/Users/username/Downloads/</string>
  </array>

  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
```

Remember to replace `/path/to/starterscript.py`, `username`, `/path/to/.venv/bin/python`, and `/path/to/your/script.py` with your actual paths and username.

After creating the `.plist` file, load it:

```bash
launchctl load ~/Library/LaunchAgents/com.example.monitorDownloads.plist
```

Now, your `launchd` service is set up to monitor the `~/Downloads` folder and will execute your Python script when any change occurs.
