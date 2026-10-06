---
layout: default
title: CS-499 ePortfolio
---

<style>
  h2, h3 {
    color: #5b21b6 !important;
  }
</style>

## Introduction
Hello, my name is Marilyn Roy. I am currently completing my Bachelor's in Computer Science. This GitHub Pages account serves as my electronic professional portfolio for my CS-499 capstone class. It highlights my technical growth across my software design, algorithms, and database artifacts.

---

## Education Review
Completing my coursework has allowed me to appreciate the importance of rigorous software engineering practices, secure coding, algorithms, and data structure optimization.

---

## Portfolio Artifacts

---

## Code Review
[Watch Code Review Video](https://youtu.be/wokFh1Ooinc)

---

## Enhancement 1: Software Design and Engineering (Animal Rescue Database & Dashboard Application)
For my first enhancement in the Software Design and Engineering category, I chose the Animal Rescue Database and Dashboard Application I built in CS 340. I coded it in Python using MongoDB, Plotly, and Dash. It hooks straight into an animal shelter database, filters records for things like water or mountain rescue needs, and shows everything on an interactive web dashboard with data tables and maps.

I picked this piece because it proves my skills in software development, database handling, and full-stack app building. The Python CRUD code and the interactive maps do the heavy lifting here. To level it up, I moved the whole app to run locally, added input checks to stop bad data from crashing it, and threw in user login security to lock down database changes.

These upgrades hit the course outcomes I mapped out in Module One right on the mark. Adding input validation proved Outcome 3 by keeping the app stable against bad data. The login security checked off Outcome 5 by building a real security mindset and restricting database access. Other than shifting everything to my local machine, my original plan didn't change at all.

Working through this enhancement taught me a ton about writing reliable code with proper security and authentication. The biggest headache was moving the code and database setup off the lab environment and onto my own computer. Figuring out connection strings and local dependencies forced me to learn how Python talks to MongoDB behind the scenes, and the dashboard is more stable now because of it.

---  
  
## Enhancement 2: Algorithms and Data Structures (Binary Search Tree & Price Range Search)
For my second enhancement, I picked a Binary Search Tree program written in C++ from my CS 300 course. It loads, organizes, sorts, and searches through auction bid data. Instead of running slow linear scans over the whole dataset, it uses custom node structures and tree traversal algorithms to manage and query records fast.

I chose this BST program for my ePortfolio to show off my skills in algorithms and data structures. The original app only handled exact-match ID lookups, which was pretty limiting. To fix that, I built a custom recursive function called searchByPriceRange that safely checks both left and right branches to pull up records matching a specific budget window.

These updates checked off the course outcomes I planned for Module One. Adding the price range search proved Outcome 3 by using recursive logic to solve a real computing problem beyond standard ID lookups. I also added the necessary wrapper methods and declaration fixes to keep the tree stable while traversing it.

Working on this taught me a lot about adding features to existing code without breaking the core structure. Writing recursive search logic gave me a much better grip on data filtering. The biggest hurdle was handling the technical details outside the basic pseudocode, like setting up wrapper methods and fixing declarations. Fixing those bugs proved that building new features takes careful attention to the underlying code, not just the logic.
--- 

## Enhancement 3: Databases 
For my third enhancement, I stayed with the Animal Rescue Database and Dashboard Application from CS 340 to focus on the Databases category. It's built using Python, MongoDB, Plotly, and Dash. The app connects to a shelter database, handles animal records, and displays filtered results through an interactive web dashboard.

I picked this project again because it's a great base for showing off database management and query optimization. In the original version, complex dashboard filters forced MongoDB to run slow, full-collection scans. To fix that bottleneck, I designed and added a custom compound index on the (breed, status) fields using pymongo.ASCENDING. That turned sluggish searches into instant lookups so the app scales smoothly as data grows.

These upgrades hit the course outcomes I aimed for right on target. Adding custom search indexes proved Outcome 3 by building efficient database solutions for real data problems, and Outcome 4 by using professional optimization to keep performance high. Aside from tweaking connection settings for Jupyter and handling module reloads during testing, my original plan didn't change much.

Working on this performance upgrade taught me a lot about how MongoDB handles compound indexing under the hood. The main headaches were parameter mapping mismatches between my CRUD class and Jupyter, plus a few module caching issues during testing. Sorting out those integration hurdles showed me why clean API design and solid testing matter so much when you're updating working code.


---




