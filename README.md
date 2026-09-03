# Grokking Algorithms: Code & Notes

I'm working my way through *Grokking Algorithms* by Aditya Y. Bhargava. This repo is basically my digital notebook, a place where I'm translating the book's concepts into Python, solving the chapter exercises, and getting hands-on practice with data structures and time complexity.

It's just me reading, learning, and writing code to make sure these concepts actually stick.

## 📚 What's Done So Far

| Chapter | Topic | What I Practiced |
| --- | --- | --- |
| **01** | Intro to Algorithms | Binary Search, figuring out Big O notation, Logarithmic Time |
| **02** | Selection Sort | Arrays vs. Linked Lists, Memory basics, O(n^2) Sorting |
| **03** | Recursion | The Call Stack, Base vs. Recursive Cases, avoiding Stack-Overflows |
| **04** | Quicksort | Divide & Conquer, Inductive Proofs, Pivot mechanics |
| **05** | Hash Tables | O(1) Lookups, Collisions, Load Factors |

## 🗺️ What's Next

I've finished the first half of the book (up to Chapter 5). I plan to tackle the rest over the next couple of weeks. Here is what's on deck:

* **Chapter 06:** Breadth-First Search & Graphs
* **Chapter 07:** Dijkstra's Algorithm
* **Chapter 08:** Greedy Algorithms & NP-Complete problems
* **Chapter 09:** Dynamic Programming
* **Chapter 10:** K-Nearest Neighbors (KNN)
* **Chapter 11:** Where to Go Next

## 💻 What's Inside

I'm trying to keep the code clean and practical.

* **One exercise file per chapter:** You'll find my answers all condensed into a single `exercises.py` file per chapter to keep things tidy.
* **Notes in the code:** I use multi-line comments in the Python files to explain my logic or write down the theoretical answers.
* **Optimizing as I go:** I'm trying to write efficient Python-like tracking pointers instead of slicing arrays during recursive searches to actually maintain the correct Big O time complexity.

## 🚀 Running the Code

Just standard Python 3. Navigate to whatever chapter you want and run the scripts:

```bash
cd chapter_4
python quick_sort.py
python exercises.py

```