# Private Data
Use Accessibility.

# Audio
## Recording VOIP Calls
Summary: Available after Android 10, use accessibility and Voice_Recognition for recording. To detect VOIP calls, use notification.

* Challenge 1: Detecting VOIP Calls
  * Solution: Use notification. 
  * Code `channelID = statusBarNotification.getNotification().getChannelId();`

* Challenge 2: Recording via Microphone
  * Available after Android version 10, [which allows more than 1 device to use Microphone at the same time](https://developer.android.com/guide/topics/media/sharing-audio-input).
  * Request accessibility permission
  * Use `Voice_Recognition` in AudioSoruce

## Record Phone Calls
Summary: Before Android 6, native API. Android 6 - 8, use NDK. Android 9, the only work around is MIC. Android 10 above, use Accessibility to access Mic.

* Before Android 6: [Use official Android Recording API](https://issuetracker.google.com/issues/112602629).
  * Below Android 6: Worked fine on phones that supported VOICE_CALL
* Android 6 - 8: Use [NDK](https://github.com/rumblefishdev/CallRecLib/tree/develop) to set AudioSource parameter to VOICE_CALL. For Android 6, AudioSource = Mic seems to be working.
* Android 9: Can only record via MIC by running a foreground service. [This is because Google blocked NDK](https://android.googlesource.com/platform/frameworks/av/+/android-9.0.0_r30/services/audioflinger/AudioFlinger.cpp) and requires a [foreground service](https://developer.android.com/about/versions/pie/android-9.0-changes-all).
* Android 10+: [Use accessibility](https://developer.android.com/guide/topics/media/sharing-audio-input), [Voice_Recognition](https://stackoverflow.com/questions/58230181/call-recorder-not-working-in-android-10-q?noredirect=1&lq=1) (**Notice that it is unclear why this does not work on Android 9) and a foreground service.

## Environment Recording
* Start Microphone

## Spy Calls
Only works for certain cases. Why?



## On Demand Picture
* calls `obj2 = new ExecOnDemandImageCapture().execute(this.f768a);`
  * com.p024fp.appengine.p054a.ExecOnDemandImageCapture
    * calls `Intent intent = new Intent(context, RemoteCameraActivity.class);`

# 