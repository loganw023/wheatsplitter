import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.D0, board.D1, board.D2, board.D3, board.D4,
)
keyboard.row_pins = (
    board.D10, board.D9, board.D8, board.D7, board.D6,
)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [
        KC.A,    KC.B,    KC.C,    KC.D,    KC.E,
        KC.F,    KC.G,    KC.H,    KC.I,    KC.J,
        KC.K,    KC.L,    KC.M,    KC.N,    KC.O, 
        KC.P,    KC.Q,    KC.R,    KC.S,    KC.T,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,
    ]
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.NKRO)