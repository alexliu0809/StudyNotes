# References
* https://www.geeksforgeeks.org/compilation-execution-java-program/
* http://crackingjavainterviews.blogspot.com/2013/04/what-are-four-principles-of-oop.html
* https://blog.csdn.net/jackfrued/article/details/44921941

# Table of Contents
- [1. How Java Compiles](#1-how-java-compiles)
- [2. OOP Concepts](#2-oop-concepts)
  * [2.1 Definition](#21-definition)
  * [2.2 Four Basic Concepts](#22-four-basic-concepts)
- [3. Objects](#3-objects)
  * [3.1 Storage of Objects](#31-storage-of-objects)
  * [3.2 Primitive Types](#32-primitive-types)
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
  * [7.1 Composition](#71-composition)
  * [7.2 Inheitance](#72-inheitance)
  * [7.2.1 Initialize base class](#721-initialize-base-class)
  * [7.2.2 Name Hiding](#722-name-hiding)
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
- [11. Serialization and Deserialization](#11-serialization-and-deserialization)
  * [11.1 Use Serialization](#111-use-serialization)
  * [11.2 Why Serialization](#112-why-serialization)
  * [11.3 Externalizable](#113-externalizable)
  * [11.4 Cloneable](#114-cloneable)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# 1. How Java Compiles
* Javac.exe compiles source file (.java) into byte code files (.class). Pass this file to JVM
* There are three stages executed in JVM:
    * Load main class 
    * Bytecode Verifier (initialize, type checking)
    * Just-In-Time Compiler (JIT) translates code into machine code
    
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

## 7.1 Composition
One class contain another class directly. It represents part-of relationship. In composition, both the entities are dependent on each other. Example:
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

## 7.2.1 Initialize base class
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

## 7.2.2 Name Hiding
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


## TODO
SQL + THREADING + List/Set/Map
