# Tooling
## Decompilation Tool
* JADX
  * Can't make it show byte code
* APKDeguard
  * Looks legit too (show byte code)
* APK-tools (to smali) + dex2jar (smali to Java)
* Enjarify with JD-GUI
  * Looks legit (shows byte code)

## Analysis Tools
* JEB
  * https://www.pnfsoftware.com/jeb/manual/android/

## Analyze .so file
* Ghidra

## Signing APKs
* Sign.jar

## Android Malware Analysis
* quark-engine
* MobileAudit
* AndroPyTool

## Dynamic Analysis Tool
* Frida
* QBDI


# Fundamentals Review
* Android applications are in the APK file format. APK is basically a ZIP file. (You can rename the file extension to .zip and use unzip to open and see its contents.)
* APK Contents (Not exhaustive)
  * AndroidManifest.xml
  * META-INF/
    * Certificate lives here!
  * classes.dex
        * Dalvik bytecode for application in the DEX file format. This is the Java (or Kotlin) code that the application will run by default.
  * lib/
    * Native libraries for the application, by default, live here! Under the lib/ directory, there are the cpu-specific directories. Ex: armeabi, mips,
* assets/
  * Any other files that may be needed by the app.
  * Additional native libraries or DEX files may be included here. This can happen especially when malware authors want to try and “hide” additional code, native or Dalvik, by not including it in the default locations.

# Dalvik & Smali
Most Android applications are written in Java. Kotlin is also supported and interoperable with Java. For ease, for the rest of this workshop, when I refer to “Java”, you can assume that I mean “Java or Kotlin”. Instead of the Java code being run in Java Virtual Machine (JVM) like desktop applications, in Android, the Java is compiled to the Dalvik Executable (DEX) bytecode format. For earlier versions of Android, the bytecode was translated by the Dalvik virtual machine. For more recent versions of Android, the Android Runtime (ART) is used.

If developers, write in Java and the code is compiled to DEX bytecode, to reverse engineer, we work the opposite direction.

