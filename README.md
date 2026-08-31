# Splatoon Raiders - Awlmun Den Crates-Only Macro

> 中文说明在下方 / Chinese version below

This repository contains a tested `code.py` for automatically farming **weapon drops from the crates in Awlmun Den (Super Spicy)** using an RP2040 and CircuitPython.

It is based on the RP2040 / Switch HID implementation from:

https://github.com/Deathm0b/splatoon-raiders-macro

Please refer to the original repository for setup.

This repository only provides the **Awlmun Den farming `code.py`**.

## What it does

The script repeatedly:

1. Enters **Awlmun Den - Super Spicy**
2. Moves to the crate area
3. Breaks the weapon crates
4. Exits the raid
5. Re-enters the stage
6. Repeats

This route is intended specifically for **weapon farming**

## Tested setup

The script has been successfully tested with:

- Nintendo Switch 2
- RP2040-Zero
- CircuitPython
- Awlmun Den - Super Spicy

## Installation

First complete the setup from the original project:

https://github.com/Deathm0b/splatoon-raiders-macro

Then replace the existing:

```text
code.py
