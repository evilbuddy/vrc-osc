# VRC-OSC
Yet another OSC program, but now in Python !

# How to use ?
1. Clone the repo (`git clone https://github.com/evilbuddy/vrc-osc.git`)
2. Write the modules you want to use in `modules.txt`
    - All the modules are in `modules/` as Python files (`.py`)
    - Each module might have dependencies, check for `import`s !
    - example:
         ```
        hwinfo
        hyprland
        ```
        This will import `hwinfo.py` and `hyprland.py` from the modules folder
3. Change the `text.txt` to what you want the chatbox to be
    - All the modules should contain info about the keys they replace !
4. Install the dependencies (using `pip` or your Linux distro's package manager !)
    - python-osc
5. Run `main.py` (`python main.py`)
    - See `main.py --help` for the command-line arguments

# How to write modules ?
Each module is a Python file in the `modules/` folder.

Every module should import `vrcosc`, as it contains str_replace_bulk(), which is the easiest way to integrate your module with the others.

For the program to use your module, you need a `format(text)` function that will return the modified text.

Please, at the beginning of your module, add the dependencies (if necessary) and keys with their usage:
```python
# mymodule
#
# Dependencies:
#   libcool
#
# Keys:
#   {my_key}    Shows cool stuff !
```

Modules can also contain an init function, that will be ran upon loading the module.

Use the built-in modules as examples !
