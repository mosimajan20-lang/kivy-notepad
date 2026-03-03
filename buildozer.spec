[app]
title = Kivy Notepad
package.name = kivynotepad
package.domain = org.mosim
source.dir = .
source.include_exts = py,png,jpg,kv

# FIX 1: Must explicitly name your entry point.
# Buildozer defaults to main.py — rename kivy-notepad.py → main.py
# Hyphens in Python filenames break imports and p4a compilation.
source.main = main.py

version = 0.1

# FIX 2: cython is required — python-for-android uses it to compile
# Kivy's native C extensions (graphics, input, etc.)
requirements = python3,kivy,cython

orientation = portrait

# FIX 3: Android API / NDK settings are REQUIRED.
# Without these, buildozer picks wrong or stale defaults → return 1
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# Accept SDK licenses automatically inside the build environment
android.accept_sdk_license = True

[buildozer]
log_level = 2
