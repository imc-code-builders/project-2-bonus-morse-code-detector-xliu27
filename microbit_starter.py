from microbit import *
import music

morse_dict = {
    'dot-dash': 'A', 'dash-dot-dot-dot': 'B', 'dash-dot-dash-dot': 'C',
    'dash-dot-dot': 'D', 'dot': 'E', 'dot-dot-dash-dot': 'F',
    'dash-dash-dot': 'G', 'dot-dot-dot-dot': 'H', 'dot-dot': 'I',
    'dot-dash-dash-dash': 'J', 'dash-dot-dash': 'K', 'dot-dash-dot-dot': 'L',
    'dash-dash': 'M', 'dash-dot': 'N', 'dash-dash-dash': 'O',
    'dot-dash-dash-dot': 'P', 'dash-dash-dot-dash': 'Q', 'dot-dash-dot': 'R',
    'dot-dot-dot': 'S', 'dash': 'T', 'dot-dot-dash': 'U',
    'dot-dot-dot-dash': 'V', 'dot-dash-dash': 'W', 'dash-dot-dot-dash': 'X',
    'dash-dot-dash-dash': 'Y', 'dash-dash-dot-dot': 'Z',
    'dot-dash-dash-dash-dash': '1', 'dot-dot-dash-dash-dash': '2',
    'dot-dot-dot-dash-dash': '3', 'dot-dot-dot-dot-dash': '4',
    'dot-dot-dot-dot-dot': '5', 'dash-dot-dot-dot-dot': '6',
    'dash-dash-dot-dot-dot': '7', 'dash-dash-dash-dot-dot': '8',
    'dash-dash-dash-dash-dot': '9', 'dash-dash-dash-dash-dash': '0'
}

current_symbol = ''
message = []

while True:
    display.clear()
    



    # TASK 4: Shake to scroll the full message
    if accelerometer.was_gesture('shake'):
        full_text = ''.join(message)
        display.scroll(full_text)



    # TASK 2: Decode current_symbol when logo is touched
    if pin_logo.is_touched():
        if current_symbol != "":
            letter = morse_dict.get(current_symbol, "?")
            print(current_symbol)
            message.append(letter)
            current_symbol = ""
            display.show(letter)
            music.pitch(500)
            sleep(1000)
            music.stop()


    # TASK 1: Record dots and dashes (Button A = dot, Button B = dash)
    # Build current_symbol as a string like 'dot-dash-dot'
    elif button_a.was_pressed():
        if current_symbol == "":
            current_symbol = "dot"
        else:
            current_symbol += "-dot"
            
        display.show(Image('00000:'
                    '00000:'
                    '36963:'
                    '00000:'
                    '00000'))
        music.pitch(200)
        sleep(100)
        music.stop()
    

    elif button_b.was_pressed():
        if current_symbol == "":
            current_symbol = "dash"
        else:
            current_symbol += "-dash"
            display.show(Image('00300:'
                    '03630:'
                    '36963:'
                    '03630:'
                    '00300'))
            music.pitch(300)
            sleep(300)
            music.stop()

    # TASK 3: Add display and sound to each of the above