![ReverseFlow](https://www.ragingrock.com/AndroidAppRE/images/ReversersFlow.jpg)

Smali is the human readable version of Dalvik bytecode. Technically, Smali and baksmali are the name of the tools (assembler and disassembler, respectively), but in Android, we often use the term “Smali” to refer to instructions. SMALI is like the assembly language: between the higher level source code and the bytecode.

For the following Hello World Java code:
```java
public static void printHelloWorld() {
	System.out.println("Hello World")
}
```

The Smali code would be:
```smali
.method public static printHelloWorld()V
	.registers 2
	sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;
	const-string v1, "Hello World"
	invoke-virtual {v0,v1}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
	return-void
.end method
```

Most often when reverse engineering Android applications, you will not need to work in Smali. Most applications can be lifted to an even higher level, decompiled Java. Like all tools, Java decompilers may have bugs. My suggestion to you is that whenever the decompiled Java output looks questionable, look at the Smali output. Work line by line with the instruction reference to figure out what the code is doing.

To get the Smali from DEX, you can use the baksmali tool (disassembler) available at [here](https://github.com/JesusFreke/smali/wiki). The smali tool will allow you to assemble smali back to DEX.

# Application Entry Points
One of the most important points of reverse engineering is knowing where to begin your analysis and entry points for code execution is an important part of that.

## Launcher Activity
The launcher activity is what most people think of as the entry point to an Android application. The launcher activity is the activity that is started when a user clicks on the icon for an application. You can determine the launcher activity by looking at the application’s manifest. The launcher activity will have the following MAIN and LAUNCHER intents listed.

Keep in mind that **not every application will have a launcher activity**, especially apps without a UI. Examples of applications without a UI (and thus a launcher activity) are pre-installed applications that perform services in the background, such as voicemail.
```xml
<activity android:name=".LauncherActivity">
	<intent-filter>
    	<action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

## Services
[Services](https://developer.android.com/guide/components/services) run in the background without a UI. There are a myriad of ways that they can be started and thus are an entry point for applications. The default way that a service can be started as an entry point to an application is through `Intents`.

When the `startService` API is called to start a Service, the `onStart` method in the Service is executed.

## Broadcast Receivers
Broadcasts can be thought of a messaging system and broadcast receivers are the listeners. If an application has registered a receiver for a specific broadcast, the code in that receiver is executed when the system sends the broadcast. There are 2 ways that an app can register a receiver: in the app’s Manifest or dynamically registered in the app’s code using the `registerReceiver()` API call.

In both cases, to register the receiver, the intent filters for the receiver are set. These intent filters are the broadcasts that should trigger the receiver.

When the specific broadcasts are sent that the receiver is registered for are sent, `onReceive` in the `BroadcastReceiver` class is executed.


## Exported Components (Services & Activities)
Services and Activities can also be “exported”, which allows other processes on the device to start the service or launch the activity. The components are exported by setting an element in the manifest like below. By default, android:exported="false" unless this element is set to true in the manifest or intent-filters are defined for the Activity or Service.
```xml
<service android:name=".ExampleExportedService" android:exported="true"/>
<activity android:name=".ExampleExportedActivity" android:exported="true"/>
```



# Starting Points for RE
One of the main keys of reverse engineering, regardless of platform, that all reverse engineers need to do, is figure out where to start their analysis. As a reverse engineer, when you’ve decided that your next step to solve your problem/answer your question is to use static analysis, then you need to know where you want to begin the static analysis.
* Android applications can be very large and realistically, you likely won’t be able to review every line of code. So where do you begin? My guidance when deciding where to begin doing static analysis is:
* What is your goal? In most cases, you are doing RE/static analysis to answer a specific question. Remember what that is and go back to it often. It’s very easy to go down a rabbit hole of code that is not related to the problem you’re trying to solve.
* API Calls Most interesting behaviors that you may want to identify in Android, ultimately come down to a single, or a set of API calls. For example, let’s say you’re evaluating an application to see if it’s doing Premium SMS Fraud. Premium SMS Fraud means that an app is sending a premium SMS message without user consent. Therefore, to do the fraud, the app must send an SMS message. There’s a finite number of API calls that will allow an application to send an SMS message. For example, `sendTextMessage`, `sendMultipartMessage,smsto`:. Therefore one of the key places to begin analysis, is to find the API calls that are required for the behavior you’re interested in, and then search for them in your application. You can then begin your reversing around those API calls.
* App Entry Points In many cases, you’re only interested in code that can be executed, not dead code, in the application. Therefore, starting at an application entry point (detailed in this section) is a good choice if you’re not sure where else to start.
* Decryption Methods Java largely relies on strings to do many of its operations. For example, to send intents or call methods through reflection. If your application has no human readable strings, then it likely means its obfuscated or encrypted. A good starting point is to find if **either “jumbled” strings or binary arrays are all passed to the same methods**. If they are, those methods are likely the deobfuscation or decryption methods.



# Native Code
Android applications can contain compiled, native libraries. Native libraries are code that the developer wrote and then compiled for a specific computer architecture. Most often, this means code that is written in C or C++. The benign, or legitimate, reasons a developer may do this is for mathematically intensive or time sensitive operations, such as graphics libraries. Malware developers have begun moving to native code because reverse engineering compiled binaries tends to be a less common skillset than analyzing DEX bytecode. This is largely due to DEX bytecode can be decompiled to Java whereas native, compiled code, often must be analyzed as assembly.

# Java Native Interface (JNI)
The Java Native Interface (JNI) allows developers to declare Java methods that are implemented in native code (usually compiled C/C++). JNI interface is not Android-specific, but is available more generally to Java applications that run on different platforms.

The Android Native Development Kit (NDK) is the Android-specific toolset on top of JNI. According to the docs:
```
In Android, the Native Development Kit (NDK) is a toolset that permits developers to write C and C++ code for their Android apps.
```

Together, JNI and NDK allow Android developers to implement some of their app’s functionality in native code. The Java (or Kotlin) code will call a Java-declared native method which is implemented in the compiled, native library.

# Analyzing Android Native Libraries
Android native libraries are included in APKs as .so, shared object libraries, in the ELF file format. If you have analyzed Linux binaries previously, it’s the same format.

These libraries by default are included in the APK at the file path /lib/cpu/libname.so. This is the default path, but developers could also choose to include the native library in /assets/custom_name if they so choose. More often, we are seeing malware developers choose to include native libraries in paths other than /lib and using different file extensions to attempt to "hide" the presence of the native library.

Because native code is compiled for specific CPUs, if a developer wants their app to run on more than 1 type of hardware, they have to include each of those versions of the compiled, native library in the application. The default path mentioned above, includes a directory for each cpu type officially supported by Android.
* "generic" 32-bit ARM: lib/armeabi/libcalc.so
* x86:lib/x86/libcalc.so
* x64:lib/x86_64/libcalc.so
* ARMv7:lib/armeabi-v7a/libcalc.so
* ARM64:lib/arm64-v8a/libcalc.so

# Loading the Library
Before an Android app can call and execute any code that is implemented in a native library, the application (Java code) must load the library into memory. There are two different API calls that will do this:
```java
System.loadLibrary("calc")
// or
System.load("lib/armeabi/libcalc.so")
```
The difference between the two api calls is that loadLibrary only take takes the library short name as an argument (ie. `libcalc.so` = `calc` & `libinit.so` = `init`) and the system will correctly determine the architecture it’s currently running on and thus the correct file to use. On the other hand, load requires the full path to the library. This means that the app developer has to determine the architecture and thus the correct library file to load themselves.

When either of these two (loadLibrary or load) APIs are called by the Java code, the native library that is passed as an argument executes its `JNI_OnLoad` if it was implemented in the native library.

To reiterate, before executing any native methods, the native library has to be loaded by calling `System.loadLibrary` or `System.load` in the Java code. When either of these 2 APIs is executed, the `JNI_OnLoad` function in the native library is also executed.

# The Java to Native Code Connection
In order to execute a function from the native library, there must be a Java-declared native method that the Java code can call. When this Java-declared native method is called, the "paired" native function from the native library (ELF/.so) is executed.

A Java-declared native method appears in the Java code as below. It appears like any other Java method, except it includes the native keyword and has no code in its implementation, because its code is actually in the compiled, native library.

```java
public native String doThingsInNativeLibrary(int var0);
```

To call this native method, the Java code would call it like any other Java method. However, in the backend, the JNI and NDK would instead execute the corresponding function in the native library. To do this, it must know the pairing between a Java-declared native method with a function in the native library.

There are 2 different ways to do this pairing, or linking:
* Dynamic Linking using JNI Native Method Name Resolving, or
* Static Linking using the `RegisterNatives` API call

## Dynamic Linking
In order to link, or pair, the Java declared native method and the function in the native library dynamically, the developer names the method and the function according to the specs such that the JNI system can dynamically do the linking.

According to the spec, the developer would name the function as follow for the system to be able to dynamically link the native method and function. A native method name is concatenated from the following components:
* the prefix Java_
* a mangled fully-qualified class name
* an underscore ("_") separator
* a mangled method name
* for overloaded native methods, two underscores ("__") followed by the mangled argument signature

In order to do dynamic linking for the Java-declared native method below and let’s say it’s in the class com.android.interesting.Stuff:
```java
public native String doThingsInNativeLibrary(int var0);
```

The function in the native library would need to be named:
```
Java_com_android_interesting_Stuff_doThingsInNativeLibrary
```

If there is not a function in the native library with that name, that means that the application must be doing static linking.

## Static Linking
If the developer doesn’t want to or can not name the native functions according to the spec (Ex. wants to strip debug symbols), then they must use static linking with the RegisterNatives ([doc](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/functions.html#wp5833)) API in order to do the pairing between the Java-declared native method and the function in the native library. The RegisterNatives function is called from the native code, not the Java code and is most often called in the JNI_OnLoad function since RegisterNatives must be executed prior to calling the Java-declared native method.

```c++
jint RegisterNatives(JNIEnv *env, jclass clazz, const JNINativeMethod *methods, jint nMethods);

typedef struct { 
    char *name; 
    char *signature; 
    void *fnPtr; 
} JNINativeMethod;
```

When reverse engineering, if the application is using the static linking method, we as analysts can find the JNINativeMethod struct that is being passed to RegisterNatives in order to determine which subroutine in the native library is executed when the Java-declared native method is called.

The JNINativeMethod struct requires a string of the Java-declared native method name and a string of the method’s signature, so we should be able to find these in our native library.

### Method Signature
The JNINativeMethod struct requires the method signature. A method signature states the types of the arguments that the method takes and the type of what it returns. [This link](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/types.html) documents JNI Type Signatures in the “Type Signatures” section.
* Z: boolean
* B: byte
* C: char
* S: short
* I: int
* J: long
* F: float
* D: double
* L fully-qualified-class ; :fully-qualified-class
* [ type: type[]
* ( arg-types ) ret-type: method type
* V: void

For the native method
```java
public native String doThingsInNativeLibrary(int var0);
```
The type signature is:
```
(I)Ljava/lang/String;
```

Here’s another example of a native method and its signature. For the following is the method declaration
```java
public native long f (int n, String s, int[] arr); 
```
It has the type signature:
```
(ILjava/lang/String;[I)J
```

# Dealing with native functions
## Search for native functions
Search for ` native `.

## Search for loading functions
```java
System.loadLibrary("calc")
// or
System.load("lib/armeabi/libcalc.so")
```

## Analyze corresponding .so file
Use ghidra

# Reversing Android Native Libraries Code - JNIEnv
JNIEnv is a struct of function pointers to [JNI Functions](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/functions.html). Every JNI function in Android native libraries, takes JNIEnv* as the first argument.

# Search For Strings (or functions names)
grep -r "String" *, this can search for binary libs like .so

# Retype Parameters in native functions
Retype parameters so that the function looks more clear.
[This Video](https://youtu.be/nzv9ODeijwI)
[This Link](https://www.ragingrock.com/AndroidAppRE/reversing_native_libs.html)

# Obfuscation
There are many times when the application you’re reversing will not be as straight forward as some of the examples we’ve discussed. The developer will implement one or more obfuscation techniques to hide the behavior and/or implementation of their app. This can be for both benign and malicious reasons.

The key about obfuscation to remember is that if you want to de-obfuscate it, you will be able to. The key decision is not whether or not you can, but whether or not it’s worth the resources to de-obfuscate.

The reason that you can always de-obfuscate something is because ultimately the CPU at some point has to see the unobfuscated code in order to run it.

## How to De-Obfuscate
How you choose to de-obfuscate the application will depend on the obfuscation method, but there are a couple of common techniques that usually work well. Here, we will only touch on the static de-obfuscation techniques since this workshop only covers static analysis/reversing. However, do remember that running the application and dynamically analyzing it can be another great way to get around obfuscation.

For obfuscation in the DEX bytecode (Java), one of the easiest ways to statically deobfuscate is to identify the de-obfuscation methods in the application and copy their decompilation into a Java file that you then run on the obfuscated file, strings, code, etc.

Another solution for both Java and Native Code is to transliterate the de-obfuscation algorithm into Python or any other scripting language that you’re most comfortable. I say “transliterate” because it’s important to remember that you don’t always need to *understand* the de-obfuscation algorithm, you just need a way to execute it. I cover this in more detail in the “Unpacking the Packed Unpacker” talk that is linked in the “More Examples” section.

## Indicators of Obfuscation
There are many different types of obfuscation and thus, just as many different types of indicators to alert you as the analyst that an application is likely obfuscated, but here are a few examples with proposed static analysis solutions for deobfuscating.
* No strings: Java and Android are highly dependent on strings so if you don’t see any or only scrambled strings, it’s highly likely the strings are obfuscated.
  * Suggested solution: Look for method calls that take strings as an argument and trace back where that argument is coming from. At some point the string argument will be going through a deobfuscation method before it’s passed to the API that takes the String argument.
* Scrambled strings: The Java and Android APIs require the plain text strings, not scrambled.
  * Suggested solution: The scrambled strings are all likely passed to the same methods prior to being passed to the APIs. These methods are likely the deobfuscation methods.
* Binary files in the assets/ directory and DexClassLoader calls in the app: Likely unpacking and loading additional code. (Could also be downloading from a remote location and then loading using DexClassLoader)
  * Suggestion Solution: Identify where the file is read and then follow the path. It is likely deobfuscated quickly after being read.
* Native libraries - Can’t identify the JNI functions (no funcs named Java_ and no calls to RegisterNatives): In order to execute any native methods, JNI has to be able to pair the function in the native library with the native method declaration in Java and thus one of the two must exist at some point.
  * Suggested Solution: Start at JNI_OnLoad method and look for a de-obfuscation routine that loads additional code.

[Additional obfuscation videos](https://www.ragingrock.com/AndroidAppRE/obfuscation.html)

