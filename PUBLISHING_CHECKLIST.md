# ======================================================
# PUBLISHING CHECKLIST - Google Play Store
# ======================================================

## STEP 1: PREPARE YOUR APP
- [x] Update app version in buildozer.spec
- [x] Test all features on Android device
- [x] Verify AdMob integration works
- [x] Test payment flow (PayPal)
- [x] Ensure app icon and presplash are ready

## STEP 2: ADMOB SETUP
- [ ] Go to https://admob.google.com
- [ ] Sign in with Google account
- [ ] Create AdMob account if needed
- [ ] Link Google Play Console account
- [ ] Create new app: "EDUKIDS: THE VAULT"
- [ ] Create ad units:
  - Banner Ad Unit ID: Replace "ca-app-pub-6872596196321341/xxxxxxxx"
  - Interstitial Ad Unit ID: Replace "ca-app-pub-6872596196321341/yyyyyyyy"
- [ ] Copy Publisher ID: pub-6872596196321341 (already in code)
- [ ] Create ads.txt file and upload to server

## STEP 3: GENERATE SIGNING KEY
```bash
keytool -genkey -v -keystore my-release-key.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias my-key-alias
```

## STEP 4: BUILD APK/AAB
```bash
buildozer android release
```

## STEP 5: GOOGLE PLAY CONSOLE
- [ ] Go to https://play.google.com/console
- [ ] Create new app: "EDUKIDS: THE VAULT"
- [ ] Fill app details:
  - Short description
  - Full description
  - Screenshots (5-8 recommended)
  - Feature graphic (1024x500)
  - Category: Education
  - Content rating questionnaire
- [ ] Add app icons and presplash
- [ ] Set pricing: FREE (with in-app purchases via PayPal)
- [ ] Target audience: Kids (4-12 years)
- [ ] Content rating: Everyone
- [ ] Privacy policy: https://your-domain.com/privacy
- [ ] Upload signed APK/AAB
- [ ] Review and submit

## STEP 6: COMPLIANCE
- [ ] Add privacy policy URL
- [ ] Ensure COPPA compliance (kids app)
- [ ] Verify payment gateway (PayPal)
- [ ] Check AdMob policies
- [ ] Review Google Play policies

## STEP 7: LAUNCH
- [ ] Set rollout percentage (start 10%, increase gradually)
- [ ] Monitor crash reports
- [ ] Check user ratings
- [ ] Respond to reviews

## MONETIZATION SETTINGS
- Banner Ads: Bottom of screens
- Interstitial Ads: Between level transitions
- Premium Access: R50 via PayPal
- Ad-free option: Can be added via premium

## IMPORTANT NOTES
- Replace "ca-app-pub-6872596196321341~0000000000" with your actual Google AdMob App ID
- Replace ad unit IDs with your actual unit IDs
- Test ads use: ca-app-pub-3940256099942544/6300978111 (banner test)
- Keep ads.txt updated and accessible at: yourdomain.com/ads.txt
