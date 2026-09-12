[app]

# (str) Title of your application
title = Hydra

# (str) Package name
package.name = hydra

# (str) Package domain
package.domain = com.hydra.hydra

# (str) Source code where the main.py live
source.dir =.

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientation
orientation = portrait

# (int) Display file
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept SDK license
android.accept_sdk_license_agreement = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Buildozer working directory
warn_on_root = 1
