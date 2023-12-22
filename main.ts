input.onGesture(Gesture.ScreenDown, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 849, 1, 255, 0, 1000, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    basic.showIcon(IconNames.Asleep)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    record.setMicGain(record.AudioLevels.Low)
    record.startRecording(record.BlockingState.Nonblocking)
    while (input.logoIsPressed()) {
        led.plotBarGraph(
        input.soundLevel(),
        255
        )
        basic.pause(5)
    }
    music.stopAllSounds()
    basic.clearScreen()
    record.playAudio(record.BlockingState.Blocking)
})
input.onButtonPressed(Button.A, function () {
    if (mode == "s") {
        radio.sendString("Leo")
    } else {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.spring), SoundExpressionPlayMode.InBackground)
        basic.showIcon(IconNames.Happy)
    }
})
input.onPinPressed(TouchPin.P2, function () {
    mode = "r"
    basic.showString(mode)
    start()
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 3041, 3923, 59, 255, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
    basic.showLeds(`
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    if (input.lightLevel() > 50) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
    } else {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerDown), music.PlaybackMode.InBackground)
        basic.showLeds(`
            . . # # .
            . . . # #
            . . . # #
            . . . # #
            . . # # .
            `)
    }
})
radio.onReceivedString(function (receivedString) {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.InBackground)
    basic.showIcon(IconNames.Sad)
})
input.onPinPressed(TouchPin.P1, function () {
    mode = "s"
    basic.showString(mode)
})
function start () {
    if (mode != "s") {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.InBackground)
    }
    basic.showIcon(IconNames.Heart)
}
let mode = ""
// Switch between modes r = recieve, s = send
mode = "r"
radio.setGroup(1)
pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
if (input.buttonIsPressed(Button.A)) {
    // Switch between modes r = recieve, s = send
    mode = "s"
}
start()
