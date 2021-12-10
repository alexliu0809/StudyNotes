# Reference
[AndroidFundamentals](https://developer.android.com/codelabs/android-training-hello-world?index=..%2F..%2Fandroid-training#7)

[AndroidTraningCourses](https://developer.android.com/courses)

[IntroToAndroid](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/)

## What’s Android?
* An operating system
    * Based on Linux
* A software stack
    * The operating system
    * The application framework
* Support for multiple devices
    * Phones, Tablets, and Wearable

## Android SDK
* Compiler
    * Build and package apps
* Debugging tools
    * Through Android Studio
* Version: Android 1 - 10 (for end user)
* API Level: For developer
* System image --> virtual emulator

## Android Versions
* Android 9 (Pie)
* Android 8 (Oreo)
* Android 7 (Nougat)
* Android 6 (Marshmallow)
* Old versions

## Android Architecture
* Built on Linux Kernel (a version works for slow devices)
    * Linux Kernel + A set of drivers (tailored to hardware)
* On top: Android runtime and Libs
    * Runtime includes Core libs and ART (contemporary android runtime)
    * Libs include the compilers, and default libs like OpenGL/SSL/SQLite/FreeType
* On top: Application Frameworks
    * Module for controlling apps
* On top: Applications
    * Apps themselves
    * Default: Launcher/Browser/Contacts/Phone 


## Android and OpenJDK
* The Android SDK is built around open-source Java
    * All java 5 and 6
    * Most Java 7
    * Some Java 8 features
* Android Standard Java APIs
    * The Android SDK implements most standard Java packages
        * JAVA.LANG
        * JAVA.IO
        * JAVA.MATH
        * …
    * Android Custom APIs
        * Android.app
        * Android.widget
        * Android.hardware
        * …
* Primary Programming Languages
    * Java vs Kotlin


## Android Jetpack
* A collection of software components that are designed to speed up the development of Android applications. The Jetpack components are delivered in a set of libs that are prefixed with androidx



## Android Build Process 
* Java
    * Source code (.java) / Lib code (.class) --> DEX bytecode (.dev) --> machine code (depend on the hardware and processor)
* Kotlin
    * Source code (.kt) / Lib code (.class) --> Java bytecode --> DEV bytecode --> machine code (depend on the hardware and processor)




## Manage Virtual Device
Android virtual device (AVD)
* When testing on a virtual device, it is a good practice to start it up once, at the very beginning of your session. You should not close it until you are done testing your app, so that your app doesn't have to go through the device startup process again. To close the virtual device, click the X button at the top of the emulator, choose Quit from the menu, or press Control-Q in Windows or Command-Q in macOS.


## Manage on Physical Device
[Link](https://developer.android.com/codelabs/android-training-hello-world?index=..%2F..%2Fandroid-training#5)
* Connect device to computer using a usb
* Goto Logcat window (and see if there’s a device)
* Touch build number 7 times (to enter developer mode)
* Turn on stay awake & USB debugging


## Project Structure
* Android view:
    * Manifest
        * AndroidManifest.xml: This file describes all the components of your Android app and is read by the Android runtime system when your app is executed. All components for an app, such as each Activity, must be declared in this XML file.
    * Java: All your Java language files are organized here. Contains 3 sub folders
        * com.example.myfirstapp: This folder contains the Java source code files for your app.
        * com.example.myfirstapp (androidTest): This folder is where you would put your instrumented tests, which are tests that run on an Android device. It starts out with a skeleton test file.
        * com.example.myfirstapp (test): This folder is where you would put your unit tests. Unit tests don't need an Android device to run. It starts out with a skeleton unit test file.
    * Res: contains all the resources for your app, including images, layout files, strings, icons, and styling. Contains these sub folders:
        * drawable: All your app's images will be stored in this folder.
        * Layout: This folder contains the UI layout files for your activities. Currently, your app has one activity that has a layout file called activity_main.xml. It also contains content_main.xml, fragment_first.xml, and fragment_second.xml
        * Menu: This folder contains XML files describing any menus in your app.
        * Mipmap: This folder contains the launcher icons for your app.
        * Navigation: This folder contains the navigation graph, which tells Android Studio how to navigate between different parts of your application.
        * Values: This folder contains resources, such as strings and colors, used in your app.
    * Gradle
        * build.gradle(Project:xxx): This is where you'll find the configuration options that are common to all of the modules that make up your project. Every Android Studio project contains a single, top-level Gradle build file. By default, the top-level build file uses the buildscript block to define the Gradle repositories and dependencies that are common to all modules in the project. When your dependency is something other than a local library or file tree, Gradle looks for the files in whichever online repositories are specified in the repositories block of this file. By default, new Android Studio projects declare JCenter and Google (which includes the Google Maven repository) as the repository locations:
          ```gradle
          allprojects {
             repositories {
                google()
                jcenter()
             }
          }
          ```
        * build.gradle(Module:app): In addition to the project-level build.gradle file, each module has a build.gradle file of its own, which allows you to configure build settings for each specific module (the HelloWorld app has only one module). Configuring these build settings allows you to provide custom packaging options, such as additional build types and product flavors. You can also override settings in the `AndroidManifest.xml` file or the top-level build.gradle file. This file is most often the file to edit when changing app-level configurations, such as declaring dependencies in the dependencies section. You can declare a library dependency using one of several different dependency configurations. Each dependency configuration provides Gradle different instructions about how to use the library.

## Log in App:
Log statements in your app code display messages in the Logcat pane. For example:

```java
Log.d("MainActivity", "Hello World");

// for a class
private static final String LOG_TAG = MainActivity.class.getSimpleName();
Log.d(LOG_TAG, "Button clicked!");
```

The parts of the message are:
* `Log`: The Log class for sending log messages to the Logcat pane.
* `d`:  The Debug Log level setting to filter log message display in the Logcat pane. Other log levels are `e` for Error, `w` for Warn, and `i` for Info.
* `"MainActivity"`: The first argument is a tag which can be used to filter messages in the Logcat pane. This is commonly the name of the Activity from which the message originates. However, you can make this anything that is useful to you for debugging.

## Android Terminal Tool
* Add the tools to PATH
* Then you can use adb after the device is connected.


## View & View Hierarchy 
The user interface (UI) that appears on a screen of an Android device consists of a hierarchy of objects called views --- **Every element in is a view**. The `View` class represents the basic building block for all UI components, and the base class for classes that provide interactive UI components such as buttons, checkboxes, and text entry fields.
* Every layout must have a root view that contains all the other views. The root view is always a view group, which is a view that contains other views.
* A ConstraintLayout is one example of a view group of 2. Notice that the ConstraintLayout contains a TextView, called textview_first and a Button, called button_first.
* In the XML code, notice that the root element is &lt;androidx.constraintlayout.widget.ConstraintLayout>. The root element contains a &lt;TextView> element and a &lt;Button> element.


## Activity and Intent
An `Activity` represents a single screen in your app with which your user can perform a single, focused task such as taking a photo, sending an email, or viewing a map. An activity is usually presented to the user as a full-screen window.

An app usually consists of multiple screens that are loosely bound to each other. Each screen is an activity. Typically, one activity in an app is specified as the "main" activity (`MainActivity.java`), which is presented to the user when the app is launched. The main activity can then start other activities to perform different actions.

Each time a new activity starts, the previous activity is stopped, but the system preserves the activity in a stack (the "back stack"). When a new activity starts, that new activity is pushed onto the back stack and takes user focus. The back stack follows basic "last in, first out" stack logic. When the user is done with the current activity and presses the Back button, that activity is popped from the stack and destroyed, and the previous activity resumes.

Each new activity you add to your project has its own layout and Java files, separate from those of the main activity. They also have their own `activity` elements in the `AndroidManifest.xml` file. As with the main activity, new activity implementations that you create in Android Studio also extend from the `AppCompatActivity` class.

Each activity in your app is only loosely connected with other activities. However, you can define an `activity` as a parent of another activity in the `AndroidManifest.xml` file. This parent-child relationship enables Android to add navigation hints such as left-facing arrows in the title bar for each activity.

An activity is started or activated with an `intent`. An Intent is an asynchronous message that you can use in your activity to request an action from another activity, or from some other app component. An activity communicates with **other activities (in the same app and across different apps) with an intent**. 

An Intent can be explicit or implicit:
* An explicit intent is one in which you know the target of that intent. That is, you already know the fully qualified class name of that specific activity.
* An implicit intent is one in which you do not have the name of the target component, but you have a general action to perform.


## Declare intent in Manifest
[more](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-2-activities-and-intents/2-1-c-activities-and-intents/2-1-c-activities-and-intents.html)

Each Activity in your app must be declared in the AndroidManifest.xml file with the activity element, inside the application section. When you create a new project or add a new Activity to your project in Android Studio, the AndroidManifest.xml file is created or updated to include skeleton declarations for each Activity. Here's the declaration for MainActivity:

```xml
<activity android:name=".MainActivity" >
   <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
   </intent-filter>
</activity>
```
The `activity` element includes a number of attributes to define properties of the Activity such as its label, icon, or theme. The only required attribute is android:name, which specifies the class name for the Activity (such as MainActivity). See the `activity` element reference for more information on Activity declarations.

The `activity` element can also include declarations for Intent filters. The Intent filters specify the kind of Intent your Activity will accept.

<intent-filter>
   <action android:name="android.intent.action.MAIN" />
   <category android:name="android.intent.category.LAUNCHER" />
</intent-filter>

Intent filters must include at least one `action` element, and can also include a `category` and optional `data`. The MainActivity for your app needs an Intent filter that defines the "main" action and the "launcher" category so that the system can launch your app. 

The `action` element specifies that this is the "main" entry point to the app. The `category` element specifies that this Activity should be listed in the system's app launcher.

## Constraints
* Jagged line: constraints link one to another
* Wavy line: indicates a chain, where the constraints link two or more objects to each other
* Bias: The "bias" constraints allows you to tweak the position of a view to be more on one side than the other when both sides are constrained in opposite directions. For example, if both the top and bottom sides of a view are constrained to the top and bottom of the screen, you can use a vertical bias to place the view more towards the top than the bottom. (the vertical slide bar)
* Marge: distance from the border. **Using the bias attribute instead of margins or padding results in a more pleasing layout on different screen sizes and orientations.**


## Toast
A toast is a short message that appears briefly at the bottom of the screen.


## Finding a View By ID
### Given a view, find View by ID:
The id for a view helps you identify that view distinctly from other views. Using the findViewByID() method, your code can find the view using its id, R.id.view_id.

```java
// Level 1: view.findViewByID(view_id).setOnClickListener(listener)
// Level 2: view_id = R.id.random_button;
// Level 2: new View.OnClickListener(){}
// Level 3:{ @Override public void onClick(View view){do_something()} };
// Level 4: do_something()....

view.findViewById(R.id.random_button).setOnClickListener(new View.OnClickListener() {
   @Override
   public void onClick(View view) {
      do_something();
   }
});

public void do_something(){
        Toast myToast = Toast.makeText(getActivity(), "Hello toast!", Toast.LENGTH_SHORT);
        myToast.show();
}
```

The click listener can either:

* Implement a small amount of code directly.
* Call a method that defines the desired click behavior in the activity.

### Find view without a given view:
```java
a_text_view = (TextView) findViewById(R.id.id_text_view);
```

## Connect View with Actions
### Option1 (doesn't work for older versions)
* Create function for action in activity
```java
public void showToast(View view) {
        Toast toast = Toast.makeText(this, R.string.toast_message,
                Toast.LENGTH_SHORT);
        toast.show();
    }
```

* Connect function with view
```xml
Button
    android:onClick="countUp"/
```
### Option 2
```java
findViewById(R.id.random_button).setOnClickListener(new View.OnClickListener() {
   @Override
   public void onClick(View view) {
      do_something();
   }
});
```



## Pre-initialize Pointers to Views
Create a pointer to a view:

```java
TextView showCountTextView;

@Override
public View onCreateView(
       LayoutInflater inflater, ViewGroup container,
       Bundle savedInstanceState
) {
   // Inflate the layout for this fragment
   /*
        The LayoutInflater class is used to instantiate the contents of layout XML files into their corresponding View objects.
        In other words, it takes an XML file as input and builds the View objects from it.
   */

   View fragmentFirstLayout = inflater.inflate(R.layout.fragment_first, container, false);
   // Get the count text view
   showCountTextView = fragmentFirstLayout.findViewById(R.id.textview_first);

   return fragmentFirstLayout;
}
```



## Add an intent
* Create an intent: The Intent constructor takes two arguments for an explicit Intent: an application `Context` and the specific component that will receive that `Intent`. Here you should use `this` as the Context, and `SecondActivity.class` as the specific class
    ```java
    Intent intent = new Intent(this, SecondActivity.class);
    startActivity(intent);
    ```

## Passing data between activities
Your intent object can pass data to the target activity in two ways: in the data field, or in the intent extras. The intent data is a URI indicating the specific data to be acted on. If the information you want to pass to an activity through an intent is not a URI, or you have more than one piece of information you want to send, you can put that additional information into the extras instead.

The intent extras are key/value pairs in a `Bundle`. A `Bundle` is a collection of data, stored as key/value pairs. To pass information from one activity to another, you put keys and values into the intent extra Bundle from the sending activity, and then get them back out again in the receiving activity.

The `Intent` extras are key/value pairs in a `Bundle`. A `Bundle` is a collection of data, stored as key/value pairs. To pass information from one `Activity` to another, you put keys and values into the `Intent` extra `Bundle` from the sending Activity, and then get them back out again in the receiving `Activity`.

```java
intent.putExtra("key",val);
```

## Unpacking Passed Value
* Open SecondActivity to add code to the onCreate() method, Get the Intent that activated this Activity
```java
Intent intent = getIntent();
String message = intent.getStringExtra(key);
```

## Call back intent
### Old way (deprecated)
```java
public void openSomeActivityForResult() {
      Intent intent = new Intent(this, SomeActivity.class);
      startActivity(intent)
      // register call back
      startActivityForResult(intent, 123);
  }

  @Override
  protected void onActivityResult (int requestCode, int resultCode, Intent data) {
      if (resultCode == Activity.RESULT_OK && requestCode == 123) {
          doSomeOperations();
      }
  }
```
### New way
```java
// create a launcher
ActivityResultLauncher<Intent> passDataToSecondScreenWithCallbackLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(), // keep the intent as it is
            new ActivityResultCallback<ActivityResult>() {
                // register a callback function
                @Override
                public void onActivityResult(ActivityResult result) {
                    if (result.getResultCode() == Activity.RESULT_OK) {
                        handleCallbackResult(result);
                    }
                }
            });

// launch the acitivty
public void launchSecondActivity(View view) {
    Log.d(LOG_TAG, "Button clicked!");
    Intent intent = new Intent(this, SecondActivity.class);
    intent.putExtra(INTENT_KEY, mEditText.getText().toString());
    passDataToSecondScreenWithCallbackLauncher.launch(intent);
}
```

## Handle Implicit Intent
### One way to create implicit intent
```java
// Parse the URI and create the intent.
Uri webpage = Uri.parse(url);
Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

// Use the resolveActivity() method and the Android package manager to find an Activity that can handle your implicit Intent. 
// Make sure that the request resolved successfully.
if (intent.resolveActivity(getPackageManager()) != null) {
    startActivity(intent);
} else {
    Log.d("ImplicitIntents", "Can't handle this intent!");
}
```
### Another way (using a helper func)
```java
String txt = mShareTextEditText.getText().toString();
String mimeType = "text/plain";
// faster way to build an intent for action_send
ShareCompat.IntentBuilder
        .from(this)
        .setType(mimeType)
        .setChooserTitle(R.string.share_text_with)
        .setText(txt)
        .startChooser();
```

## Receive an intent
* action: "android.intent.action.VIEW". Any Intent with view actions.
* category: "android.intent.category.DEFAULT". Any implicit Intent. This category must be included for your Activity to receive any implicit Intent.
* category: "android.intent.category.BROWSABLE". Requests for browsable links from web pages, email, or other sources.
* data: android:scheme="http" android:host="developer.android.com". URIs that contain a scheme of http and a host name of developer.android.com.

Note for urls, you can't capture all urls (you can only capture specific ones).
```xml
<action android:name="android.intent.action.VIEW" />
<category android:name="android.intent.category.DEFAULT" />
<category android:name="android.intent.category.BROWSABLE" />
<data android:scheme="http" android:host="developer.android.com" />
```


## Create a layout variant for horizontal orientation
* Click the Orientation in Editor button 
* Choose Create Landscape Variation.
* Look for `activity_main.xml` (land)


## Support Libs
When developing apps that support multiple API versions, you may want a standard way to provide newer features on earlier versions of Android or gracefully fall back to equivalent functionality. Rather than building code to handle earlier versions of the platform, you can leverage these libraries to provide that compatibility layer. 

With the release of Android 9.0 (API level 28) there is a new version of the support library called AndroidX which is part of Jetpack. The AndroidX library contains the existing support library and also includes the latest Jetpack components.

For each module in which you want to use a Support Library, add the library in the dependencies block of the module's build.gradle file. For example, to add the v4 core-utils library, add the following:
```xml
dependencies {
    ...
    implementation "com.android.support:support-core-utils:28.0.0"
}
```

### Using Support Library APIs
When using classes from the Support Library, be certain you import the class from the appropriate package. For example, when applying the ActionBar class:
* android.support.v7.app.ActionBar when using the Support Library.
* android.app.ActionBar when developing only for API level 11 or higher.

## Change the launcher icon
[Link](https://developer.android.com/codelabs/android-training-available-resources?index=..%2F..%2Fandroid-training#2)
Each app you create with Android Studio starts with a default launcher icon that represents the app. Launcher icons are sometimes called app icons or product icons.

After an app is installed on an Android-powered device, the app's launcher icon appears on the device's home screen and elsewhere on the device. For example, launcher icons appear in the device's Search Apps window, as shown in the screenshot below. The HelloToast icon shown below is the default launcher icon used for all app projects that you create in Android Studio.

## Status Bar
* Status bar, which the Android system provides and controls. 
* Not visible in the template code, but you can access the status-bar from your activity. For example, you can add code in MainActivity.java to [hide the status bar](http://developer.android.com/training/system-ui/status.html), if necessary.

## Add Activity
* In the Project > Android pane, right-click the java folder.
* Select New > Activity > Gallery.
* Add an activity to the app by selecting one of the Activity templates. For example, select Navigation Drawer Activity to add an Activity that has a navigation drawer.

## Pass Information Between Fragments (two screens)
* Open nav_graph.xml
* Add Action (with a name at the Origin) and Arg (at the destination)
    * https://developer.android.com/guide/navigation/navigation-pass-data


## Show a Dialog
The builder design pattern makes it easy to create an object from a class that has a lot of required and optional attributes and would therefore require a lot of parameters to build. Without this pattern, you would have to create constructors for combinations of required and optional attributes; with this pattern, the code is easier to read and maintain.

The builder class is usually a static member class of the class it builds. Use AlertDialog.Builder to build a standard alert dialog, with setTitle() to set its title, setMessage() to set its message, and setPositiveButton() and setNegativeButton() to set its buttons.
```java
public void onClickShowAlert(View view) {
    AlertDialog.Builder myAlertBuilder = new
                               AlertDialog.Builder(MainActivity.this);
    // Set the dialog title and message.
    // Set the dialog title and message.
    myAlertBuilder.setTitle("Alert");
    myAlertBuilder.setMessage("Click OK to continue, or Cancel to stop:");
    // Add the dialog buttons.
    myAlertBuilder.setPositiveButton("OK", new 
                                    DialogInterface.OnClickListener() {
        public void onClick(DialogInterface dialog, int which) {
            // User clicked OK button.
            Toast.makeText(getApplicationContext(), "Pressed OK",
                            Toast.LENGTH_SHORT).show();
        }
    });
    myAlertBuilder.setNegativeButton("Cancel", new 
                                    DialogInterface.OnClickListener() {
        public void onClick(DialogInterface dialog, int which) {
            // User cancelled the dialog.
            Toast.makeText(getApplicationContext(), "Pressed Cancel",
                            Toast.LENGTH_SHORT).show();
        }
    });
    // Create and show the AlertDialog.
    myAlertBuilder.show();
}
```

## Fragment
A Fragment is a piece of an application's user interface or behavior that can be placed in an Activity.  In its core, it represents a particular operation or interface that is running within a larger Activity. A Fragment is closely tied to the Activity it is in, and can not be used apart from one. Though Fragment defines its own lifecycle, that lifecycle is dependent on its activity: if the activity is stopped, no fragments inside of it can be started; when the activity is destroyed, all fragments will be destroyed.


## ID of a widget
* android:id=”@+id/your_name”

## Use External API in an Async Way
### Option 1: Java Concurrent
The problem with this approach: background thread can't update the UI if a configuration change occurs while the background task is running.
#### Use Java Concurrent to Run an Async Program
* Define a class that performs some task
```java
// The type in callable is the return type
public class FetchBook implements Runnable {
    private Activity activity;
    private String fetch_url;
    private WeakReference<TextView> mTitleText;
    private WeakReference<TextView> mAuthorText;

    FetchBook(Activity current_activity, String fetch_url, TextView mTitleText, TextView mAuthorText) {
        this.fetch_url = fetch_url;
        this.mTitleText = new WeakReference<>(mTitleText); // Weak reference prevents memory leak
        this.mAuthorText = new WeakReference<>(mAuthorText);
        this.activity = current_activity;
    }

    @Override
    public void run() {
        String bookJSONString = NetworkUtils.getBookInfo(this.fetch_url);
        try {
            //...
            JSONObject jsonObject = new JSONObject(bookJSONString);
            JSONArray itemsArray = jsonObject.getJSONArray("items");
            int i = 0;
            String title = null;
            String authors = null;
            while (i < itemsArray.length() &&
                    (authors == null && title == null)) {
                // Get the current item information.
                JSONObject book = itemsArray.getJSONObject(i);
                JSONObject volumeInfo = book.getJSONObject("volumeInfo");

                // Try to get the author and title from the current item,
                // catch if either field is empty and move on.
                try {
                    title = volumeInfo.getString("title");
                    authors = volumeInfo.getString("authors");
                } catch (Exception e) {
                    e.printStackTrace();
                }

                // Move to the next item.
                i++;
            }
            final String final_title = title;
            final String final_author = authors;

            // this has to be on UI thread, otherwise an exception will be raised
            activity.runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    if (final_title != null && final_author != null) {
                        mTitleText.get().setText(final_title);
                        mAuthorText.get().setText(final_author);
                    } else {
                        mTitleText.get().setText(R.string.no_results);
                        mAuthorText.get().setText("");
                    }
                }
            });
        } catch (JSONException e) {
            // If onPostExecute does not receive a proper JSON string,
            // update the UI to show failed results.
            activity.runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    mTitleText.get().setText(R.string.no_results);
                    mAuthorText.get().setText("");
                    e.printStackTrace();
                }
            });
        }
    }

}
```
* Run this task in background
```java
Runnable runnable = new FetchBook(this, queryString, mTitleText, mAuthorText); // or an anonymous class, or lambda...

Thread thread = new Thread(runnable);
thread.start();
```
#### Option 2: AsyncTaskLoader
[asynctaskloader](https://developer.android.com/codelabs/android-training-asynctask-asynctaskloader)

### Add Permission
Add the following code just before the <application> element:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission 
       android:name="android.permission.ACCESS_NETWORK_STATE" />
```


## Override Code
Code --> Override Method

## Hiding Keyboard
```java
// Hide the keyboards
InputMethodManager inputManager = (InputMethodManager)
        getSystemService(Context.INPUT_METHOD_SERVICE);

if (inputManager != null ) {
    inputManager.hideSoftInputFromWindow(view.getWindowToken(),
            InputMethodManager.HIDE_NOT_ALWAYS);
}
``` 


## Broadcasts
Broadcasts are messages that the Android system and Android apps send when events occur that might affect the functionality of other apps or app components. For example, the Android system sends a system broadcast when the device boots up, or when headphones are connected or disconnected. If the wired headset is unplugged, you might like your media app to pause the music.

Your Android app can also broadcast events, for example when new data is downloaded that might interest some other app. Events that your app delivers are called custom broadcasts.

In general, you can use broadcasts as a messaging system across apps and outside of the normal user flow.

A broadcast is received by any app or app component that has a broadcast receiver registered for that action. BroadcastReceiver is the base class for code that receives broadcast intents. 

The broadcast message itself is wrapped in an `Intent` object whose action string identifies the event that occurred (for example `android.intent.action.AIRPLANE_MODE`). The intent may also include additional information bundled into its extra field. For example, the airplane mode intent includes a boolean extra that indicates whether or not Airplane Mode is on.

### Create Broadcast Receiver
* To create a new broadcast receiver, select the package name in the Android Project View and navigate to File > New > Other > Broadcast Receiver.
* Name the class CustomReceiver. Make sure that Java is selected as the source language, and that Exported and Enabled are selected. `Exported` allows your broadcast receiver to receive broadcasts from outside your app. `Enabled` allows the system to instantiate the receiver.

### Register your receiver for system broadcasts
* A system broadcast is a message that the Android system sends when a system event occurs. Each system broadcast is wrapped in an Intent object:
 * The intent's action field contains event details such as android.intent.action.HEADSET_PLUG, which is sent when a wired headset is connected or disconnected.
 * The intent can contain other data about the event in its extra field, for example a boolean extra indicating whether a headset is connected or disconnected.

Apps can register to receive specific broadcasts. When the system sends a broadcast, it routes the broadcast to apps that have registered to receive that particular type of broadcast.

A BroadcastReceiver is either a static receiver or a dynamic receiver, depending on how you register it:
* To register a receiver statically, use the <receiver> element in your AndroidManifest.xml file. Static receivers are also called manifest-declared receivers.
* To register a receiver dynamically, use the app context or activity context. The receiver receives broadcasts as long as the registering context is valid, meaning as long as the corresponding app or activity is running. Dynamic receivers are also called context-registered receivers.

Starting from Android 8.0 (API level 26 and higher), you can't use static receivers to receive most Android system broadcasts, with some exceptions.

### Manifest-declared receivers
* Specify the `receiver` element in your app's manifest.
    ```xml
    <receiver android:name=".MyBroadcastReceiver"  android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.BOOT_COMPLETED"/>
            <action android:name="android.intent.action.INPUT_METHOD_CHANGED" />
        </intent-filter>
    </receiver>
    ```
    The intent filters specify the broadcast actions your receiver subscribes to.
* Subclass BroadcastReceiver and implement onReceive(Context, Intent). The broadcast receiver in the following example logs and displays the contents of the broadcast:
    ```java
    public class MyBroadcastReceiver extends BroadcastReceiver {
        private static final String TAG = "MyBroadcastReceiver";
        @Override
        public void onReceive(Context context, Intent intent) {
            StringBuilder sb = new StringBuilder();
            sb.append("Action: " + intent.getAction() + "\n");
            sb.append("URI: " + intent.toUri(Intent.URI_INTENT_SCHEME).toString() + "\n");
            String log = sb.toString();
            Log.d(TAG, log);
            Toast.makeText(context, log, Toast.LENGTH_LONG).show();
        }
    }
    ```


### Dynamically Register and Unregister
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    // Dynamically register intent-filter
    IntentFilter filter = new IntentFilter();

    filter.addAction(Intent.ACTION_POWER_DISCONNECTED);
    filter.addAction(Intent.ACTION_POWER_CONNECTED);

    // Register the receiver using the activity context.
    BroadcastReceiver mReceiver = new MyBroadcastReceiver();
    this.registerReceiver(mReceiver, filter);

}

@Override
protected void onDestroy() {
    //Unregister the receiver
    this.unregisterReceiver(mReceiver);
    super.onDestroy();
}
```

### Receiving Broadcast Message
```java
public class CustomReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String intentAction = intent.getAction();
        if (intentAction != null) {
            String toastMessage = "unknown intent action";
            switch (intentAction) {
                case Intent.ACTION_POWER_CONNECTED:
                    toastMessage = "Power connected!";
                    break;
                case Intent.ACTION_POWER_DISCONNECTED:
                    toastMessage = "Power disconnected!";
                    break;
            }
            //Display the toast.
            Toast.makeText(context, toastMessage, Toast.LENGTH_SHORT).show();
        }


    }
}
```

### Send and receive a custom broadcast
In addition to responding to system broadcasts, your app can send and receive custom broadcasts. Use a custom broadcast when you want your app to take an action without launching an activity, for example when you want to let other apps know that data has been downloaded to the device.

Android provides three ways for your app to send custom broadcasts:

* Normal broadcasts are asynchronous. Receivers of normal broadcasts run in an undefined order, often at the same time. To send a normal broadcast, create a broadcast intent and pass it to sendBroadcast(Intent).
* Local broadcasts are sent to receivers that are in the same app as the sender. To send a local broadcast, create a broadcast intent and pass it to LocalBroadcastManager.sendBroadcast.
* Ordered broadcasts are delivered to one receiver at a time. As each receiver executes, it can propagate a result to the next receiver, or it can cancel the broadcast so that the broadcast is not passed to other receivers. To send an ordered broadcast, create a broadcast intent and pass it to sendOrderedBroadcast(Intent, String).

The broadcast message is wrapped in an Intent object. The Intent action string must provide the app's Java package name syntax and uniquely identify the broadcast event.

For a custom broadcast, you define your own Intent action (a unique string). You can create Intent objects with custom actions and broadcast them yourself from your app using one of the methods above. The broadcasts are received by apps that have a BroadcastReceiver registered for that action.

#### Send Custom Intent
```java
    private static final String ACTION_CUSTOM_BROADCAST =
            BuildConfig.APPLICATION_ID + ".ACTION_CUSTOM_BROADCAST";

    public void sendCustomBroadcast(View view) {
        Intent customBroadcastIntent = new Intent(ACTION_CUSTOM_BROADCAST);
        LocalBroadcastManager.getInstance(this).sendBroadcast(customBroadcastIntent);
    }
```

#### Receive Custom Intent
Save as above for receiving custom intent


## Service
A Service is an application component that can perform long-running operations in the background. It does not provide a user interface. Once started, a service might continue running for some time, even after the user switches to another application. Additionally, a component can bind to a service to interact with it and even perform interprocess communication (IPC).

### Types of Services
* Foreground: A foreground service performs some operation that is noticeable to the user. For example, an audio app would use a foreground service to play an audio track. Foreground services must display a Notification. Foreground services continue running even when the user isn't interacting with the app. 
    The WorkManager API offers a flexible way of scheduling tasks, and is able to run these jobs as foreground services if needed. In many cases, using WorkManager is preferable to using foreground services directly.
* Background: A background service performs an operation that isn't directly noticed by the user. For example, if an app used a service to compact its storage, that would usually be a background service.
    If your app targets API level 26 or higher, the system imposes restrictions on running background services when the app itself isn't in the foreground. In most situations, for example, you shouldn't access location information from the background. Instead, schedule tasks using WorkManager.
* Bound: A service is bound when an application component binds to it by calling bindService(). A bound service offers a client-server interface that allows components to interact with the service, send requests, receive results, and even do so across processes with interprocess communication (IPC). A bound service runs only as long as another application component is bound to it. Multiple components can bind to the service at once, but when all of them unbind, the service is destroyed.

### Declaring a service in the manifest
You must declare all services in your application's manifest file, just as you do for activities and other components.
```xml
<manifest ... >
  ...
  <application ... >
      <service android:name=".ExampleService" />
      ...
  </application>
</manifest>
```
There are other attributes that you can include in the `service` element to define properties such as the permissions that are required to start the service and the process in which the service should run. The android:name attribute is the only required attribute—it specifies the class name of the service. 

You can ensure that your service is available to only your app by including the `android:exported` attribute and setting it to `false`. This effectively stops other apps from starting your service, even when using an explicit intent.

### Create a service
```java
public class HelloService extends Service {
  private Looper serviceLooper;
  private ServiceHandler serviceHandler;

  // Handler that receives messages from the thread
  private final class ServiceHandler extends Handler {
      public ServiceHandler(Looper looper) {
          super(looper);
      }
      @Override
      public void handleMessage(Message msg) {
          // Normally we would do some work here, like download a file.
          // For our sample, we just sleep for 5 seconds.
          try {
              Thread.sleep(5000);
          } catch (InterruptedException e) {
              // Restore interrupt status.
              Thread.currentThread().interrupt();
          }
          // Stop the service using the startId, so that we don't stop
          // the service in the middle of handling another job
          stopSelf(msg.arg1);
      }
  }

  @Override
  public void onCreate() {
    // Start up the thread running the service. Note that we create a
    // separate thread because the service normally runs in the process's
    // main thread, which we don't want to block. We also make it
    // background priority so CPU-intensive work doesn't disrupt our UI.
    HandlerThread thread = new HandlerThread("ServiceStartArguments",
            Process.THREAD_PRIORITY_BACKGROUND);
    thread.start();

    // Get the HandlerThread's Looper and use it for our Handler
    serviceLooper = thread.getLooper();
    serviceHandler = new ServiceHandler(serviceLooper);
  }

  @Override
  public int onStartCommand(Intent intent, int flags, int startId) {
      Toast.makeText(this, "service starting", Toast.LENGTH_SHORT).show();

      // For each start request, send a message to start a job and deliver the
      // start ID so we know which request we're stopping when we finish the job
      Message msg = serviceHandler.obtainMessage();
      msg.arg1 = startId;
      serviceHandler.sendMessage(msg);

      // If we get killed, after returning from here, restart
      return START_STICKY;
  }

  @Override
  public IBinder onBind(Intent intent) {
      // We don't provide binding, so return null
      return null;
  }

  @Override
  public void onDestroy() {
    Toast.makeText(this, "service done", Toast.LENGTH_SHORT).show();
  }
}
```

### Starting a service
```java
Intent intent = new Intent(this, HelloService.class);
startService(intent);

// service of a different app
Intent i = new Intent();
i.setComponent(new ComponentName("com.xxx.yyy", "com.xxx.yyy.SyncService"));
ComponentName c = ctx.startService(i);
```

### Differentiate Intent 
If you want to use a service to perform different actions, then declaring an intent filter will help your service match against different actions you want to perform. **Note that if an intent-filter is specified, a service is automatically exported.**
```xml
<service
    android:name="MyService" >
    <intent-filter>
        <action android:name="com.x.y.DOWNLOAD_DATA" />
        <action android:name="com.x.y.UPLOAD_DATA" />
    </intent-filter>
</service>
```
Then in your `IntentService` you could filter for these actions like this:
```java
public class MyService extends IntentService {

    public MyService() {
        super("MyService");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if(intent.getAction().equals("com.x.y.DOWNLOAD_DATA"){
            //download data here
        }else if(intent.getAction().equals("com.x.y.UPLOAD_DATA"){
            // upload data here
        }
    }
}

```


## Notification
Sometimes you want your app to show information to users even when the app isn't running in the foreground. For example, you might want to let users know that new content is available, or that their favorite sports team just scored a goal in a game. The Android notification framework provides a way for your app to notify users even when the app is not in the foreground.

A notification is a message that your app displays to the user outside of your app's normal UI. Notifications appear as icons in the device's notification area, which is in the status bar. To see the details of a notification, the user opens the notification drawer, for example by swiping down on the status bar. The notification area and the notification drawer are system-controlled areas that the user can view at any time.

On devices running Android 8.0 and higher, when your app has a new notification to show to the user, your app icon automatically shows a badge. (Badges are also called notification dots).



### Create a notification channel
In the Settings app on an Android-powered device, users can adjust the notifications they receive. Starting with Android 8.0 (API level 26), your code can assign each of your app's notifications to a user-customizable notification channel:
* Each notification channel represents a type of notification.
* In your code, you can group several notifications in each notification channel.
* For each notification channel, your app sets behavior for the channel, and the behavior is applied to all the notifications in the channel. For example, your app might set the notifications in a channel to play a sound, blink a light, or vibrate.
* Whatever behavior your app sets for a notification channel, the user can change that behavior, and the user can turn off your app's notifications altogether.

On Android-powered devices running Android 8.0 (API level 26) or higher, notification channels that you create in your app appear as Categories under App notifications in the device Settings app.

For example, in the screenshot below of a device running Android 8.0, the Notify Me! app has one notification channel, Mascot Notification.

![Notification](https://developer.android.com/codelabs/android-training-notifications/img/b4ad33b85806f6ae.png)

When your app targets Android 8.0 (API level 26), to display notifications to your users you must implement at least one notification channel. To display notifications on lower-end devices, you're not required to implement notification channels. However, it's good practice to always do the following:
* Target the latest available SDK.
* Check the device's SDK version in your code. If the SDK version is 26 or higher, build notification channels.

Creates a notification channel for device with version >= 26
```java
private static final String PRIMARY_CHANNEL_ID = "primary_notification_channel";
private NotificationManager mNotifyManager;

public void createNotificationChannel() {
    mNotifyManager = (NotificationManager)
            getSystemService(NOTIFICATION_SERVICE);
    if (android.os.Build.VERSION.SDK_INT >=
            android.os.Build.VERSION_CODES.O) {
        // Create a NotificationChannel
        NotificationChannel notificationChannel = new NotificationChannel(PRIMARY_CHANNEL_ID,
                "Mascot Notification", NotificationManager
                .IMPORTANCE_HIGH);
        notificationChannel.enableLights(true);
        notificationChannel.setLightColor(Color.RED);
        notificationChannel.enableVibration(true);
        notificationChannel.setDescription("Notification from Mascot");
        mNotifyManager.createNotificationChannel(notificationChannel);
    }
}

@Override
protected void onCreate(Bundle savedInstanceState) {
    createNotificationChannel();
}
```

### Create Notification
Notifications are created using the `NotificationCompat.Builder` class, which allows you to set the content and behavior of the notification. A notification can contain the following elements:
* Icon (required), which you set in your code using the setSmallIcon() method.
* Title (optional), which you set using setContentTitle().
* Detail text (optional), which you set using setContentText().

To create the required notification icon:
* In Android Studio, go to File > New > Image Asset.
* From the Icon Type drop-down list, select Notification Icons.
* Click the icon next to the Clip Art item to select a Material Design icon for your notification. For this app, use the Android icon.
* Rename the resource ic_android and click Next and Finish. This creates drawable files with different resolutions for different API levels.



### Add a content intent and dismiss the notification
Content intents for notifications are similar to the intents you've used throughout this course. Content intents can be explicit intents to launch an activity, implicit intents to perform an action, or broadcast intents to notify the system of a system event or custom event.

The major difference with an Intent that's used for a notification is that the Intent must be wrapped in a PendingIntent. The PendingIntent allows the Android notification system to perform the assigned action on behalf of your code.

### Add priority and defaults to your notification for backward compatibility
This task is required for devices running Android 7.1 or lower, which is most Android-powered devices. For devices running Android 8.0 and higher, you use notification channels to add priority and defaults to notifications, but it's a best practice to provide backward compatibility and support for lower-end devices.

When the user taps the Notify Me! button in your app, the notification is issued, but the only visual that the user sees is the icon in the notification bar. To catch the user's attention, set notification default options.

Priority is an integer value from `PRIORITY_MIN` (-2) to `PRIORITY_MAX` (2). Notifications with a higher priority are sorted above lower priority ones in the notification drawer. `HIGH` or `MAX` priority notifications are delivered as "heads up" notifications, which drop down on top of the user's active screen. It's not a good practice to set all your notifications to `MAX` priority, so use `MAX` sparingly.

```java
private Button button_notify;
private static final String PRIMARY_CHANNEL_ID = "primary_notification_channel";
private NotificationManager mNotifyManager;
private static final int NOTIFICATION_ID = 0;

public void sendNotification() {
    // Use Builder to Create Notification
    NotificationCompat.Builder notifyBuilder = getNotificationBuilder();
    // Notify with manager
    mNotifyManager.notify(NOTIFICATION_ID, notifyBuilder.build());
}

private NotificationCompat.Builder getNotificationBuilder(){
    // By using a PendingIntent to communicate with another app, you are telling that app to execute some predefined code at some point in the future. It's like the other app can perform an action on behalf of your app.
    // In this case, you adding tap behavior (taking users to main app) --> indicated by the second parameter in the intent, which specifies the specific component to start
    Intent notificationIntent = new Intent(this, MainActivity.class);
    PendingIntent notificationPendingIntent = PendingIntent.getActivity(this,
            NOTIFICATION_ID, notificationIntent, PendingIntent.FLAG_UPDATE_CURRENT);

    NotificationCompat.Builder notifyBuilder = new NotificationCompat.Builder(this, PRIMARY_CHANNEL_ID)
            .setContentTitle("You've been notified!")
            .setContentText("This is your notification text.")
            .setSmallIcon(R.drawable.ic_android)
            .setContentIntent(notificationPendingIntent)
            // Set Notification Prioirty
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            // Set Notification Behavior (e.g., sound)
            .setDefaults(NotificationCompat.DEFAULT_ALL)
            // Setting auto-cancel to true closes the notification when user taps on it.
            .setAutoCancel(true);
    return notifyBuilder;
}
```


### Cancel or update notification
After your app issues a notification, it's useful for your app to be able to update or cancel the notification if the information changes or becomes irrelevant.
```java
public void cancelNotification() {
  mNotifyManager.cancel(NOTIFICATION_ID);
}

// you have to pull it down to see the image
public void updateNotification() {
  Bitmap androidImage = BitmapFactory
          .decodeResource(getResources(), R.drawable.mascot_1);
  NotificationCompat.Builder notifyBuilder = getNotificationBuilder();
  notifyBuilder.setStyle(new NotificationCompat.BigPictureStyle()
          .bigPicture(androidImage)
          .setBigContentTitle("Notification Updated!"));
  mNotifyManager.notify(NOTIFICATION_ID, notifyBuilder.build());
}
```

### Add a notification action button
[Link](https://developer.android.com/codelabs/android-training-notifications?index=..%2F..%2Fandroid-training#4)



## Alarm Manager
Now that your app can send a notification, it's time to implement the main component of your app: the AlarmManager. This class will periodically deliver the reminder to stand up. AlarmManager has many kinds of alarms built into it, both one-time and periodic, exact and inexact.

AlarmManager, like notifications, uses a PendingIntent that it delivers with the specified options. Because of this, AlarmManager can deliver the Intent even when the app is no longer running.

A broadcast receiver receives the broadcast intent and delivers the notification.

Alarms do not fire when the device is in Doze mode (idle). Instead, alarms are deferred until the device exits Doze. To guarantee that alarms execute, you can use setAndAllowWhileIdle() or setExactAndAllowWhileIdle(). You can also use the new WorkManager API, which is built to perform background work either once or periodically. For details, see Schedule tasks with WorkManager.

The AlarmManager can trigger one-time or recurring events that occur even when your app is not running. For real-time clock (RTC) alarms, schedule events using System.currentTimeMillis(). For elapsed-time (ELAPSED_REALTIME) alarms, schedule events using elapsedRealtime(). Deliver a PendingIntent when events occur.
```java
// Set up the alarm:
Intent notifyIntent = new Intent(this, AlarmReceiver.class);
PendingIntent notifyPendingIntent = PendingIntent.getBroadcast
        (this, NOTIFICATION_ID, notifyIntent, PendingIntent.FLAG_UPDATE_CURRENT);
AlarmManager alarmManager = (AlarmManager) getSystemService(ALARM_SERVICE);

alarmManager.setInexactRepeating
        (AlarmManager.ELAPSED_REALTIME_WAKEUP,
                triggerTime, repeatInterval, notifyPendingIntent);

// Handle Alarm BroadCast
private void deliverNotification(Context context) {
Intent contentIntent = new Intent(context, MainActivity.class);
PendingIntent contentPendingIntent = PendingIntent.getActivity
        (context, NOTIFICATION_ID, contentIntent, PendingIntent.FLAG_UPDATE_CURRENT);
NotificationCompat.Builder builder = new NotificationCompat.Builder(context, PRIMARY_CHANNEL_ID)
        .setSmallIcon(R.drawable.ic_stand_up)
        .setContentTitle("Stand Up Alert")
        .setContentText("You should stand up and walk around now!")
        .setContentIntent(contentPendingIntent)
        .setPriority(NotificationCompat.PRIORITY_HIGH)
        .setAutoCancel(true)
        .setDefaults(NotificationCompat.DEFAULT_ALL);
mNotificationManager.notify(NOTIFICATION_ID, builder.build());
}

```
In manifest:
```xml
<receiver
            android:name=".AlarmReceiver"
            android:enabled="true"
            android:exported="true"></receiver>
```


## Job Scheduler
You've seen that you can use the AlarmManager class to trigger events based on the real-time clock, or based on elapsed time since boot. Most tasks, however, do not require an exact time, but should be scheduled based on a combination of system and user requirements. For example, to preserve the user's data and system resources, a news app could wait until the device is charging and connected to Wi-Fi to update the news.

The JobScheduler class allows you to set the conditions, or parameters, for when to run your task. Given these conditions, JobScheduler calculates the best time to schedule the execution of the job. For example, job parameters can include `the persistence of the job across reboots`, whether the device is plugged in, or whether the device is idle.

The task to be run is implemented as a JobService subclass and executed according to the specified parameters.

JobScheduler is only available on devices running API 21 and higher, and is currently not available in the support library. For backward compatibility, use `WorkManager`. The WorkManager API lets you schedule background tasks that need guaranteed completion, whether or not the app process is around. For devices running API 14 and higher, including devices without Google Play services, WorkManager provides capabilities that are like those provided by JobScheduler.

In this practical, you create an app that schedules a notification. The notification is posted when the parameters set by the user are fulfilled and the system requirements are met.


### Implement a JobService
To begin with, create a service that will run at a time determined by the conditions. The system automatically executes the JobService. The only parts you need to implement are the onStartJob() callback and the onStopJob() callback.

About the onStartJob() callback:
* Called when the system determines that your task should be run. In this method, you implement the job to be done.
* Returns a boolean indicating whether the job needs to continue on a separate thread. If true, the work is offloaded to a different thread, and your app must call jobFinished() explicitly in that thread to indicate that the job is complete. If false, the system knows that the job is completed by the end of onStartJob(), and the system calls jobFinished() on your behalf.

Implementation:

* Register Bind Service
```xml
<service
   android:name=".NotificationJobService"
   android:permission="android.permission.BIND_JOB_SERVICE"/>
```

* Create Job Service (Logic for Job)
```java
public class NotificationJobService extends JobService {

    NotificationManager mNotifyManager;

    // Notification channel ID.
    private static final String PRIMARY_CHANNEL_ID =
            "primary_notification_channel";

    @Override
    public boolean onStartJob(JobParameters params) {
        //Create the notification channel
        createNotificationChannel();

        //Set up the notification content intent to launch the app when clicked
        PendingIntent contentPendingIntent = PendingIntent.getActivity
                (this, 0, new Intent(this, MainActivity.class), PendingIntent.FLAG_UPDATE_CURRENT);

        NotificationCompat.Builder builder = new NotificationCompat.Builder
                (this, PRIMARY_CHANNEL_ID)
                .setContentTitle("Job Service")
                .setContentText("Your Job ran to completion!")
                .setContentIntent(contentPendingIntent)
                .setSmallIcon(R.drawable.ic_job_running)
                .setPriority(NotificationCompat.PRIORITY_HIGH)
                .setDefaults(NotificationCompat.DEFAULT_ALL)
                .setAutoCancel(true);

        mNotifyManager.notify(0, builder.build());
        return false;
    }

    @Override
    public boolean onStopJob(JobParameters params) {
        return true;
    }

    /**
     * Creates a Notification channel, for OREO and higher.
     */
    public void createNotificationChannel() {

        // Define notification manager object.
        mNotifyManager =
                (NotificationManager) getSystemService(NOTIFICATION_SERVICE);

        // Notification channels are only available in OREO and higher.
        // So, add a check on SDK version.
        if (android.os.Build.VERSION.SDK_INT >=
                android.os.Build.VERSION_CODES.O) {

            // Create the NotificationChannel with all the parameters.
            NotificationChannel notificationChannel = new NotificationChannel
                    (PRIMARY_CHANNEL_ID,
                            "Job Service notification",
                            NotificationManager.IMPORTANCE_HIGH);

            notificationChannel.enableLights(true);
            notificationChannel.setLightColor(Color.RED);
            notificationChannel.enableVibration(true);
            notificationChannel.setDescription
                    ("Notifications from Job Service");

            mNotifyManager.createNotificationChannel(notificationChannel);
        }
    }
}
```


### Schedule a job with condition
```java
public class MainActivity extends AppCompatActivity {

    private static final int JOB_ID = 0;
    private JobScheduler mScheduler;

    // Switches for setting job options.
    private Switch mDeviceIdleSwitch;
    private Switch mDeviceChargingSwitch;

    // Override deadline seekbar.
    private SeekBar mSeekBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mDeviceIdleSwitch = findViewById(R.id.idleSwitch);
        mDeviceChargingSwitch = findViewById(R.id.chargingSwitch);
        mSeekBar = findViewById(R.id.seekBar);

        final TextView seekBarProgress = findViewById(R.id.seekBarProgress);

        mScheduler = (JobScheduler) getSystemService(JOB_SCHEDULER_SERVICE);

        // Updates the TextView with the value from the seekbar.
        mSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                if (i > 0) {
                    seekBarProgress.setText(getString(R.string.seconds, i));
                } else {
                    seekBarProgress.setText(R.string.not_set);
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        });

    }

    /**
     * onClick method that schedules the jobs based on the parameters set.
     */
    public void scheduleJob(View view) {
        RadioGroup networkOptions = findViewById(R.id.networkOptions);

        int selectedNetworkID = networkOptions.getCheckedRadioButtonId();

        int selectedNetworkOption = JobInfo.NETWORK_TYPE_NONE;

        int seekBarInteger = mSeekBar.getProgress();
        boolean seekBarSet = seekBarInteger > 0;


        switch (selectedNetworkID) {
            case R.id.noNetwork:
                selectedNetworkOption = JobInfo.NETWORK_TYPE_NONE;
                break;
            case R.id.anyNetwork:
                selectedNetworkOption = JobInfo.NETWORK_TYPE_ANY;
                break;
            case R.id.wifiNetwork:
                selectedNetworkOption = JobInfo.NETWORK_TYPE_UNMETERED;
                break;
        }

        ComponentName serviceName = new ComponentName(getPackageName(),
                NotificationJobService.class.getName());
        JobInfo.Builder builder = new JobInfo.Builder(JOB_ID, serviceName)
                .setRequiredNetworkType(selectedNetworkOption)
                .setRequiresDeviceIdle(mDeviceIdleSwitch.isChecked())
                .setRequiresCharging(mDeviceChargingSwitch.isChecked());

        if (seekBarSet) {
            builder.setOverrideDeadline(seekBarInteger * 1000);
        }
        boolean constraintSet = selectedNetworkOption
                != JobInfo.NETWORK_TYPE_NONE
                || mDeviceChargingSwitch.isChecked()
                || mDeviceIdleSwitch.isChecked()
                || seekBarSet;

        if (constraintSet) {
            JobInfo myJobInfo = builder.build();
            mScheduler.schedule(myJobInfo);
            Toast.makeText(this, R.string.job_scheduled, Toast.LENGTH_SHORT)
                    .show();
        } else {
            Toast.makeText(this, R.string.no_constraint_toast,
                    Toast.LENGTH_SHORT).show();
        }
    }

    /**
     * onClick method for cancelling all existing jobs.
     */
    public void cancelJobs(View view) {

        if (mScheduler != null) {
            mScheduler.cancelAll();
            mScheduler = null;
            Toast.makeText(this, R.string.jobs_canceled, Toast.LENGTH_SHORT)
                    .show();
        }
    }
}
```






## Save Activity State
Depending on system resources and user behavior, each Activity in your app may be destroyed and reconstructed far more frequently than you might think.

The state of each `Activity` is stored as a set of key/value pairs in a `Bundle` object called the `Activity` instance state. The system saves default state information to instance state `Bundle` just before the Activity is stopped, and passes that `Bundle` to the new `Activity` instance to restore.

To keep from losing data in an Activity when it is unexpectedly destroyed and recreated, you need to implement the `onSaveInstanceState()` method. The system calls this method on your Activity (between onPause() and onStop()) when there is a possibility the Activity may be destroyed and recreated.



### Save
```java
@Override
public void onSaveInstanceState(Bundle outState) {
   super.onSaveInstanceState(outState);
   // If the heading is visible, message needs to be saved.
   // Otherwise we're still using default layout.
   if (mReplyHeadTextView.getVisibility() == View.VISIBLE) {
       outState.putBoolean("reply_visible", true);
       outState.putString("reply_text", 
                      mReplyTextView.getText().toString());
   }
}
```

### Restore
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);
   setContentView(R.layout.activity_main);

   Log.d(LOG_TAG, "-------");
   Log.d(LOG_TAG, "onCreate");

   // Initialize all the view variables.
   mMessageEditText = findViewById(R.id.editText_main);
   mReplyHeadTextView = findViewById(R.id.text_header_reply);
   mReplyTextView = findViewById(R.id.text_message_reply);

   // Restore the saved state. 
   // See onSaveInstanceState() for what gets saved.
   if (savedInstanceState != null) {
       boolean isVisible = 
                     savedInstanceState.getBoolean("reply_visible");
       // Show both the header and the message views. If isVisible is
       // false or missing from the bundle, use the default layout.
       if (isVisible) {
           mReplyHeadTextView.setVisibility(View.VISIBLE);
           mReplyTextView.setText(savedInstanceState
                                  .getString("reply_text"));
           mReplyTextView.setVisibility(View.VISIBLE);
       }
   }
}
```

## Save Shared Preference
Shared preferences allow you to store small amounts of primitive data as key/value pairs in a file on the device. To get a handle to a preference file, and to read, write, and manage preference data, use the SharedPreferences class. The Android framework manages the shared preferences file itself. The file is accessible to all the components of your app, but it is not accessible to other apps.

The data you save to shared preferences is different from the data in the saved activity state, which you learned about in an earlier chapter:
* Data in a saved activity instance state is retained across activity instances in the same user session.
* Shared preferences persist across user sessions. Shared preferences persist even if your app stops and restarts, or if the device reboots.

### Save
Saving preferences is a lot like saving the instance state – both operations set aside the data to a Bundle object as a key/value pair. For shared preferences, however, you save that data in the onPause() lifecycle callback, and you need a shared editor object (SharedPreferences.Editor) to write to the shared preferences object.

```java
private SharedPreferences mPreferences;
private String sharedPrefFile = 
   "com.example.android.hellosharedprefs";

@Override
protected void onPause(){
   super.onPause();

   SharedPreferences.Editor preferencesEditor = mPreferences.edit();
   preferencesEditor.putInt(COUNT_KEY, mCount);
   preferencesEditor.putInt(COLOR_KEY, mColor);
   preferencesEditor.apply();
}
```

### Restore
As with the instance state, your app reads any saved shared preferences in the onCreate() method. Every time onCreate() is called – when the app starts, on configuration changes – the shared preferences are used to restore the state of the view.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);
   setContentView(R.layout.activity_main);

   // Initialize views, color, preferences
   mShowCountTextView = (TextView) findViewById(R.id.count_textview);
   mColor = ContextCompat.getColor(this, R.color.default_background);
   mPreferences = getSharedPreferences(
                         mSharedPrefFile, MODE_PRIVATE);

   // Restore preferences
   // Note that the getInt() method takes two arguments: one for the key, and the other for the default value if the key cannot be found. In this case the default value is 0, which is the same as the initial value of mCount.
   mCount = mPreferences.getInt(COUNT_KEY, 0);
   mShowCountTextView.setText(String.format("%s", mCount));
   mColor = mPreferences.getInt(COLOR_KEY, mColor);
   mShowCountTextView.setBackgroundColor(mColor);
}
```

### Reset
```java
public void reset(View view) {
   // Reset count
   mCount = 0;
   mShowCountTextView.setText(String.format("%s", mCount));

   // Reset color
   mColor = ContextCompat.getColor(this, R.color.default_background);
   mShowCountTextView.setBackgroundColor(mColor);

   // Clear preferences
   SharedPreferences.Editor preferencesEditor = mPreferences.edit();
   preferencesEditor.clear();
   preferencesEditor.apply();
}
```


## App Settings
### Create Setting Preference
```xml
implementation 'androidx.preference:preference:1.1.1'
```

```xml
<androidx.preference.SwitchPreferenceCompat
        android:defaultValue="true"
        android:key="example_switch"
        android:summary="@string/switch_summary"
        android:title="@string/switch_title" />
```

### Create an Activity For Setting
```java
public class SettingsActivity extends AppCompatActivity {

    public static final String
            KEY_PREF_EXAMPLE_SWITCH = "example_switch";

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        // Display the Fragment in SettingsActivity
        getSupportFragmentManager().beginTransaction()
                .replace(android.R.id.content, new SettingsFragment())
                .commit();
    }
}
```

### Create a Fragment For Setting
A Fragment is like a modular section of an Activity—it has its own lifecycle and receives its own input events, and you can add or remove a Fragment while the Activity is running. You use a specialized Fragment subclass to display a list of settings. The best practice is to use a regular Activity that hosts a PreferenceFragment that displays the app settings. PreferenceFragment provides a more flexible architecture for your app, compared to using an Activity for the preferences.

You will use PreferenceFragmentCompat rather than PreferenceFragment in order to maintain compatibility with AppCompatActivity.
```java
public class SettingsFragment extends PreferenceFragmentCompat {

    @Override
    public void onCreatePreferences(Bundle
                                            savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences, rootKey);
    }
}
```
### Connect the Settings menu item to SettingsActivity
```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    // Handle action bar item clicks here. The action bar will
    // automatically handle clicks on the Home/Up button, so long
    // as you specify a parent activity in AndroidManifest.xml.
    int id = item.getItemId();

    //noinspection SimplifiableIfStatement
    if (id == R.id.action_settings) {
        Intent intent = new Intent(this, SettingsActivity.class);
        startActivity(intent);
        return true;
    }

    return super.onOptionsItemSelected(item);
}
```
#### Make return easy
```xml
<activity android:name=".SettingsActivity"
            android:label="Settings"
            android:parentActivityName=".MainActivity">
            <meta-data
                android:name="android.support.PARENT_ACTIVITY"
                android:value=".MainActivity"/>
</activity>
```

### Save the default values in shared preferences
Although the default value for the toggle switch setting has already been set in the android:defaultValue attribute, the app must save the default value in the SharedPreferences file for each setting when the user first opens the app.
```java
androidx.preference.PreferenceManager
                .setDefaultValues(this, R.xml.preferences, false);
```
he code above ensures that the settings are properly initialized with their default values. The PreferenceManager.setDefaultValues() method takes three arguments:

* The app context, such as this.
* The resource ID (preferences) for the XML resource file with one or more settings.
* A boolean indicating whether the default values should be set more than once. When false, the system sets the default values only if this method has never been called. As long as you set this third argument to false, you can safely call this method every time MainActivity starts without overriding the user's saved settings values. However, if you set it to true, the method will override any previous values with the defaults.

### Read the changed settings value from shared preferences
Each setting is identified using a key-value pair. The Android system uses this key-value pair when saving or retrieving settings from a SharedPreferences file for your app. When the user changes a setting, the system updates the corresponding value in the SharedPreferences file. To use the value of the setting, the app can use the key to get the setting from the SharedPreferences file using PreferenceManager.getDefaultSharedPreferences()
```java
// example_switch references the key defined above (in the settings preference)
public static final String 
            KEY_PREF_EXAMPLE_SWITCH = "example_switch";

androidx.preference.PreferenceManager
                .setDefaultValues(this, R.xml.preferences, false);
        SharedPreferences sharedPref =
                androidx.preference.PreferenceManager
                        .getDefaultSharedPreferences(this);
        Boolean switchPref = sharedPref.getBoolean
                (KEY_PREF_EXAMPLE_SWITCH, false);
        Toast.makeText(this, switchPref.toString(),
                Toast.LENGTH_SHORT).show();
```

## Location
### Get the last known location
#### Set permission at Manifest
Using the Location API requires permission from the user. Android offers two location permissions:
* ACCESS_COARSE_LOCATION
* ACCESS_FINE_LOCATION
The permission you choose determines the accuracy of the location returned by the API. For this lesson, use the ACCESS_FINE_LOCATION permission, because you want the most accurate location information possible.
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
```

#### Request a permission at runtime
Starting with Android 6.0 (API level 23), it's not always enough to include a permission statement in the manifest. For "dangerous" permissions, you also have to request permission programmatically, at runtime.
```java
private static final String LOG_TAG = MainActivity.class.getSimpleName();


private final int REQUEST_LOCATION_PERMISSION = 1;

private Location mLastLocation;
private FusedLocationProviderClient mFusedLocationClient;
private TextView mLocationTextView;

private void getLocation() {
    // Check permission granted
    if (ActivityCompat.checkSelfPermission(this,
            Manifest.permission.ACCESS_FINE_LOCATION)
            != PackageManager.PERMISSION_GRANTED) {
        // request permission
        ActivityCompat.requestPermissions(this, new String[]
                        {Manifest.permission.ACCESS_FINE_LOCATION},
                REQUEST_LOCATION_PERMISSION);
    } else {
        setLocationOnTextView();
    }
}

// Handle Permission Grant Result
@Override
public void onRequestPermissionsResult(int requestCode,
                                       @NonNull String[] permissions, @NonNull int[] grantResults) {

    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    switch (requestCode) {
        case REQUEST_LOCATION_PERMISSION:
            // If the permission is granted, get the location,
            // otherwise, show a Toast
            if (grantResults.length > 0
                    && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                getLocation();
            } else {
                Toast.makeText(this,
                        "Permission Denied",
                        Toast.LENGTH_SHORT).show();
            }
            break;
    }
}
```

#### Get the last known location
The getLastLocation() method doesn't actually make a location request. It simply returns the location most recently obtained by the FusedLocationProviderClient class.

If no location has been obtained since the device was restarted, the getLastLocation() method may return null. Usually, the getLastLocation() method returns a Location object that contains a timestamp of when this location was obtained.

```java
private void setLocationOnTextView(){
    mFusedLocationClient.getLastLocation().addOnSuccessListener(
            new OnSuccessListener<Location>() {
                @Override
                public void onSuccess(Location location) {
                    if (location != null) {
                        mLastLocation = location;
                        mLocationTextView.setText(
                                getString(R.string.location_text,
                                        mLastLocation.getLatitude(),
                                        mLastLocation.getLongitude(),
                                        mLastLocation.getTime()));
                    } else {
                        mLocationTextView.setText("No Location Returned");
                    }
                }
            });
}
```

### Consistent Tracking
(Link)[https://developer.android.com/codelabs/advanced-android-training-device-location?index=..%2F..advanced-android-training#5]

## System Application
There are two types of system apps:
* Apps installed on the system partition, which can be accomplished by users with root privileges
* Apps signed by the same signing key that signed the firmware
  * to obtain rights to use `android:sharedUserId="android.uid.system"`
