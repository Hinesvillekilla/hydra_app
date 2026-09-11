[app]
title = Hydra
package.name = hydra
package.domain = com.hydra.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
p4a.whitelist = libffi,openssl,sqlite3
android.gradle_dependencies =

[buildozer]
log_level = 1
warn_on_root = 1
