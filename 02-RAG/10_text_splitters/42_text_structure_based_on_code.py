from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
import streamlit as st
st.title("Text Structure Based Text Splitter on Code")

text = '''
This is a clean, professional **README.md** template designed to document a single class across multiple programming languages. It uses standard Markdown features like tables, task lists, and syntax-highlighted code blocks.

---

# Project: Person Class Implementation

A multi-language demonstration of a basic `Person` class, covering object-oriented concepts in Java, Fortran, and Lua.

## 📋 Overview

The goal of this project is to implement a standard `Person` entity that stores basic data and provides a simple interaction method.

### Class Blueprint

| Attribute | Type | Description |
| --- | --- | --- |
| `name` | String | The individual's full name. |
| `age` | Integer | The age in years. |

### Methods

* `introduce()`: Prints a greeting string to the console.

---

## 💻 Implementations

### 1. Java

The Java version uses a standard class with a constructor and a main method.

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void introduce() {
        System.out.println("Hi, I'm " + name);
    }
}

```

### 2. Fortran

Uses a `module` and `derived type` to simulate a class structure.

```fortran
type :: Person
    character(len=20) :: name
    integer :: age
contains
    procedure :: introduce
end type Person

```

### 3. Lua

Utilizes `tables` and `metatables` for prototype-based OOP.

```lua
function Person:new(name, age)
    local instance = setmetatable({}, self)
    instance.name = name
    instance.age = age
    return instance
end

```

---

## 🛠️ Status & Tasks

* [x] Implement Java Class
* [x] Implement Fortran Module
* [x] Implement Lua Table
* [ ] Add Python version
* [ ] Write Unit Tests

> **Note:** This project is for educational purposes to compare syntax across paradigms.

---

**Would you like me to fill in the Python or C++ versions to complete the list?**
'''

text_splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=500, chunk_overlap=0, language=Language.MARKDOWN
)

chunks = text_splitter.split_text(text)

st.subheader("Chunks Length")

st.write(len(chunks))

for i, chunk in enumerate(chunks):

    st.subheader(f"Chunk {i+1}")

    st.write(chunk)