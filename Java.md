
# References
* https://www.geeksforgeeks.org/compilation-execution-java-program/
* http://crackingjavainterviews.blogspot.com/2013/04/what-are-four-principles-of-oop.html
* https://blog.csdn.net/jackfrued/article/details/44921941

# Table of Contents
- [1. Java Overview](#1-java-overview)
  * [1.1 How Java Compiles](#11-how-java-compiles)
  * [1.2 Java vs Python](#12-java-vs-python)
  * [1.3 JRE, JDK, JVM](#13-jre--jdk--jvm)
- [2. OOP Concepts](#2-oop-concepts)
  * [2.1 Definition](#21-definition)
  * [2.2 Four Basic Concepts](#22-four-basic-concepts)
- [3. Objects](#3-objects)
  * [3.1 Storage of Objects](#31-storage-of-objects)
  * [3.2 Primitive Types](#32-primitive-types)
    + [3.2.1 Wrapper classes](#321-wrapper-classes)
  * [3.3 Array of Objects](#33-array-of-objects)
  * [3.4 Scoping](#34-scoping)
  * [3.5 Class](#35-class)
- [4. Flow Control](#4-flow-control)
  * [4.1 Operators](#41-operators)
    + [4.1.1 Assigment](#411-assigment)
    + [4.1.2 Relational](#412-relational)
    + [4.1.3 Logical](#413-logical)
    + [4.1.4 Shift Operators](#414-shift-operators)
    + [4.1.5 String operator +](#415-string-operator--)
    + [4.1.6 Casting Operator](#416-casting-operator)
    + [4.1.7 No Sizeof() Function](#417-no-sizeof---function)
  * [4.2 Execution Control](#42-execution-control)
    + [4.2.1 IF-ELSE](#421-if-else)
    + [4.2.2 For](#422-for)
    + [4.2.3 GOTO](#423-goto)
    + [4.2.4 Switch](#424-switch)
- [5. Class](#5-class)
  * [5.1 Constructor](#51-constructor)
  * [5.2 Methods](#52-methods)
    + [5.2.1 Type of Methods](#521-type-of-methods)
    + [5.2.2 Method Overloading](#522-method-overloading)
    + [5.2.3 Method Overriding](#523-method-overriding)
  * [5.3 Default Constructor](#53-default-constructor)
  * [5.4 This](#54-this)
  * [5.5 Finalize](#55-finalize)
  * [5.6 GC](#56-gc)
  * [5.7 Intialization](#57-intialization)
- [6. Package](#6-package)
  * [6.1 Package Path](#61-package-path)
  * [6.2 Jar](#62-jar)
  * [6.3 Access Specifiers](#63-access-specifiers)
  * [6.4 Class Access](#64-class-access)
- [7. Reusing Classes](#7-reusing-classes)
  * [7.1 Association, Composition and Aggregation](#71-association--composition-and-aggregation)
    + [7.1.1 Association](#711-association)
    + [7.1.2 Aggregation](#712-aggregation)
    + [7.1.3 Composition](#713-composition)
  * [7.2 Inheitance](#72-inheitance)
    + [7.2.1 Initialize base class](#721-initialize-base-class)
    + [7.2.2 Name Hiding](#722-name-hiding)
  * [7.3 Composition vs Inheritance](#73-composition-vs-inheritance)
  * [7.4 Protected and Private](#74-protected-and-private)
  * [7.5 Upcasting a class](#75-upcasting-a-class)
  * [7.6 Final](#76-final)
    + [7.6.1 Final Data Member](#761-final-data-member)
    + [7.6.2 Final Methods](#762-final-methods)
    + [7.6.3 Final Class](#763-final-class)
- [8. Polymorphism](#8-polymorphism)
  * [8.1 Method Call Binding](#81-method-call-binding)
    + [8.1.1 Static Binding](#811-static-binding)
    + [8.1.2 Dynamic Binding](#812-dynamic-binding)
  * [8.2 Abstract Classes and Methods](#82-abstract-classes-and-methods)
    + [8.2.1 Abstract Methods](#821-abstract-methods)
    + [8.2.2 Abstract Classes](#822-abstract-classes)
  * [8.3 Behavior of polymorphic methods inside constructors](#83-behavior-of-polymorphic-methods-inside-constructors)
- [9. Interface and Inner Classes](#9-interface-and-inner-classes)
  * [9.1 Interface](#91-interface)
    + [9.1.1 Properties](#911-properties)
    + [9.1.2 Why interface?](#912-why-interface-)
  * [9.2 Inner classes](#92-inner-classes)
    + [9.2.1 Nested Inner class](#921-nested-inner-class)
    + [9.2.2 Method Local inner classes](#922-method-local-inner-classes)
    + [9.2.3 Static nested classes](#923-static-nested-classes)
    + [9.2.4 Anonymous inner classes](#924-anonymous-inner-classes)
    + [9.2.5 Why inner class?](#925-why-inner-class-)
- [10. Exceptions](#10-exceptions)
  * [10.1 Cathing an exception](#101-cathing-an-exception)
  * [10.2 Creating an exception](#102-creating-an-exception)
  * [10.3 Exception vs Error](#103-exception-vs-error)
- [11. Serialization and Deserialization](#11-serialization-and-deserialization)
  * [11.1 Use Serialization](#111-use-serialization)
  * [11.2 Why Serialization](#112-why-serialization)
  * [11.3 Externalizable](#113-externalizable)
  * [11.4 Cloneable](#114-cloneable)
- [12. Multithreading](#12-multithreading)
  * [12.1 Thread Class vs Runnable Interface](#121-thread-class-vs-runnable-interface)
    + [12.1.1 Extending the Thread class](#1211-extending-the-thread-class)
    + [12.1.2 Implementing the Runnable Interface](#1212-implementing-the-runnable-interface)
    + [12.1.3 Thread Class vs Runnable Interface](#1213-thread-class-vs-runnable-interface)
  * [12.2 Life Cycle of A Thread](#122-life-cycle-of-a-thread)
  * [12.3 Main Thread](#123-main-thread)
    + [12.3.1 Property](#1231-property)
    + [12.3.2 Controlling Main thread](#1232-controlling-main-thread)
    + [12.3.3 Main Thread and Main Function](#1233-main-thread-and-main-function)
  * [12.4 Volatile vs Synchronized](#124-volatile-vs-synchronized)
    + [12.4.1 Synchronized](#1241-synchronized)
    + [12.4.2 Volatile Keyword](#1242-volatile-keyword)
    + [12.4.3 Volatile vs Synchronized](#1243-volatile-vs-synchronized)
  * [12.5 Thread Related Methods](#125-thread-related-methods)
    + [12.5.1 Single-Thread Methods](#1251-single-thread-methods)
      - [12.5.1.1 yield](#12511-yield)
      - [12.5.1.2 sleep](#12512-sleep)
      - [12.5.1.3 yield vs sleep](#12513-yield-vs-sleep)
      - [12.5.1.4 join](#12514-join)
    + [12.5.2 Inter-thread Methods](#1252-inter-thread-methods)
      - [12.5.2.1 Polling](#12521-polling)
      - [12.5.2.2 Polling in Multithreading](#12522-polling-in-multithreading)
  * [12.6 ReentrantLock](#126-reentrantlock)
  * [12.7 Daemon thread](#127-daemon-thread)
  * [12.8 Advanced Multithreading](#128-advanced-multithreading)
- [13. Collections](#13-collections)
  * [13.1 Iterators](#131-iterators)
    + [13.1.1 Enumeration](#1311-enumeration)
    + [13.1.2 Iterator](#1312-iterator)
    + [13.1.3 ListIterator](#1313-listiterator)
    + [13.1.4 Notice](#1314-notice)
  * [13.2 Collections](#132-collections)
  * [13.3 Use Iterator](#133-use-iterator)
  * [13.4 Iterator vs Foreach](#134-iterator-vs-foreach)
    + [13.4.1 Difference:](#1341-difference-)
    + [13.4.2 When to Use Which:](#1342-when-to-use-which-)
    + [13.4.3 Performance](#1343-performance)
  * [13.5 Retrieving Elements from Collections](#135-retrieving-elements-from-collections)
    + [13.5.1 For-each](#1351-for-each)
    + [13.5.2 Using Cursors](#1352-using-cursors)
  * [13.6 Set Interface](#136-set-interface)
  * [13.7 List Interface](#137-list-interface)
  * [13.8 HashSet](#138-hashset)
  * [13.9 LinkedList](#139-linkedlist)
  * [13.10 ArrayList](#1310-arraylist)
  * [13.11 ArrayList vs LinkedList in Java](#1311-arraylist-vs-linkedlist-in-java)
  * [13.12 Map Interface](#1312-map-interface)
  * [13.13 HashMap](#1313-hashmap)
  * [13.14 More](#1314-more)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# 1. Java Overview
## 1.1 How Java Compiles
* Javac.exe compiles source file (.java) into byte code files (.class). Pass this file to JVM
* There are three stages executed in JVM:
    * Load main class 
    * Bytecode Verifier (initialize, type checking)
    * Just-In-Time Compiler (JIT) translates code into machine code

## 1.2 Java vs Python
| Category | Java | Python |
| ---- | ---- | ---- |
| Variable Type | statically typed, compiled language | dynamically typed, non-compiled (scripting)|
| | In Java, all variable names (along with their types) must be explicitly declared. Attempting to assign an object of the wrong type to a variable name triggers a type exception.| In Python, you never declare anything. An assignment statement binds a name to an object, and the object can be of any type. |
| Style | verbose | concise |
| | containing more words than are necessary| expressing much in a few words. Implies clean-cut brevity|
| Speed | In general Java is faster | Python is slower|
| Cross-Platform| Java is translated into Java Byte code| Python relies on compiler that can turn Python code into code that your particular operating system can understand.|

## 1.3 JRE, JDK, JVM
* JVM is an acronym for Java Virtual Machine, it is an abstract machine which provides the runtime environment in which java bytecode can be executed. It is a specification. JVMs are available for many hardware and software platforms (so JVM is platform dependent).

* JRE stands for Java Runtime Environment. It is the implementation of JVM.

* JDK is an acronym for Java Development Kit. It physically exists. It contains JRE + development tools.
    
# 2. OOP Concepts
## 2.1 Definition
In OOP languages, programmers define**not only the data type of a data structure, but also the types of operations (functions)** that can be applied to the data structure.

## 2.2 Four Basic Concepts
1. Encapsulation: **hiding of data implementation** by restricting access to public methods.
2. Abstraction: using abstract class/interface to **express the intent of the class rather than the actual implementation**.
3. Polymorphism: **"One name many forms."** It is further of two types - static and dynamic. Static polymorphism is achieved using method overloading and dynamic polymorphism using method overriding
4. Inheritance: **"Inherit the features(fields and methods) of another class"**. We can reuse the code of existing super classes.

# 3. Objects
## 3.1 Storage of Objects
1. Registers.
2. The stack: references to objects and primitive types.
3. The heap: Actual objects.
4. Static Storage: in a fixed location
5. Constants: Placed in the program code

## 3.2 Primitive Types
8 primitive types (digits, chars, byte and boolean): byte、short、int、long、float、double、char、boolean. **No reference** is created for primitive types. **String** is not primitive. Java also have high-precision classes like BigInteger and BigDecimal

### 3.2.1 Wrapper classes
A Wrapper class is a class whose object wraps or contains a primitive data types. When we create an object to a wrapper class, it contains a field and in this field, we can store a primitive data types.
* They convert primitive data types into objects. Objects are needed if we wish to modify the arguments passed into a method (because primitive types are passed by value).
* The classes in java.util package handles only objects and hence wrapper classes help in this case also.
* Data structures in the Collection framework, such as ArrayList and Vector, store only objects (reference types) and not primitive types.
* An object is needed to support synchronization in multithreading.

## 3.3 Array of Objects
When creating an array of objects, you **actually create an array of references**, each reference is initialized to null. You can create an array of primitives, the compiler zeros the memory.
```java
int[] myIntArray = new int[3];
String[] myStringArray = new String[3];
```

## 3.4 Scoping
Code scope is determined by curly braces. Objects created with **new** stay as long as you want. When no reference is pointing to one object, this object is collected by GC.

## 3.5 Class
Each class has two crucial components:
1. Data Members
2. Methods (Including constructor)

# 4. Flow Control
## 4.1 Operators
### 4.1.1 Assigment
```java
a = b
```
### 4.1.2 Relational
```java
a == b
a.equals(b)
```
To compare the relationship between two object, you **override equals()** function, and **hashcode()** function. Two objects **are equal should have same hashcode**
### 4.1.3 Logical
```java
a && b
c || d
```
### 4.1.4 Shift Operators
```java
9 << 1
4 >> 1
```
### 4.1.5 String operator +
Concatenate two strings
```java
"afb" + "bcd"
```
### 4.1.6 Casting Operator
Auto casting from low precision to high precision (i.e. appropriate)

### 4.1.7 No Sizeof() Function
All sizes are consistent across different platforms.

## 4.2 Execution Control
### 4.2.1 IF-ELSE
```java
if(a == 3)
{
    System.out.println("Equals")
}
```
### 4.2.2 For
```java
for (int x = 2; x <= 4; x++)
{
    System.out.println("Value of x:" + x);
}

String[] array = {"Ron", "Harry", "Hermoine"};
//enhanced for loop
for (String x:array)
{
    System.out.println(x);
}        
```
### 4.2.3 GOTO
Goto is reserved but not used in the langauge.

### 4.2.4 Switch
```java
int month = 8;
switch (month) {
    case 1:  monthString = "January";
             break;
    case 2:  monthString = "February";
             break;
}
```

# 5. Class
## 5.1 Constructor
Constructor creates objects from the class blueprint. They use the name of the class and have no return type
```java

public Bicycle(int startCadence, int startSpeed, int startGear) {
    this.gear = startGear;
    this.cadence = startCadence;
    this.speed = startSpeed;
}
```

## 5.2 Methods
### 5.2.1 Type of Methods
* Instance method. Instance method are methods which **require an object** of its class to be created before it can be called.

```java
class Foo{
     
    String name = "";
     
    // Instance method to be called within the same class or 
    // from a another class defined in the same package
    // or in different package. 
    public void geek(String name){
         
        this.name = name;
    }
}
 
class GFG {
    public static void main (String[] args) {
     
        // create an instance of the class.
        Foo ob = new Foo();
          
        // calling an instance method in the class 'Foo'.
        ob.geek("GeeksforGeeks");
        System.out.println(ob.name);
    }
}
```

* Static methods are the methods in Java that can be called without creating an object of class. They are referenced **by the class name itself or reference to the Object** of that class.

```java
class Geek{
     
    public static String geekName = "";
     
    public static void geek(String name){
         
        geekName = name;
    }
}
 
class GFG {
    public static void main (String[] args) {
         
        // Accessing the static method geek() and 
        // field by class name itself.
        Geek.geek("vaibhav"); 
        System.out.println(Geek.geekName);
        
        // Accessing the static method geek() by using Object's reference.
        Geek obj = new Geek();
        obj.geek("mohit");
        System.out.println(obj.geekName);   
         
        
    }
}
```

### 5.2.2 Method Overloading
More than one method having the same name, if their argument lists are different. **Cannot overloading on different return types**

```java
class DisplayOverloading
{
    public void disp(char c)
    {
         System.out.println(c);
    }
    public void disp(char c, int num)  
    {
         System.out.println(c + " "+num);
    }
}
```

**Overloading Premitives**
Java searched up in this case. I.e. int -> long -> float.

```java
public class Conversion 
{
    // overloaded method
    public void method(int i)
    {
        System.out.println("Primitive type int formal argument :" + i);
    }
     
    // overloaded method primitive formal argument
    // and to be invoked for wrapper Object as 
 
    public void method(float i)
    {
         
        System.out.println("Primitive type float formal argument :" + i);
    }
}

class GFG 
{
     
    public static void main (String[] args)
    {
     
        Conversion c = new Conversion();
         
        // invoking the method with signature
        // has widened data type
        c.method(10);
        c.method(new Long(100));
    }
}
```

### 5.2.3 Method Overriding
Overriding is a feature that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. Method overriding is one of the way by which java achieve **Run Time Polymorphism**. 
```java
// Base Class
class Parent
{
    void show() { System.out.println("Parent's show()"); }
}
 
// Inherited class
class Child extends Parent
{
    // This method overrides show() of Parent
    @Override
    void show() { System.out.println("Child's show()"); }
}
 
// Driver class
class Main
{
    public static void main(String[] args)
    {
        // If a Parent type reference refers
        // to a Parent object, then Parent's
        // show is called
        Parent obj1 = new Parent();
        obj1.show();
 
        // If a Parent type reference refers
        // to a Child object Child's show()
        // is called. This is called RUN TIME
        // POLYMORPHISM.
        Parent obj2 = new Child();
        obj2.show();
    }
 //Parent's show()
 //Child's show()
}
```
* **Final methods** cannot be overridden
* **Private Methods** cannot be overridden
* **Static methods** can not be overridden(Method Overriding vs Method Hiding) : When you defines a static method with same signature as a static method in base class, it is known as **method hiding** (subclass function hides).
* Invoking overridden method from sub-class : We can call parent class method in overriding method using super keyword
* We **can not override constructor**.

```java
public class NewClass
{
    public static class superclass
    {
        static void print()
        {
            System.out.println("print in superclass.");
        }
    }
    public static class subclass extends superclass
    {
        static void print()
        {
            System.out.println("print in subclass.");
        }
    }
 
    public static void main(String[] args)
    {
        superclass A = new superclass();
        superclass B = new subclass();
        A.print();
        B.print();
     //print in superclass.
     //print in superclass.
    }
}
```

## 5.3 Default Constructor
Java **automatically creates default constructor (no param)** if there is no default or parameterized constructor written by user. Default constructor in Java initializes member data variable to **null/0/false**.

## 5.4 This
This is used to reference to the object internally.

## 5.5 Finalize
It is a method that the Garbage Collector always **calls just before the deletion/destroying** the object which is eligible for Garbage Collection, so as to **perform clean-up** activity. Clean-up activity means closing the resources associated with that object **like Database Connection, Network Connection**

## 5.6 GC
What GC do?
1. Use reference counting
2. Stop and Copy. Make it compact.
3. Mark and Sweep. Release garbage.

## 5.7 Intialization
1. Local initialzation: No auto intialization
2. Object Member Intialization: To 0/false/null
3. Static Initialization: same as member

Order of initialization: static first, then non-static.

# 6. Package
## 6.1 Package Path
E:\Libararies\com\liu\simple\a.java

**CLASSPATH**: "E:\Libararies\"

**PACKAGE PATH**: com.liu.simple


## 6.2 Jar
A working program of compressed .class files.

## 6.3 Access Specifiers
Access specifier for **class members **. **Not Class**.

| Access Specifiers| Current Class| Same Package| Sub Class (Extended)| Other Package|
| ---------------- | ------------ | ----------- | -------- | ------------ |
| Public | √ | √ | √ | √ |
| Protected | √ | √ | √ | × |
| Default (Friendly) | √ | √ | × | × |
| Private | √ | × | × | × |

## 6.4 Class Access
1. **Only One Public Class** per java file.
2. **Public Class name matches file name**
3. It is possible to have non-public class.
4. Class access is eitehr **Public ** or **Friendly**. **No protect and private** before class.

# 7. Reusing Classes
Two ways of reusing classes
1. Composition
2. Inheritance

## 7.1 Association, Composition and Aggregation
### 7.1.1 Association
Association is relation between two separate classes which establishes through their Objects. Association can be one-to-one, one-to-many, many-to-one, many-to-many. (student - teacher)

### 7.1.2 Aggregation
It is a special form of Association where:

* It represents Has-A relationship.
* It is a unidirectional association i.e. a one way relationship. For example, department can have students but vice versa is not possible and thus unidirectional in nature.
* In Aggregation, both the entries can survive individually which means ending one entity will not effect the other entity


### 7.1.3 Composition
Composition is a **restricted form of Aggregation** in which two entities are highly dependent on each other. One class contain another class directly. It represents part-of relationship. In composition, both the entities are dependent on each other. When there is a composition between two entities, the composed object cannot exist without the other entity. Example:
```java
// class book
class Book 
{
 
    public String title;
    public String author;
     
    Book(String title, String author)
    {
         
        this.title = title;
        this.author = author;
    }
}
 
// Libary class contains 
// list of books.
class Library 
{
 
    // reference to refer to list of books.
    private final List<Book> books;
     
    Library (List<Book> books)
    {
        this.books = books; 
    }
     
    public List<Book> getTotalBooksInLibrary(){
         
       return books;  
    }
     
}
```

## 7.2 Inheitance
You are always doing inheritance when you create a class -- from **Object Class**.
```java
class A extends B{
}
```
1. The derived class will automatically get all the data members and methods in the base class. 
2. To plan for inheritance, a general rule is to make all fields **private** and all methods **public or protected** so that sub class can use it. 
3. Use **super** to class base-class functions
```java
super.scrub()
```

### 7.2.1 Initialize base class
Java automatically calls constructor of super class of no parameter. If we want to call parameterized contructor of base class, then we can call it using super(). The point to note is **base class constructor call must be the first line in derived class constructor**.
```java
// filename: Main.java
class Base {
  int x;
  Base(int _x) {
    x = _x;
  }
}
 
class Derived extends Base {
  int y;
  Derived(int _x, int _y) {
    super(_x);
    y = _y;
  }
  void Display() {
    System.out.println("x = "+x+", y = "+y);
  }
}
 
public class Main {
  public static void main(String[] args) {  
    Derived d = new Derived(10, 20);
    d.Display();
  }
}
```

### 7.2.2 Name Hiding
Overloading a method that exist in super class does not hide overloaded methods in super class. Example:
```java
class Homer {
  char doh(char c) {
    System.out.println("doh(char)");
    return 'd';
  }

  float doh(float f) {
    System.out.println("doh(float)");
    return 1.0f;
  }
}

class Milhouse {
}

class Bart extends Homer {
  void doh(Milhouse m) {
    System.out.println("doh(Milhouse)");
  }
}

// Even though doh is overloaded in subclass, the functions defined in super class is still valid.
public class Hide {
  public static void main(String[] args) {
    Bart b = new Bart();
    b.doh(1); //float
    b.doh('x'); //char
    b.doh(1.0f); //float
    b.doh(new Milhouse()); //milhouse
  }
} 
```

## 7.3 Composition vs Inheritance
If something is-a --- inheritance. If something has-a --- composition

## 7.4 Protected and Private
Protected methods are available to sub classes, but private methods are not available.

## 7.5 Upcasting a class
From sub class to super class. Upcasting is always **safe** because you are going from a specific type to a more general type. When you upcast a class, **the method used is still the methods overriden in subclass**.
```java
public class NewClass
{
    public static class superclass
    {
     void print()
        {
            System.out.println("print in superclass.");
        }
    }
    public static class subclass extends superclass
    {
     void print()
        {
            System.out.println("print in subclass.");
        }
    }
 
    public static void main(String[] args)
    {
        superclass A = new superclass();
        superclass B = new subclass();
        A.print();
        B.print();
     //print in superclass.
     //print in subclass.
    }
}
```

## 7.6 Final
"Cannot be changed"

### 7.6.1 Final Data Member
1. Compile-time constant that wont change ever
2. Initialized at run-time that you dont want change.
3. "static" + "final" has only one piece of storage that cant be changed
4. With a primitive, final makes the value a constant. With object reference, final makes the **reference a constant**, **the object itself can be modified**.
5. Blank Final: a final variable that is not initialized during declaration.
```java
// A simple blank final example 
final int i;
i = 30;
```

### 7.6.2 Final Methods
"This method cannot be overriden"
1. All **private** methods are **implicitly final**. If you try to override a private method, you just **created a new one**.
2. **Overriding** can only occur if **the method is part of the base-class interface**.

### 7.6.3 Final Class
"Cannot be inherited"

# 8. Polymorphism
The characteristic of being able to assign a different meaning or usage to one thing ("one name multiple forms").

## 8.1 Method Call Binding
### 8.1.1 Static Binding
The binding which can be resolved at compile time by compiler is known as static or early binding. Binding of all the **static, private and final methods** is done at compile-time. ("all such **methods cannot be overridden** and will always be accessed by object of local class")
```java
public class NewClass
{
    public static class superclass
    {
        static void print()
        {
            System.out.println("print in superclass.");
        }
    }
    public static class subclass extends superclass
    {
        static void print()
        {
            System.out.println("print in subclass.");
        }
    }
 
    public static void main(String[] args)
    {
        superclass A = new superclass();
        superclass B = new subclass();
        A.print();
        B.print();
     //print in superclass.
     //print in superclass.
    }
}
```
### 8.1.2 Dynamic Binding
In Dynamic binding compiler doesn’t decide the method to be called. Overriding is a perfect example of dynamic binding. In overriding both parent and child classes have same method.
```java
public class NewClass
{
    public static class superclass
    {
        void print()
        {
            System.out.println("print in superclass.");
        }
    }
 
    public static class subclass extends superclass
    {
        @Override
        void print()
        {
            System.out.println("print in subclass.");
        }
    }
 
    public static void main(String[] args)
    {
        superclass A = new superclass();
        superclass B = new subclass();
        A.print();
        B.print();
     //print in superclass.
     //print in superclass.
    }
}
```

## 8.2 Abstract Classes and Methods
### 8.2.1 Abstract Methods
A method that is **not complete**. It has **only a declaration** and no method body.
```java
public abstract class GraphicObject {
   // declare fields
   // declare nonabstract methods
   abstract void draw();
}
```

### 8.2.2 Abstract Classes
Abstract classes are something you cannot instantiate.

* In Java, **an instance of an abstract class cannot be created**, we can have references of abstract class type though.

```java
abstract class Base {
    abstract void fun();
}
class Derived extends Base {
    void fun() { System.out.println("Derived fun() called"); }
}
class Main {
    public static void main(String args[]) { 
     
        // Uncommenting the following line will cause compiler error as the 
        // line tries to create an instance of abstract class.
        // Base b = new Base();
 
        // We can have references of Base type.
        Base b = new Derived();
        b.fun(); 
    }
}
```

* An abstract class can contain constructors in Java. And a constructor of abstract class is called when an instance of a inherited class is created.

```java
// An abstract class with constructor
abstract class Base {
    Base() { System.out.println("Base Constructor Called"); }
    abstract void fun();
}
class Derived extends Base {
    Derived() { System.out.println("Derived Constructor Called"); }
    void fun() { System.out.println("Derived fun() called"); }
}
class Main {
    public static void main(String args[]) { 
       Derived d = new Derived();
    }
```

* In Java, we can have an abstract class without any abstract method. This allows us to **create classes that cannot be instantiated (cant initiate abstract class), but can only be inherited.**

```java
// An abstract class without any abstract method
abstract class Base {   
    void fun() { System.out.println("Base fun() called"); }
}
  
class Derived extends Base { }
  
class Main {
    public static void main(String args[]) { 
        Derived d = new Derived();
        d.fun();
    }
}
```

* **Not all methods** have to be abstract in an abstract class.
* If you inherit an abstract class and want to make objects of this new type, you need to provide method definitions for **all abstract methods**.

## 8.3 Behavior of polymorphic methods inside constructors
[Reference](https://www.codeguru.com/java/tij/tij0082.shtml)

The hierarchy of constructor calls brings up an interesting dilemma. What happens if you’re inside a constructor and you call a dynamically-bound method of the object being constructed? Inside an ordinary method you can imagine what will happen – the dynamically-bound call is resolved at run-time because the object cannot know whether it belongs to the class the method is in or some class derived from it. For consistency, you might think this is what should happen inside constructors.

This is not exactly the case. If you call a dynamically-bound method inside a constructor, the overridden definition for that method is used. However, the effect can be rather unexpected, and can conceal some difficult-to-find bugs.

Conceptually, the constructor’s job is to bring the object into existence (which is hardly an ordinary feat). Inside any constructor, the entire object might be only partially formed – you can know only that the base-class objects have been initialized, but you cannot know which classes are inherited from you. A dynamically-bound method call, however, reaches “forward” or “outward” into the inheritance hierarchy. It calls a method in a derived class. If you do this inside a constructor, you call a method that might manipulate members that haven’t been initialized yet – a sure recipe for disaster.

```java
abstract class Glyph {
  abstract void draw();
  Glyph() {
    System.out.println("Glyph() before draw()");
    draw(); 
    System.out.println("Glyph() after draw()");
  }
}
 
class RoundGlyph extends Glyph {
  int radius = 1;
  RoundGlyph(int r) {
    radius = r;
    System.out.println(
      "RoundGlyph.RoundGlyph(), radius = "
      + radius);
  }
  void draw() { 
    System.out.println(
      "RoundGlyph.draw(), radius = " + radius);
  }
}
 
public class PolyConstructors {
  public static void main(String[] args) {
    new RoundGlyph(5);
  }
} ///:~ 
```


# 9. Interface and Inner Classes
## 9.1 Interface
Think of interfaces as "pure" abstract class. 
### 9.1.1 Properties
* Interface can have methods and variables (final public and static), but the methods declared in interface are **all abstract**. 
* Interface **cannot have constructors**. 
* Methods from the interface **must** be defined as **public**.
* Variables in interface are **final and static**.

### 9.1.2 Why interface?
Why do we use interface?
* It is used to achieve total abstraction.
* Since java does not support **multiple inheritance** in case of class, but by using interface it can achieve multiple inheritance .
* Interfaces are used to implement abstraction. So the question arises why use interfaces when we have abstract classes? The reason is, abstract classes may contain non-final variables, whereas variables in interface are **final, public and static**.

## 9.2 Inner classes
A class defined in another class. There are four types of inner classes.
1. Nested Inner class
2. Method Local inner classes
3. Anonymous inner classes
4. Static nested classes

### 9.2.1 Nested Inner class
Nested Inner class can **access any private instance variable of outer class**. Like any other instance variable, we can have access modifier private, protected, public and default modifier. Like class, interface can also be nested and can have access specifiers.
```java
public class Outer {
   public int x = 0;
   // Simple nested inner class
   class Inner {
      public void show() {
           System.out.println("In a nested class method"); 
           System.out.println(Outer.this.x);
      }
   }
   
   public static void main(String[] args) {
       Outer.Inner in = new Outer().new Inner();
       in.show(); //In a nested class method; 0
   }
}
```
As a side note, we **can’t have static method in a nested inner class** because an inner class is implicitly associated with an object of its outer class so it cannot define any static method for itself.

### 9.2.2 Method Local inner classes
Inner class can be declared within a method of an outer class. In the following example, Inner is an inner class in outerMethod().
```java
class Outer {
    void outerMethod() {
        System.out.println("inside outerMethod");
        // Inner class is local to outerMethod()
        class Inner {
            void innerMethod() {
                System.out.println("inside innerMethod");
            }
        }
        Inner y = new Inner();
        y.innerMethod();
    }
}
class MethodDemo {
    public static void main(String[] args) {
        Outer x = new Outer();
        x.outerMethod();
        //Inside outerMethod
        //Inside innerMethod
    }
}
```
Method Local inner classes **can’t use local variable of outer method** unless that local variable is not declared as final.

### 9.2.3 Static nested classes
Static nested classes are not technically an inner class. They are like a static member of outer class.
```java
class Outer {
   private static void outerMethod() {
     System.out.println("inside outerMethod");
   }
    
   // A static inner class
   static class Inner {
     public static void main(String[] args) {
        System.out.println("inside inner class Method");
        outerMethod();
     }
   }
 //inside inner class Method
 //inside outerMethod 
         
}
```

### 9.2.4 Anonymous inner classes
Anonymous inner classes are declared without any name at all. They are created in two ways.
* As subclass of specified type

```java
class Demo {
   void show() {
      System.out.println("i am in show method of super class");
   }
}
class Flavor1Demo {
 
   //  An anonymous class with Demo as base class
   static Demo d = new Demo() {
       void show() {
           super.show();
           System.out.println("i am in Flavor1Demo class");
       }
   };
   public static void main(String[] args){
       d.show();
   }
}
//i am in show method of super class
//i am in Flavor1Demo class 
```
In the above code, we have two class Demo and Flavor1Demo. Here demo act as super class and anonymous class acts as a subclass, both classes have a method show(). In anonymous class show() method is overridden.

* As implementer of the specified interface

```java
class Flavor2Demo {
 
    // An anonymous class that implements Hello interface
    static Hello h = new Hello() {
        public void show() {
            System.out.println("i am in anonymous class");
        }
    };
 
    public static void main(String[] args) {
        h.show();
        //i am in anonymous class
    }
}
 
interface Hello {
    void show();
}
```
In above code we create an object of anonymous inner class but this anonymous inner class is an implementer of the interface Hello. Any anonymous inner class can implement only one interface at one time. It can either extend a class or implement interface at a time.

### 9.2.5 Why inner class?
Allows you to group classes that logically belong together, also control the visibility.


# 10. Exceptions
## 10.1 Cathing an exception
```java
//Parent class will always catch sub class
try {
// block of code to monitor for errors
// the code you think can raise an exception
}
catch (ExceptionType1 exOb) {
// exception handler for ExceptionType1
}
catch (ExceptionType2 exOb) {
// exception handler for ExceptionType2
}
// optional
finally {
// block of code to be executed after try block ends
}
```
Notes:
* For each try block there can be zero or more catch blocks, but only **one finally block**.
* The finally block is optional.It **always gets executed** whether an exception occurred in try block or not .
* java terminates the program where exception happens.

## 10.2 Creating an exception
[Reference](https://www.geeksforgeeks.org/throw-throws-java/)
* Use **throw**, in the code

```java
// Java program that demonstrates the use of throw
class ThrowExcep
{
    static void fun()
    {
        try
        {
            throw new NullPointerException("demo");
        }
        catch(NullPointerException e)
        {
            System.out.println("Caught inside fun().");
            throw e; // rethrowing the exception
        }
    }
 
    public static void main(String args[])
    {
        try
        {
            fun();
        }
        catch(NullPointerException e)
        {
            System.out.println("Caught in main.");
        }
    }
}
```

* Use **throws**, in definition

```java
// Java program to illustrate throws
class tst 
{
    public static void main(String[] args)throws InterruptedException
    {
        Thread.sleep(10000);
        System.out.println("Hello Geeks");
    }
}
```

Comparison:

|Throw| Throws|
| --- | ------|
|throw is used to explicitly throw an exception|throws is used to declare an exception|
|throw is used within the method|throws is used with the method signature|
|You cannot throw multiple exception|You can declare multiple exception e.g. public void method()throws IOException,SQLException.|


## 10.3 Exception vs Error
An error is an irrecoverable condition occurring at runtime. Such as OutOfMemory error. 

While exceptions are conditions that occur because of bad input or human error etc. e.g. FileNotFoundException will be thrown if the specified file does not exist.

# 11. Serialization and Deserialization
[Reference](https://www.geeksforgeeks.org/serialization-in-java/)

Serialization is a mechanism of **converting the state of an object into a byte stream**. Deserialization is the reverse process where the byte stream is used to recreate the actual Java object in memory. This mechanism is used to persist the object. The byte stream created is **platform independent**. So, the object serialized on one platform can be deserialized on a different platform.

## 11.1 Use Serialization
* To make a Java object serializable we **implement the java.io.Serializable interface**. 
* The ObjectOutputStream class contains **writeObject()** method for serializing an Object.
* The ObjectInputStream class contains **readObject()** method for deserializing an object.
* Serializable is a **marker interface** (has no data member and method).
* Only **non-static data members** are saved via Serialization process
* **Static** data members and **transient** data members are **not** saved via Serialization process.
* serialversionUID which is used during Deserialization to verify that sender and reciever of a serialized object have loaded classes for that object which are compatible with respect to serialization. (i.e., **verify same class type**)
* During the process of deserialization, **no constructor called**.

```java
class Emp implements Serializable {
private static final long serialversionUID =
                                 129348938L;
    transient int a;
    static int b;
    String name;
    int age;
 
    // Default constructor
public Emp(String name, int age, int a, int b)
    {
        this.name = name;
        this.age = age;
        this.a = a;
        this.b = b;
    }
 
}
 
public class SerialExample {
public static void printdata(Emp object1)
    {
 
        System.out.println("name = " + object1.name);
        System.out.println("age = " + object1.age);
        System.out.println("a = " + object1.a);
        System.out.println("b = " + object1.b);
    }
 
public static void main(String[] args)
    {
        Emp object = new Emp("ab", 20, 2, 1000);
        String filename = "shubham.txt";
 
        // Serialization
        try {
 
            // Saving of object in a file
            FileOutputStream file = new FileOutputStream
                                           (filename);
            ObjectOutputStream out = new ObjectOutputStream
                                           (file);
 
            // Method for serialization of object
            out.writeObject(object);
 
            out.close();
            file.close();
 
            System.out.println("Object has been serialized\n"
                              + "Data before Deserialization.");
            printdata(object);
 
            // value of static variable changed
            object.b = 2000;
        }
 
        catch (IOException ex) {
            System.out.println("IOException is caught");
        }
 
        object = null;
 
        // Deserialization
        try {
 
            // Reading the object from a file
            FileInputStream file = new FileInputStream
                                         (filename);
            ObjectInputStream in = new ObjectInputStream
                                         (file);
 
            // Method for deserialization of object
            object = (Emp)in.readObject();
 
            in.close();
            file.close();
            System.out.println("Object has been deserialized\n"
                                + "Data after Deserialization.");
            printdata(object);
 
            // System.out.println("z = " + object1.z);
        }
 
        catch (IOException ex) {
            System.out.println("IOException is caught");
        }
 
        catch (ClassNotFoundException ex) {
            System.out.println("ClassNotFoundException" +
                                " is caught");
        }
    }
}

/*
Object has been serialized
Data before Deserialization.
name = ab
age = 20
a = 2
b = 1000
Object has been deserialized
Data after Deserialization.
name = ab
age = 20
a = 0
b = 2000
*/
```


## 11.2 Why Serialization
* To save/persist state of an object.
* To travel an object across a network.

## 11.3 Externalizable
Externalization serves the purpose of custom Serialization.
[Reference](https://www.geeksforgeeks.org/externalizable-interface-java/)

## 11.4 Cloneable
For clone an object.

# 12. Multithreading
## 12.1 Thread Class vs Runnable Interface
Threads can be created by using two mechanisms:
1. Extending the Thread class
2. Implementing the Runnable Interface

### 12.1.1 Extending the Thread class
We create a class that extends the java.lang.Thread class. This class **overrides the run()** method available in the Thread class. A thread begins its life inside run() method. We create an object of our new class and **call start()** method to start the execution of a thread. Start() invokes the run() method on the Thread object.
```java
class MultithreadingDemo extends Thread
{
    public void run()
    {
        try
        {
            // Displaying the thread that is running
            System.out.println ("Thread " +
                  Thread.currentThread().getId() +
                  " is running");
 
        }
        catch (Exception e)
        {
            // Throwing an exception
            System.out.println ("Exception is caught");
        }
    }
}
 
// Main Class
public class Multithread
{
    public static void main(String[] args)
    {
        int n = 8; // Number of threads
        for (int i=0; i<8; i++)
        {
            MultithreadingDemo object = new MultithreadingDemo();
            object.start(); //Directly call start
        }
    }
}
```

### 12.1.2 Implementing the Runnable Interface
We create a new class which implements java.lang.Runnable interface and **override run()** method. Then we instantiate a Thread object and **call start()** method on this object.
```java
class MultithreadingDemo implements Runnable
{
    public void run()
    {
        try
        {
            // Displaying the thread that is running
            System.out.println ("Thread " +
                                Thread.currentThread().getId() +
                                " is running");
 
        }
        catch (Exception e)
        {
            // Throwing an exception
            System.out.println ("Exception is caught");
        }
    }
}
 
// Main Class
class Multithread
{
    public static void main(String[] args)
    {
        int n = 8; // Number of threads
        for (int i=0; i<8; i++)
        {
            Thread object = new Thread(new MultithreadingDemo());
            object.start();
        }
    }
}
```

### 12.1.3 Thread Class vs Runnable Interface
1. If we extend the Thread class, our class cannot extend any other class because Java doesn’t support multiple inheritance. But, if we implement the Runnable interface, our class can still extend other base classes.

2. We can achieve basic functionality of a thread by extending Thread class because it provides some inbuilt methods like **yield()** etc. that are **not available in Runnable interface**.

3. If you implement runnable interface, you need to create this class by **wrapping a thread class**. By contrast, you can instantiate a extended class directly.

## 12.2 Life Cycle of A Thread
A thread lies only in one of the shown states at any instant:
* New: The thread has not yet started to run when thread is in this state. It’s code is yet to be run and **hasn’t started to execute**.
* Runnable: either **running or ready to run** just waiting for cpu
* Blocked: Waiting for lock
* Waiting: Thread.join() with no timeout or Object.wait with no timeout
* Timed Waiting: Sleep() or Object.wait with timeout or Thread.join() with timeout
* Terminated: Ended

## 12.3 Main Thread
When a Java program starts up, one thread begins running immediately. This is usually called the **main thread** of our program.

### 12.3.1 Property
1. It is the thread from which other “child” threads will be spawned
2. Often, it must be the last thread to finish execution because it performs various shutdown actions.

### 12.3.2 Controlling Main thread
To control it we must obtain a reference to it. This can be done by calling the method **currentThread()** which is present in Thread class. This method returns a reference to the thread on which it is called. The default priority of Main thread is 5 and for all remaining user threads priority will be inherited from parent to child.
```java
// Java program to control the Main Thread
public class Test extends Thread
{
    public static void main(String[] args)
    {
        // getting reference to Main thread
        Thread t = Thread.currentThread();
         
        // getting name of Main thread
        System.out.println("Current thread: " + t.getName());
         
        // changing the name of Main thread
        t.setName("Geeks");
        System.out.println("After name change: " + t.getName());
         
        // getting priority of Main thread
        System.out.println("Main thread priority: "+ t.getPriority());
         
        // setting priority of Main thread to MAX(10)
        t.setPriority(MAX_PRIORITY);
         
        System.out.println("Main thread new priority: "+ t.getPriority());
         
         
        for (int i = 0; i < 5; i++)
        {
            System.out.println("Main thread");
        }
         
        // Main thread creating a child thread
        ChildThread ct = new ChildThread();
         
        // getting priority of child thread
        // which will be inherited from Main thread
        // as it is created by Main thread
        System.out.println("Child thread priority: "+ ct.getPriority());
         
        // setting priority of Main thread to MIN(1)
        ct.setPriority(MIN_PRIORITY);
         
        System.out.println("Child thread new priority: "+ ct.getPriority());
         
        // starting child thread
        ct.start();
    }
}
 
// Child Thread class
class ChildThread extends Thread
{
    @Override
    public void run() 
    {
        for (int i = 0; i < 5; i++)
        {
            System.out.println("Child thread");
        }
    }
}
/*
Current thread: main
After name change: Geeks
Main thread priority: 5
Main thread new priority: 10
Main thread
Main thread
Main thread
Main thread
Main thread
Child thread priority: 10
Child thread new priority: 1
Child thread
Child thread
Child thread
Child thread
Child thread
*/
```

### 12.3.3 Main Thread and Main Function
For each program, a Main thread is created by JVM(Java Virtual Machine). The “Main” thread first verifies the existence of the main() method, and then it initializes the class. Note that from JDK 6, main() method is mandatory in a standalone java application.


## 12.4 Volatile vs Synchronized
### 12.4.1 Synchronized
Multi-threaded programs may often come to a situation where multiple threads try to **access the same resources** and finally produce erroneous and unforeseen results.

So it needs to be made sure by some synchronization method that **only one thread can access the resource at a time**.

Java provides a way of creating threads and synchronizing their task by using **synchronized blocks**. Synchronized blocks in Java are marked with the synchronized keyword. A synchronized block in Java is **synchronized on some object (either a method (still object) / an object / part of a method (still object))**. All synchronized blocks synchronized on the same object can only have one thread executing inside them at a time. All other threads attempting to enter the synchronized block are blocked until the thread inside the synchronized block exits the block.

```java
import java.io.*;
import java.util.*;
 
// A Class used to send a message
class Sender
{
    public void send(String msg)
    {
        System.out.println("Sending\t"  + msg );
        try
        {
            Thread.sleep(1000);
        }
        catch (Exception e)
        {
            System.out.println("Thread  interrupted.");
        }
        System.out.println("\n" + msg + "Sent");
    }
}
 
// Class for send a message using Threads
class ThreadedSend extends Thread
{
    private String msg;
    private Thread t;
    Sender  sender;
 
    // Recieves a message object and a string
    // message to be sent
    ThreadedSend(String m,  Sender obj)
    {
        msg = m;
        sender = obj;
    }
 
    public void run()
    {
        // Only one thread can send a message
        // at a time.
        synchronized(sender)
        {
            // synchronizing the snd object
            sender.send(msg);
        }
    }
}
// Driver class
class SyncDemo
{
    public static void main(String args[])
    {
        Sender snd = new Sender();
        ThreadedSend S1 =
            new ThreadedSend( " Hi " , snd );
        ThreadedSend S2 =
            new ThreadedSend( " Bye " , snd );
 
        // Start two threads of ThreadedSend type
        S1.start();
        S2.start();
 
        // wait for threads to end
        try
        {
            S1.join();
            S2.join();
        }
        catch(Exception e)
        {
            System.out.println("Interrupted");
        }
    }
}
```
The output is same every-time we run the program.

In the above example, we chose to synchronize the Sender object inside the run() method of the ThreadedSend class. Alternately, we could define the **whole send() method as synchronized** and it would produce the same result. Then we don’t have to synchronize the Message object inside the run() method in ThreadedSend class.
```java
// An alternate implementation to demonstrate
// that we can use synchronized with method also.
class Sender 
{
    public synchronized void send(String msg)
    {
        System.out.println("Sending\t" + msg );
        try
        {
            Thread.sleep(1000);
        } 
        catch (Exception e) 
        {
            System.out.println("Thread interrupted.");
        }
        System.out.println("\n" + msg + "Sent");
    }
}
```

We do not always have to synchronize a whole method. Sometimes it is preferable to synchronize only **part of a method**.
```java
// One more alternate implementation to demonstrate
// that synchronized can be used with only a part of 
// method
class Sender 
{
    public void send(String msg)
    {
        synchronized(this)
        {
            System.out.println("Sending\t" + msg );
            try
            {
                Thread.sleep(1000);
            } 
            catch (Exception e) 
            {
                System.out.println("Thread interrupted.");
            }
            System.out.println("\n" + msg + "Sent");
        }
    }
}
```

### 12.4.2 Volatile Keyword
[Reference](https://www.geeksforgeeks.org/volatile-keyword-in-java/)

Using volatile is yet another way (like synchronized, atomic wrapper) of making class thread safe.

Suppose that two threads are working on SharedObj. If two threads run on different processors each thread may have its own local copy of sharedVariable. If one thread modifies its value the change might not reflect in the original one in the main memory instantly. This depends on the write policy of cache. Now the other thread is not aware of the modified value which leads to data inconsistency. Using volatile keyword here makes sure that the changes made in one thread are immediately reflect in other thread.

```java
class SharedObj
{
   // volatile keyword here makes sure that
   // the changes made in one thread are 
   // immediately reflect in other thread
   static volatile int sharedVar = 6;
}
```

### 12.4.3 Volatile vs Synchronized
Before we move on let’s take a look at two important features of locks and synchronization.
1. Mutual Exclusion: It means that only one thread or process can execute a block of code (critical section) at a time.
2. Visibility: It means that changes made by one thread to shared data are visible to other threads.

Java’s synchronized keyword guarantees both mutual exclusion and visibility. If we make the blocks of threads that modifies the value of shared variable synchronized only one thread can enter the block and changes made by it will be reflected in the main memory.

In some cases we may only desire the visibility and not atomicity. Use of synchronized in such situation is an overkill and may cause scalability problems. Here volatile comes to the rescue. Volatile variables have the visibility features of synchronized but not the atomicity features. The values of volatile variable will never be cached and all writes and reads will be done to and from the main memory. However, **use of volatile is limited to very restricted set of cases as most of the times atomicity is desired**. For example a simple increment statement such as x = x + 1; or x++ seems to be a single operation but is s really a compound read-modify-write sequence of operations that must execute atomically.

## 12.5 Thread Related Methods
### 12.5.1 Single-Thread Methods
[Reference1](https://www.geeksforgeeks.org/java-concurrency-yield-sleep-and-join-methods/) and [Reference2](https://infinitescript.com/2014/09/difference-between-wait-and-sleep-yield-in-java/)

We can prevent the execution of a thread by using one of the following methods of Thread class.

#### 12.5.1.1 yield
yield() method **pauses the currently executing thread temporarily** for giving a chance to the remaining waiting threads of the same priority to execute. If there is no waiting thread or all the waiting threads have a lower priority then the same thread will continue its execution. The yielded thread when it will get the chance for execution is decided by the thread scheduler whose behavior is vendor dependent. 

Use of yield:
Whenever a thread calls java.lang.Thread.yield method, it gives hint to the thread scheduler that it is ready to pause its execution.
```java
// Control passes to child thread
Thread.yield();
```

#### 12.5.1.2 sleep
sleep(): This method causes the currently executing thread to **sleep for the specified number of milliseconds**. Sleep() causes the thread to definitely stop executing for a given amount of time; if no other thread or process needs to be run, the CPU will be idle

```java
Thread.sleep(1000);
```

#### 12.5.1.3 yield vs sleep
* yield indicates that the thread is not doing anything particularly important and if any other threads or processes need to be run, they can. Otherwise, the current thread **will continue to run.**
* causes the thread to definitely stop executing for a given amount of time; if no other thread or process needs to be run, the CPU **will be idle**

#### 12.5.1.4 join
The join() method waits for a thread to die. In other words, it causes the currently running threads to stop executing until the thread it joins with completes its task. For example:
```java
t1.start(); 
t1.join();
//The main thread will wait stop executing and wait for t1 to finish.
```

* If any executing thread t1 calls join() on t2 i.e; t2.join() immediately t1 will enter into waiting state until t2 completes its execution. 
* Giving a timeout within join(), will make the join() effect to be nullified after the specific timeout.

### 12.5.2 Inter-thread Methods
#### 12.5.2.1 Polling
The process of testing a condition repeatedly till it becomes true is known as polling. For example, in a classic queuing problem where one thread is producing data and other is consuming it.

#### 12.5.2.2 Polling in Multithreading  
To avoid polling, Java uses three methods, namely, **wait(), notify() and notifyAll()**.
All these methods belong to object class as final so that all classes have them. They must be used within a **synchronized block** only. When these functions called, the lock is released.

* wait()-It tells the calling thread to **give up the lock** and go to sleep until some other thread enters the same monitor and calls notify(). The current thread must own this object's monitor. The thread releases ownership of this monitor and waits until another thread notifies threads waiting on this object's monitor to wake up either through a call to the notify method or the notifyAll method. The thread then waits until it can re-obtain ownership of the monitor and resumes execution. [Reference](https://www.tutorialspoint.com/java/lang/object_wait.htm)
* notify()-It **wakes up one single thread that called wait()** on the same object. It should be noted that calling notify() does not actually give up a lock on a resource.
* notifyAll()-It wakes up **all the threads that called wait()** on the same object.

```java
import java.util.Scanner;
public class threadexample
{
    public static void main(String[] args)
                           throws InterruptedException
    {
        final PC pc = new PC();
 
        // Create a thread object that calls pc.produce()
        Thread t1 = new Thread(new Runnable()
        {
            @Override
            public void run()
            {
                try
                {
                    pc.produce();
                }
                catch(InterruptedException e)
                {
                    e.printStackTrace();
                }
            }
        });
 
        // Create another thread object that calls
        // pc.consume()
        Thread t2 = new Thread(new Runnable()
        {
            @Override
            public void run()
            {
                try
                {
                    pc.consume();
                }
                catch(InterruptedException e)
                {
                    e.printStackTrace();
                }
            }
        });
 
        // Start both threads
        t1.start();
        t2.start();
 
        // t1 finishes before t2
        t1.join();
        t2.join();
    }
 
    // PC (Produce Consumer) class with produce() and
    // consume() methods.
    public static class PC
    {
        // Prints a string and waits for consume()
        public void produce()throws InterruptedException
        {
            // synchronized block ensures only one thread
            // running at a time.
            synchronized(this)
            {
                System.out.println("producer thread running");
 
                // releases the lock on shared resource
                wait();
 
                // and waits till some other method invokes notify().
                System.out.println("Resumed");
            }
        }
 
        // Sleeps for some time and waits for a key press. After key
        // is pressed, it notifies produce().
        public void consume()throws InterruptedException
        {
            // this makes the produce thread to run first.
            Thread.sleep(1000);
            Scanner s = new Scanner(System.in);
 
            // synchronized block ensures only one thread
            // running at a time.
            synchronized(this)
            {
                System.out.println("Waiting for return key.");
                s.nextLine();
                System.out.println("Return key pressed");
 
                // notifies the produce thread that it
                // can wake up.
                notify();
 
                // Sleep
                Thread.sleep(2000);
            }
        }
    }
}
/*
producer thread running
Waiting for return key.
Return key pressed
Resumed
*/
```
Here is how it works:
* First of all, use of synchronized block ensures that only one thread at a time runs. Also since there is a sleep method just at the beginning of consume loop, the produce thread gets a kickstart.
* When the wait is called in produce method, it does two things. Firstly it releases the lock it holds on PC object. Secondly it makes the produce thread to go on a waiting state until all other threads have terminated, that is it can again acquire a lock on PC object and some other method wakes it up by invoking notify or notifyAll on the same object.
* Therefore we see that as soon as wait is called, the control transfers to consume thread and it prints -“Waiting for return key”.
* After we press the return key, consume method invokes notify(). It also does 2 things- Firstly, unlike wait(), it does not releases the lock on shared resource therefore for getting the desired result, it is advised to use notify only at the end of your method. Secondly, it notifies the waiting threads that now they can wake up but only after the current method terminates.
* As you might have observed that even after notifying, the control does not immediately passes over to the produce thread. The reason for it being that we have called Thread.sleep() after notify(). As we already know that the consume thread is holding a lock on PC object, another thread cannot access it until it has released the lock. Hence only after the consume thread finishes its sleep time and thereafter terminates by itself, the produce thread cannot take back the control.
* After a 2 second pause, the program terminates to its completion.


## 12.6 ReentrantLock
The ReentrantLock class implements the Lock interface and provides synchronization to methods while accessing shared resources. The code which manipulates the shared resource is surrounded by calls to **lock and unlock method**. This gives a lock to the current working thread and blocks all other threads which are trying to take a lock on the shared resource. 

As the name says, **ReentrantLock allow threads to enter into lock on a resource more than once**. When the thread first enters into lock, a hold count is set to one. Before unlocking the thread can re-enter into lock again and every time hold count is incremented by one. For every unlock request, hold count is decremented by one and when hold count is 0, the resource is unlocked.

Reentrant Locks also offer a fairness parameter, by which the lock would abide by the order of the lock request i.e. after a thread unlocks the resource, the lock would go to the thread which has been waiting for the longest time. This fairness mode is set up by passing true to the constructor of the lock.

ReentrantLock Methods:
* lock(): Call to the lock() method increments the hold count by 1 and gives the lock to the thread if the shared resource is initially free.
* unlock(): Call to the unlock() method decrements the hold count by 1. When this count reaches zero, the resource is released.
* tryLock(): If the resource is not held by any other thread, then call to tryLock() returns true and the hold count is incremented by one. If the resource is not free then the method returns false and the thread is not blocked but it exits.
* tryLock(long timeout, TimeUnit unit): As per the method, the thread waits for a certain time period as defined by arguments of the method to acquire the lock on the resource before exiting.
* lockInterruptibly(): This method acquires the lock if the resource is free while allowing for the thread to be interrupted by some other thread while acquiring the resource. It means that if the current thread is waiting for lock but some other thread requests the lock, then the current thread will be interrupted and return immediately without acquiring lock.
* getHoldCount(): This method returns the count of the number of locks held on the resource.
* isHeldByCurrentThread(): This method returns true if the lock on the resource is held by the current thread.

Example:
1. Create an object of ReentrantLock
2. Create a worker(Runnable Object) to execute and pass the lock to the object
3. Use the lock() method to acquire the lock on shared resource
4. After completing work, call unlock() method to release the lock 

```java
// Java code to illustrate Reentrant Locks
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.ReentrantLock;
 
class worker implements Runnable
{
  String name;
  ReentrantLock re;
  public worker(ReentrantLock rl, String n)
  {
    re = rl;
    name = n;
  }
  public void run()
  {
    boolean done = false;
    while (!done)
    {
      //Getting Outer Lock
      boolean ans = re.tryLock();
 
      // Returns True if lock is free
      if(ans)
      {
        try
        {
          Date d = new Date();
          SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss");
          System.out.println("task name - "+ name
                     + " outer lock acquired at "
                     + ft.format(d)
                     + " Doing outer work");
          Thread.sleep(1500);
 
          // Getting Inner Lock
          re.lock();
          try
          {
            d = new Date();
            ft = new SimpleDateFormat("hh:mm:ss");
            System.out.println("task name - "+ name
                       + " inner lock acquired at "
                       + ft.format(d)
                       + " Doing inner work");
            System.out.println("Lock Hold Count - "+ re.getHoldCount());
            Thread.sleep(1500);
          }
          catch(InterruptedException e)
          {
            e.printStackTrace();
          }
          finally
          {
            //Inner lock release
            System.out.println("task name - " + name +
                       " releasing inner lock");
 
            re.unlock();
          }
          System.out.println("Lock Hold Count - " + re.getHoldCount());
          System.out.println("task name - " + name + " work done");
 
          done = true;
        }
        catch(InterruptedException e)
        {
          e.printStackTrace();
        }
        finally
        {
          //Outer lock release
          System.out.println("task name - " + name +
                     " releasing outer lock");
 
          re.unlock();
          System.out.println("Lock Hold Count - " +
                       re.getHoldCount());
        }
      }
      else
      {
        System.out.println("task name - " + name +
                      " waiting for lock");
        try
        {
          Thread.sleep(1000);
        }
        catch(InterruptedException e)
        {
          e.printStackTrace();
        }
      }
    }
  }
}
 
public class test
{
  static final int MAX_T = 2;
  public static void main(String[] args)
  {
    ReentrantLock rel = new ReentrantLock();
    ExecutorService pool = Executors.newFixedThreadPool(MAX_T);
    Runnable w1 = new worker(rel, "Job1");
    Runnable w2 = new worker(rel, "Job2");
    Runnable w3 = new worker(rel, "Job3");
    Runnable w4 = new worker(rel, "Job4");
    pool.execute(w1);
    pool.execute(w2);
    pool.execute(w3);
    pool.execute(w4);
    pool.shutdown();
  }
}

/*
Output:
task name - Job2 waiting for lock
task name - Job1 outer lock acquired at 09:49:42 Doing outer work
task name - Job2 waiting for lock
task name - Job1 inner lock acquired at 09:49:44 Doing inner work
Lock Hold Count - 2
task name - Job2 waiting for lock
task name - Job2 waiting for lock
task name - Job1 releasing inner lock
Lock Hold Count - 1
task name - Job1 work done
task name - Job1 releasing outer lock
Lock Hold Count - 0
task name - Job3 outer lock acquired at 09:49:45 Doing outer work
task name - Job2 waiting for lock
task name - Job3 inner lock acquired at 09:49:47 Doing inner work
Lock Hold Count - 2
task name - Job2 waiting for lock
task name - Job2 waiting for lock
task name - Job3 releasing inner lock
Lock Hold Count - 1
task name - Job3 work done
task name - Job3 releasing outer lock
Lock Hold Count - 0
task name - Job4 outer lock acquired at 09:49:48 Doing outer work
task name - Job2 waiting for lock
task name - Job4 inner lock acquired at 09:49:50 Doing inner work
Lock Hold Count - 2
task name - Job2 waiting for lock
task name - Job2 waiting for lock
task name - Job4 releasing inner lock
Lock Hold Count - 1
task name - Job4 work done
task name - Job4 releasing outer lock
Lock Hold Count - 0
task name - Job2 outer lock acquired at 09:49:52 Doing outer work
task name - Job2 inner lock acquired at 09:49:53 Doing inner work
Lock Hold Count - 2
task name - Job2 releasing inner lock
Lock Hold Count - 1
task name - Job2 work done
task name - Job2 releasing outer lock
Lock Hold Count - 0
*/
```

## 12.7 Daemon thread 
Daemon thread is a low priority thread that runs in background to perform tasks such as garbage collection.
* They can not prevent the JVM from exiting when all the user threads finish their execution.
* JVM terminates itself when all user threads finish their execution
* If JVM finds running daemon thread, it terminates the thread and after that shutdown itself. * JVM does not care whether Daemon thread is running or not.
* It is an utmost low priority thread.

## 12.8 Advanced Multithreading
Semaphore,CyclicBarrier,CountDownLatch,ReadWriteLock,BlockingQueue


# 13. Collections
[Reference](https://www.geeksforgeeks.org/java-collection-tutorial/)

## 13.1 Iterators
Iterators are used in Collection framework in Java to retrieve elements one by one. There are three iterators.
### 13.1.1 Enumeration
Enumeration is a interface used to get elements of legacy collections(Vector, Hashtable).
```java
// Here "v" is an Vector class object. e is of
// type Enumeration interface and refers to "v"
Enumeration e = v.elements();
```

There are two methods in Enumeration interface namely:
```java
// Tests if this enumeration contains more elements
public boolean hasMoreElements();

// Returns the next element of this enumeration 
// It throws NoSuchElementException
// if no more element present
public Object nextElement();
```

**Limitations**:
* for **legacy classes(Vector, Hashtable) only**
* Remove operations can’t be performed
* Only forward direction iterating

### 13.1.2 Iterator
It is a **universal iterator** as we can apply it to any Collection object. By using Iterator, we can perform both read and remove operations. It is improved version of Enumeration with additional functionality of remove-ability of a element.

Iterator must be used whenever we want to enumerate elements in all Collection framework implemented interfaces like Set, List, Queue, Deque and also in all implemented classes of Map interface. Iterator is the **only** cursor available for entire collection framework.

Iterator object can be created by calling iterator() method present in Collection interface.
```java
// Here "c" is any Collection object. itr is of
// type Iterator interface and refers to "c"
Iterator itr = c.iterator();
```

Iterator interface defines three methods:
```java
// Returns true if the iteration has more elements
public boolean hasNext();

// Pop the next one
public Object next();

// Remove the just poped one, can only be called once per next() call.
public void remove();
```

**Limitations**:
* Only forward direction
* No replacement and adding elements

### 13.1.3 ListIterator
It is **only applicable for List collection** implemented classes like arraylist, linkedlist etc. It provides bi-directional iteration.

ListIterator must be used when we want to enumerate elements of List. This cursor has more functionality(methods) than iterator.

ListIterator object can be created by calling listIterator() method present in List interface.
```java
// Here "l" is any List object, ltr is of type
// ListIterator interface and refers to "l"
ListIterator ltr = l.listIterator();
```

ListIterator interface extends Iterator interface. So all three methods of Iterator interface are available for ListIterator. In addition there are six more methods.
```java
// Forward direction

// Returns true if the iteration has more elements
public boolean hasNext();

// same as next() method of Iterator
public Object next();

// Returns the next element index 
// or list size if the list iterator
// is at the end of the list
public int nextIndex();

// Backward direction

// Returns true if the iteration has more elements
// while traversing backward
public boolean hasPrevious();

// Returns the previous element in the iteration
// and can throws NoSuchElementException
// if no more element present
public Object previous();

// Returns the previous element index 
//  or -1 if the list iterator is at the 
// beginning of the list
public int previousIndex();

// Other Methods
 
// same as remove() method of Iterator
public void remove();

// Replaces the last element returned by 
// next() or previous() with the specified element 
public void set(Object obj);

// Inserts the specified element into the list at
// position before the element that would be returned 
// by next(),
public void add(Object obj);
```

Limitations of ListIterator:
* Powerful, but only for lists. Using ListItarator, we can get iterator’s current position. Since ListIterator can access elements in both directions and supports additional operators, ListIterator cannot be applied on Set (e.g., HashSet and TreeSet)

### 13.1.4 Notice
* Initially any iterator reference will point to **the index just before the index of first element** in a collection.
* We **don’t create objects of Enumeration, Iterator, ListIterator** because they are interfaces. We use methods like elements(), iterator(), listIterator() to create objects. These methods have **anonymous Inner classes** that extends respective interfaces and return this class object. 

## 13.2 Collections
The **Collection interface** (java.util.Collection) and **Map interface** (java.util.Map) are two main root interfaces of Java collection classes.

## 13.3 Use Iterator
```java
// Java code to illustrate the use of iterator
class Test {
    public static void main(String[] args)
    {
        ArrayList<String> list = new ArrayList<String>();
 
        list.add("A");
        list.add("B");
        list.add("C");
        list.add("D");
        list.add("E");
 
        // Iterator to traverse the list
        Iterator iterator = list.iterator();
 
        System.out.println("List elements : ");
 
        while (iterator.hasNext())
            System.out.print(iterator.next() + " ");
 
        System.out.println();
    }
}

// ListIterator
class Test {
    public static void main(String[] args)
    {
        ArrayList<String> list = new ArrayList<String>();
 
        list.add("A");
        list.add("B");
        list.add("C");
        list.add("D");
        list.add("E");
 
        // ListIterator to traverse the list
        ListIterator iterator = list.listIterator();
 
        // Traversing the list in forward direction
        System.out.println("Displaying list elements in forward direction : ");
 
        while (iterator.hasNext())
            System.out.print(iterator.next() + " ");
 
        System.out.println();
 
        // Traversing the list in backward direction
        System.out.println("Displaying list elements in backward direction : ");
 
        while (iterator.hasPrevious())
            System.out.print(iterator.previous() + " ");
 
        System.out.println();
    }
}
```

## 13.4 Iterator vs Foreach
* Iterator:
```java
// Iterating over collection 'c' using terator
   for (Iterator i = c.iterator(); i.hasNext(); ) 
       System.out.println(i.next());
```

* For each loop:
```java
// Iterating over collection 'c' using for-each 
   for (Element e: c)
       System.out.println(e);
```

### 13.4.1 Difference:
* In for-each loop, we can’t modify collection it will throw a ConcurrentModificationException on the other hand with iterator we can modify collection.

### 13.4.2 When to Use Which:
* If we have to modify collection, we can use Iterator.
* While using nested for loops it is better to use for-each loop

### 13.4.3 Performance
Traversing a collection using for-each loops or iterators give the same performance.Here, by performance we mean the time complexity of both these traversals.

If you iterate using the old styled C for loop then we might increase the time complexity drastically.

```java
for (i=0;i<n;i++)
   System.out.println(l.get(i));
```

Here if the list l is an ArrayList then we can access it in O(1) time since it is allocated contiguous memory blocks (just like an array) i.e random access is possible. But if the collection is LinkedList, then random access is not possible since it is not allocated contiguous memory blocks, so in order to access a element we will have to traverse the link list till you get to the required index, thus the time taken in worst case to access an element will be O(n).

**Iterator and for-each loop are faster than simple for loop for collections with no random access, while in collections which allows random access there is no performance change with for-each loop/for loop/iterator.**

## 13.5 Retrieving Elements from Collections
There are the 2 ways to retrieve any elements from a collection object
### 13.5.1 For-each
For each loop is meant for traversing items in a collection.
```java
// Iterating over collection 'c' using for-each 
   for (Element e: c)
       System.out.println(e);
```

### 13.5.2 Using Cursors
Cursor is an interface and it is used to retrieve data from collection object,one by one. Cursor has 3 types:
* Iterator Interface: Iterator is an interface provided by collection framework to traverse a collection and for a sequential access of items in the collection.
* ListIterator Interface: It is an interface that contains methods to retrieve the elements from a collection object, both in forward and reverse directions. This iterator is for list based collections.
* EnumerationIterator Interface: The interface is useful to retrieve one by one the element. This iterator is based on data from Enumeration and has methods

## 13.6 Set Interface
Java Set is a part of java.util package and extends **java.util.Collection interface**. It does not allow the use of duplicate elements and at max can accommodate only one null element. Few important features of Java Set interface are as follows:
* The set interface is an unordered collection of objects in which duplicate values cannot be stored.
* The Java Set does not provide control over the position of insertion or deletion of elements.
* Basically, Set is implemented by HashSet, LinkedHashSet or TreeSet
* Set has various methods to add, remove clear, size, etc to enhance the usage of this interface

```java
public class Set_example
{
    public static void main(String[] args)
    {
        // Set demonstration using HashSet
        Set<String> hash_Set = new HashSet<String>();
        hash_Set.add("Geeks");
        hash_Set.add("For");
        hash_Set.add("Geeks");
        hash_Set.add("Example");
        hash_Set.add("Set");
        System.out.print("Set output without the duplicates");
 
        System.out.println(hash_Set);
 
        // Set demonstration using TreeSet
        System.out.print("Sorted Set after passing into TreeSet");
        Set<String> tree_Set = new TreeSet<String>(hash_Set);
        System.out.println(tree_Set);
    }
}
//Set output without the duplicates[Set, Example, Geeks, For]
//Sorted Set after passing into TreeSet[Example, For, Geeks, Set]
```

## 13.7 List Interface
The Java.util.List is a **child interface of Collection**. It is an ordered collection of objects in which duplicate values can be stored. Since List preserves the insertion order, it allows positional access and insertion of elements. List Interface is implemented by **ArrayList, LinkedList**, Vector and Stack classes.

List is an interface, and the instances of List can be created in the following ways:
```java
List a = new ArrayList();
List b = new LinkedList();
List c = new Vector(); 
List d = new Stack(); 
```

Operations on List:
* **Positional Access**: List allows add, remove, get and set operations based on numerical positions of elements in List.
* **Search**: List provides methods to search element and returns its numeric position. (indexOf, lastIndexOf)
* **Iteration**: ListIterator(extends Iterator) is used to iterate over List element. List iterator is bidirectional iterator.
* **Range-view**: List Interface provides a method to get the List view of the portion of given List between two indices. (subList(int fromIndex,int toIndex))

## 13.8 HashSet
The HashSet class implements the Set interface, backed by a hash table which is actually a HashMap instance. No guarantee is made as to the iteration order of the set which means that the class does not guarantee the constant order of elements over time. 

Few important features of HashSet are：
* Implements Set Interface
* Underlying data structure for HashSet is hashtable
* As it implements the Set Interface, duplicate values are not allowed
* Objects that you insert in HashSet are not guaranteed to be inserted in same order
* HashSet also implements Searlizable and Cloneable interfaces

Now for the maintenance of constant time performance, iterating over HashSet requires time proportional to the sum of the HashSet instance’s size (the number of elements) plus the “capacity” of the backing HashMap instance (the number of buckets). Thus, it’s very important **not to set the initial capacity too high (or the load factor too low) if iteration performance is important**.

Initial Capacity: The initial capacity means the number of buckets when hashtable (HashSet internally uses hashtable data structure) is created. The number of buckets will be automatically increased if the current size gets full.

Load Factor: The load factor is a measure of how full the HashSet is allowed to get before its capacity is automatically increased. When the number of entries in the hash table exceeds the product of the load factor and the current capacity, the hash table is rehashed (that is, internal data structures are rebuilt) so that the hash table has approximately twice the number of buckets.

Effect on performance:
Load factor and initial capacity are two main factors that affect the performance of HashSet operations. Load factor of 0.75 provides very effective performance as respect to time and space complexity. If we increase the load factor value more than that then memory overhead will be reduced (because it will decrease internal rebuilding operation) but, it will affect the add and search operation in hashtable. To reduce the rehashing operation we should choose initial capacity wisely. If initial capacity is greater than the maximum number of entries divided by the load factor, no rehash operation will ever occur.

NOTE: The implementation in a HashSet is not synchronized, in the sense that if multiple threads access a hash set concurrently, and at least one of the threads modifies the set, it must be synchronized externally. This is typically accomplished by synchronizing on some object that naturally encapsulates the set. If no such object exists, the set should be “wrapped” using the Collections.synchronizedSet method. This is best done at creation time, to prevent accidental unsynchronized access to the set as shown below:
```java
Set s = Collections.synchronizedSet(new HashSet(...));
```

Constructors in HashSet:
```java
HashSet h = new HashSet(); 
//Default initial capacity is 16 and default load factor is 0.75.
HashSet h = new HashSet(int initialCapacity); 
//default loadFactor of 0.75
HashSet h = new HashSet(int initialCapacity, float loadFactor);
HashSet h = new HashSet(Collection C);
```

Internal working of a HashSet
All the classes of Set interface internally backed up by Map. HashSet uses HashMap for storing its object internally. You must be wondering that to enter a value in HashMap we need a key-value pair, but in HashSet we are passing only one value.

Storage in HashMap
Actually the value we insert in HashSet acts as key to the map Object and for its value java uses a constant variable. So in key-value pair all the keys will have same value.

Implementation of HashSet in java doc:
```java
private transient HashMap map;

// Constructor - 1
// All the constructors are internally creating HashMap Object.
public HashSet()
{
    // Creating internally backing HashMap object
    map = new HashMap();
}

// Constructor - 2
public HashSet(int initialCapacity)
{
    // Creating internally backing HashMap object
    map = new HashMap(initialCapacity);
}

// Dummy value to associate with an Object in Map
private static final Object PRESENT = new Object();
```
If we look at add() method of HashSet class:
```java
public boolean add(E e)
{
   return map.put(e, PRESENT) == null;
}
```
We can notice that, add() method of HashSet class internally calls put() method of backing HashMap object by passing the element you have specified as a key and constant “PRESENT” as its value.

remove() method also works in the same manner. It internally calls remove method of Map interface.
```java
public boolean remove(Object o)
{
  return map.remove(o) == PRESENT;
}
```
Time Complexity of HashSet Operations: The underlying data structure for HashSet is hashtable. So amortize (average or usual case) time complexity for add, remove and look-up (contains method) operation of HashSet takes O(1) time.

Methods in HashSet:
* boolean add(E e): Used to add the specified element if it is not present, if it is present then return false.
* void clear(): Used to remove all the elements from set.
* boolean contains(Object o): Used to return true if an element is present in set.
* boolean remove(Object o): Used to remove the element if it is present in set.
* Iterator iterator(): Used to return an iterator over the element in the set.
* boolean isEmpty(): Used to check whether the set is empty or not. Returns true for empty and false for non-empty condition for set.
* int size(): Used to return the size of the set.
* Object clone(): Used to create a shallow copy of the set.

## 13.9 LinkedList
Linked List are linear data structures where the elements **are not stored in contiguous locations** and every element is a separate object with a data part and address part. The elements are **linked using pointers and addresses**. Each element is known as a node. Due to the dynamicity and **ease of insertions and deletions**, they are preferred over the arrays. It also has few disadvantages like the nodes cannot be accessed directly instead we need to start from the head and follow through the link to reach to a node we wish to access.
To store the elements in a linked list we use a doubly linked list which provides a linear data structure and also used to inherit an abstract class and implement list and deque interfaces.

In Java, LinkedList class **implements the list interface**. The LinkedList class also consists of various constructors and methods like other java collections. 

Constructors for Java LinkedList:
* LinkedList(): Used to create an empty linked list.
* LinkedList(Collection C): Used to create a ordered list which contains all the elements of a specified collection, as returned by the collection’s iterator.

Methods for Java LinkedList:
* int size(): It returns the number of elements in this list.
* void clear(): It removes all of the elements from the list.
* Object clone(): It is used to make the copy of an existing linked list.
* Object set(int index, Object element): It is used to replace an existing element in the list with a new element.
* boolean contains(Object element): It returns true if the element is present in the list.
* boolean add(Object element): It appends the element to the end of the list.
* void add(int index, Object element): It inserts the element at the position ‘index’ in the list.
* void addFirst(Object element): It inserts the element at the beginning of the list.
* Object getFirst(): It returns the first element of the Linked List.
* int lastIndexOf(Object element): If element is found, it returns the index of the last occurrence of the element. Else, it returns -1.
* Object remove(int index): It removes the element at the position ‘index’ in this list. It throws ‘NoSuchElementException’ if the list is empty.

## 13.10 ArrayList
ArrayList is a part of collection framework and is present in java.util package. It provides us dynamic arrays in Java. Though, it may be slower than standard arrays but can be helpful in programs where lots of manipulation in the array is needed.
* ArrayList inherits AbstractList class and **implements List interface**.
* ArrayList is initialized by a size, however the size can increase if collection grows or shrunk if objects are removed from the collection.
* Java ArrayList allows us to randomly access the list.
* ArrayList can not be used for primitive types, like int, char, etc. We need a wrapper class for such cases.
* ArrayList in Java can be seen as similar to vector in C++.

Constructors in Java ArrayList:

* ArrayList(): This constructor is used to build an empty array list
* ArrayList(Collection c): This constructor is used to build an array list initialized with the elements from collection c
* ArrayList(int capacity): This constructor is used to build an array list with initial capacity being specified

Methods in Java ArrayList:

* void clear(): This method is used to remove all the elements from any list.
* void add(int index, Object element): This method is used to insert a specific element at a specific position index in a list.
* int indexOf(Object O): The index the first occurrence of a specific element is either returned, or -1 in case the element is not in the list.
* Object clone(): This method is used to return a shallow copy of an ArrayList.
* Object[] toArray(): This method is used to return an array containing all of the elements in the list in correct order.
* boolean add(Object o): This method is used to append a specificd element to the end of a list.
* Object remove(int index): removes the element at the specified position in this list.

## 13.11 ArrayList vs LinkedList in Java
0. ArrayList:-Implemented with the concept of dynamic array / LinkedList:-Implemented with the concept of doubly linked list.
1. insertions are easy and fast in LinkedList as compared to ArrayList because there is no risk of resizing array and copying content to new array if array gets full which **makes adding into ArrayList of O(n) in worst case, while adding is O(1) operation in LinkedList** in Java. ArrayList also needs to be update its index if you insert something anywhere except at the end of array.
2. Removal also better in LinkedList than ArrayList due to same reasons as insertion.
3. LinkedList has more memory overhead than ArrayList because in ArrayList each index only holds actual object (data) but in case of LinkedList each node holds both data and address of next and previous node.
4. Both LinkedList and ArrayList require O(n) time to find if an element is present or not. However we can do Binary Search on ArrayList if it is sorted and therefore can search in O(Log n) time.

## 13.12 Map Interface
The java.util.Map interface represents a **mapping between a key and a value**. The Map interface is not a subtype of the Collection interface. Therefore it behaves a bit different from the rest of the collection types. 

Few characteristics of the Map Interface are:

* A Map cannot contain duplicate keys and each key can map to at most one value. Some implementations allow null key and null value like the HashMap and LinkedHashMap, but some do not like the TreeMap.
* The order of a map depends on specific implementations, e.g TreeMap and LinkedHashMap have predictable order, while HashMap does not.
* There are two interfaces for implementing Map in java: Map and SortedMap, and three classes: HashMap, TreeMap and LinkedHashMap.

Why and When to use Maps?

Maps are perfect to use for key-value association mapping such as dictionaries. The maps are used to perform lookups by keys or when someone wants to retrieve and update elements by keys. Some examples are:

* A map of error codes and their descriptions.
* A map of zip codes and cities.
* A map of managers and employees. Each manager (key) is associated with a list of employees (value) he manages.
* A map of classes and students. Each class (key) is associated with a list of students (value).

Methods in Map Interface:

* public Object put(Object key, Object value): This method is used to insert an entry in this map.
* public Object remove(Object key): This method is used to delete an entry for the specified key.
* public Object get(Object key):This method is used to return the value for the specified key.
* public boolean containsKey(Object key): This method is used to search the specified key from this map.
* public Set keySet(): This method is used to return the Set view containing all the keys.
* public Set entrySet(): This method is used to return the Set view containing all the keys and values.

## 13.13 HashMap
HashMap is a part of Java’s collection since Java 1.2. It provides the basic implementation of Map interface of Java. It stores the data in (Key, Value) pairs. To access a value one must know its key. HashMap is known as HashMap because it uses a technique called Hashing. Hashing is a technique of converting a large String to small String that represents same String. A shorter value helps in indexing and faster searches. HashSet also uses HashMap internally. It internally uses a link list to store key-value pairs already explained in HashSet in detail and further articles.

Few important features of HashMap are:
* HashMap is a part of java.util package.
* HashMap extends an abstract class AbstractMap. AbstractMap provides an incomplete implementation of Map interface.
* It also **implements Cloneable and Serializable interface**. K and V in the above definition represent Key and Value respectively.
* HashMap doesn’t allow duplicate keys but allows duplicate values. That means A single key can’t contain more than 1 value but more than 1 key can contain a single value.
* HashMap allows null key also but only once and multiple null values.
* This class makes no guarantees as to the order of the map; in particular, it does not guarantee that the order will remain constant over time. It is roughly similar to HashTable but is unsynchronized.

Internal Structure of HashMap:

Internally HashMap contains an array of Node and a node is represented as a class which contains 4 fields:
* int hash
* K key
* V value
* Node next

Performance of HashMap depends on 2 parameters:
* Initial Capacity: As already said, Capacity is simply the number of buckets whereas the Initial Capacity is the capacity of HashMap instance when it is created. The Load Factor is a measure that when rehashing should be done. Rehashing is a process of increasing the capacity. In HashMap capacity is multiplied by 
* Load Factor: Load Factor is also a measure that what fraction of the HashMap is allowed to fill before rehashing. When the number of entries in HashMap increases the product of current capacity and load factor the capacity is increased that is rehashing is done. If the initial capacity is kept higher then rehashing will never be done. But by keeping it higher it increases the time complexity of iteration. So it should be choosed very cleverly to increase the performance. The expected number of values should be taken into account to set initial capacity. Most generally preffered load factor value is 0.75 which provides a good deal between time and space costs. Load factor’s value varies between 0 and 1.

Synchronized HashMap:

As it is told that HashMap is unsynchronized i.e. multiple threads can access it simultaneously. If multiple threads access this class simultaneously and at least one thread manipulates it structurally then it is necessary to make it synchronized externally. It is done by synchronizing some object which enzapsulates the map. If No such object exists then it can be wrapped around Collections.synchronizedMap() to make HashMap synchronized and avoid accidental unsynchronized access. As in following example:
```java
Map m = Collections.synchronizedMap(new HashMap(...));
Now the Map m is synchronized.
```

Constructors in HashMap

HashMap provides 4 constructors and access modifier of each is public:
* HashMap() : It is the default constructor which creates an instance of HashMap with initial capacity 16 and load factor 0.75.
* HashMap(int initial capacity) : It creates a HashMap instance with specified initial capacity and load factor 0.75.
* HashMap(int initial capacity, float loadFactor) : It creates a HashMap instance with specified initial capacity and specified load factor.
* HashMap(Map map) : It creates instance of HashMapwith same mappings as specified map.

Time complexity of HashMap:

HashMap provides constant time complexity for basic operations, get and put, if hash function is properly written and it disperses the elements properly among the buckets. Iteration over HashMap depends on the capacity of HashMap and number of key-value pairs. Basically it is directly proportional to the capacity + size. Capacity is the number of buckets in HashMap. So it is not a good idea to keep high number of buckets in HashMap initially.

Methods in HashMap:
* void clear(): Used to remove all mappings from a map.
* boolean containsKey(Object key): Used to return True if for a specified key, mapping is present in the map.
* Object clone(): It is used to return a shallow copy of the mentioned hash map.
* boolean isEmpty(): Used to check whether the map is empty or not. Returns true if the map is empty.
* Set keySet(): It is used to return a set view of the keys.
* int size(): It is used to return the size of a map.
* Object put(Object key, Object value): It is used to insert a particular mapping of key-value pair into a map.
* Object remove(Object key): It is used to remove the values for any particular key in the Map.

## 13.14 More
See [this] (https://www.geeksforgeeks.org/java-collection-tutorial/).

## Example Questions
#https://www.javatpoint.com/java-collections-interview-questions
#https://www.baeldung.com/java-collections-interview-questions
#https://www.journaldev.com/1330/java-collections-interview-questions-and-answers#compable-comparator
