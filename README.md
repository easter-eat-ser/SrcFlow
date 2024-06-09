# SrcFlow
## GUI for converting images to 8-bit and sending them to QLumpy

Don't expect too much - this was just recently released, and has some issues that need to be ironed out(Linux support, better design, detecting path validity, a proper file picker...)
SrcFlow does not implement dithering. If this is a requirement for you, use a program like IrfanView to dither and convert your images to 8-bit before putting them into SrcFlow.

### Some fixes for issues you might have:
- Make sure the ends of your file paths don't have slashes, and that you use backslashes
- The WAD path should include the name of your wad without the extension, e.g. C:\Half-Life\valve\textures instead of C:\Half-Life\valve\textures.wad
- Install the 'Image' package with `pip install Image` or 'python3 -m pip install --upgrade Pillow'
- Compare your config to mine
  ![image](https://github.com/easter-eat-ser/SrcFlow/assets/130861513/c7ed815c-259b-4fe7-b1db-38baa7f17040)
