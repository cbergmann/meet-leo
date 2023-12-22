def on_gesture_screen_down():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            849,
            1,
            255,
            0,
            1000,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_logo_touched():
    record.set_mic_gain(record.AudioLevels.LOW)
    record.start_recording(record.BlockingState.NONBLOCKING)
    while input.logo_is_pressed():
        led.plot_bar_graph(input.sound_level(), 255)
        basic.pause(5)
    music.stop_all_sounds()
    basic.clear_screen()
    record.play_audio(record.BlockingState.BLOCKING)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    if mode == "s":
        radio.send_string("Leo")
    else:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global mode
    mode = "r"
    basic.show_string(mode)
    start()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_gesture_shake():
    basic.show_leds("""
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        """)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            3041,
            3923,
            59,
            255,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_leds("""
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    if input.light_level() > 50:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
    else:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            . . # # .
            . . . # #
            . . . # #
            . . . # #
            . . # # .
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global mode
    mode = "s"
    basic.show_string(mode)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def start():
    if mode != "s":
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
            SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HEART)
mode = ""
# Switch between modes r = recieve, s = send
mode = "r"
radio.set_group(1)
pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
if input.button_is_pressed(Button.A):
    # Switch between modes r = recieve, s = send
    mode = "s"
start()