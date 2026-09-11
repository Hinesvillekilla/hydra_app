[app]
title = Hydra
package.name = hydra
package.domain = com.hydra.app
source.dir =.
source.include_exts = py,png,jpg
version = 1.0
requirements = python3,kivy,pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = READ_MEDIA_IMAGES,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
