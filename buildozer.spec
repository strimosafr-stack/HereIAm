[app]
title = Here I Am
package.name = hereiam
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,android
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1
android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, RECEIVE_SMS, READ_SMS
android.api = 31
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
