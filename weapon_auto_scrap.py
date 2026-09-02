import time
import usb_hid

# Safety net: Ensure boot.py worked before trying to grab the gamepad
try:
    gamepad = usb_hid.devices[0]
except IndexError:
    print("Gamepad not found. Check boot.py!")
    while True:
        time.sleep(1) 

# Helper function to tap buttons cleanly
def tap_button(btn_0=0, btn_1=0, dpad=8, lx=128, ly=128, rx=128, ry=128, press_time=0.1, wait_time=0.1):
    report = bytearray(8)
    report[0] = btn_0
    report[1] = btn_1
    report[2] = dpad
    report[3] = lx   # Left Stick X (0=Left, 128=Center, 255=Right)
    report[4] = ly   # Left Stick Y (0=Up, 128=Center, 255=Down)
    report[5] = rx
    report[6] = ry  # Right Stick Y (Center)
    
    # Press
    gamepad.send_report(report)
    time.sleep(press_time)
    
    # Release everything (D-pad 8 is neutral)
    # Release / center everything
    report[0] = 0
    report[1] = 0
    report[2] = 8
    report[3] = 128
    report[4] = 128
    report[5] = 128
    report[6] = 128
    gamepad.send_report(report)
    time.sleep(wait_time)

# ==========================================
# 1. THE PLUG-IN DELAY
# Wait 5 seconds to ensure the Nintendo Switch has fully 
# registered the USB device before sending inputs.
# ==========================================
time.sleep(5.0)

Y  = 1
B  = 2
A  = 4
X  = 8
L  = 16
R  = 32
ZL = 64
ZR = 128

MINUS = 1
PLUS  = 2
L3    = 4
R3    = 8

DPAD_UP    = 0
DPAD_RIGHT = 2
DPAD_DOWN  = 4
DPAD_LEFT  = 6
DPAD_NONE  = 8

# ==========================================
# 2. CONNECTION WAKE-UP SEQUENCE
# ==========================================
# Press A to connect the controller
tap_button(btn_0=A, press_time=0.1, wait_time=1.5)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, press_time=0.1, wait_time=3.0)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, press_time=0.1, wait_time=3.0)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, press_time=0.1, wait_time=1.0)
tap_button(btn_0=A, press_time=0.1, wait_time=1.0)

# ============================================================
# Infinite crates-only farm
# ============================================================

target_round = 200
counter = 0

while True:
    
    # Start Super Spicy Awlmun Den.
    tap_button(btn_0=A, press_time=0.1, wait_time=2)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=8)
    
    # Aim at the first crate group
    tap_button(rx=255, press_time=0.45, wait_time=0.1)
    
    # Jump
    tap_button(btn_0=B,  press_time=0.1, wait_time=0.25)
    
    # Armor jump
    tap_button(btn_0=B,  press_time=0.1, wait_time=0.1)
    
    # Jump Bomb twice
    tap_button(btn_0=L, ly=0, press_time=0.1, wait_time=0.25)

    tap_button(btn_0=L, ly=0, press_time=0.1, wait_time=0.1)

    # Dash Bomb twice
    tap_button(btn_0=R, ly=0, press_time=0.1, wait_time=1)

    tap_button(btn_0=R, ly=0, press_time=0.1, wait_time=0.1)

    # Floating
    tap_button(
        ly=0,
        press_time=2.5, wait_time=0.20
    )
    
    # Shot Pot twice quickly and wait a little
    tap_button(btn_0=A, press_time=0.1, wait_time=0.1)
    tap_button(btn_0=A, press_time=0.1, wait_time=6)

    # Back to base routine
    tap_button(btn_1=PLUS, press_time=0.1, wait_time=0.7)
    
    tap_button(dpad=DPAD_DOWN, press_time=0.1, wait_time=0.7)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
    
    tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=5.5)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=1.2)
    
    tap_button(btn_0=A, press_time=0.2, wait_time=1.2)
    
    counter+=1
    
    if counter == target_round:
        # scrap
        tap_button(btn_0=X, press_time=0.1, wait_time=0.7)
        tap_button(dpad=DPAD_DOWN, press_time=0.1, wait_time=0.7)
        tap_button(dpad=DPAD_DOWN, press_time=0.1, wait_time=0.7)
        tap_button(dpad=DPAD_DOWN, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=2)
        tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=X, press_time=0.1, wait_time=0.7)
        # *
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        # **
        tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        # ***
        tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        # ****
        tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        # select all
        tap_button(dpad=DPAD_DOWN, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
        
        # confirm
        tap_button(btn_1=PLUS, press_time=0.1, wait_time=0.7)
        tap_button(dpad=DPAD_RIGHT, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=A, press_time=0.1, wait_time=5)
        
        tap_button(btn_0=B, press_time=0.1, wait_time=0.7)
        tap_button(btn_0=B, press_time=0.1, wait_time=0.7)
        counter = 0
        
    tap_button(btn_0=X, press_time=0.1, wait_time=0.7)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=0.7)
    
    tap_button(btn_0=A, press_time=0.1, wait_time=0.7)

