import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Define your switches (update pins if needed)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = keyboard.COL2ROW

# Encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.GP5, board.GP6, None),  # CLK, DT, SW
)

# Keymap
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F
    ]
]

if __name__ == '__main__':
    keyboard.go()