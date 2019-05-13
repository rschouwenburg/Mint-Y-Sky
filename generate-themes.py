#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

def x_colorize_directory (path, variation):
    for accent in X_HEX_ACCENTS:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, x_hex_colors[variation]))
    for accent in X_RGB_ACCENTS:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, x_rgb_colors[variation]))

def y_colorize_directory (path, variation):
    for accent in Y_HEX_ACCENT1:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors1[variation]))
    for accent in Y_HEX_ACCENT2:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors2[variation]))
    for accent in Y_HEX_ACCENT3:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors3[variation]))
    for accent in Y_HEX_ACCENT4:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors4[variation]))

os.system("mkdir -p usr/share/themes")

# Mint-Y
Y_HEX_ACCENT1 = ["#4095ff"]  # BASE
Y_HEX_ACCENT2 = ["#90b4ed"]
Y_HEX_ACCENT3 = ["#4095ff"]  # PRELIGHT/HOVER
Y_HEX_ACCENT4 = ["#4095ff"]  # PRESSED

curdir = os.getcwd()

#os.chdir("src/Mint-Y")
os.system("./build-themes.py")
os.chdir(curdir)
