[app]
title = Hydra
package.name = hydra
package.domain = com.hydra.hydra
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.fork = kivy
p4a.branch = v2023.9.16

[buildozer]
log_level = 2
warn_on_root = 1
