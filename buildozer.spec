# ======================================================
# BUILDOZER SPEC - EduKids App Configuration
# For APK/AAB Build and Google Play Publishing
# ======================================================

[app]

# Basic app details
title = EDUKIDS: THE VAULT
package.name = edukids
package.domain = org.edukids

# Source and version
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,requests,jnius

# Permissions for monetization and network
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# AdMob Configuration
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-6872596196321341~0000000000

# Build configuration
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Orientation
orientation = portrait

# Icon and presplash
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Keystore for signing (IMPORTANT: Generate your own!)
# android.keystore = 1
# android.keystore_path = /path/to/my-release-key.keystore
# android.keystore_alias = my-key-alias
# android.keystore_passwd = your-keystore-password

[buildozer]

log_level = 2
warn_on_root = 1
