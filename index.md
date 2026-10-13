---
layout: default
title: CS-499 Final Capstone Project ePortfolio
---

<style>
  h2, h3 {
    color: #5b21b6 !important;
  }
  .page-header * {
    color: #ffffff !important;
    opacity: 1 !important;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.6);
  }
  .page-header .project-tagline, .page-header p, .page-header h2 {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
  }
</style>

## Self-Assessment

Completing my computer science degree over the past three years while battling stage 3C breast cancer has been a journey of resilience, focus, and determination. Pushing through these challenges to reach graduation has strengthened my passion for the field and shaped my ultimate professional goal of becoming a technical project manager. Throughout the program, I worked on projects that pushed me past basic coding and prepared me to lead software builds. I learned how to collaborate in group settings by managing shared code and tracking project tasks. I also learned how to communicate clearly with stakeholders, ensuring that technical choices, timelines, and project requirements are understood by both developers and management.

My coursework built a strong technical foundation that directly supports my career plans. Throughout the program, three of the most important concepts I learned were writing clean and maintainable code, organizing databases so they perform efficiently, and protecting software from common security threats. When studying data structures and algorithms, I learned to analyze efficiency and pick the right tools to solve performance problems. In software engineering and database classes, I learned how to design scalable systems from scratch and optimize data flow. I also focused heavily on security, learning how to spot potential vulnerabilities early and build defensive measures like input validation and user authentication right into the system architecture.

Through these experiences and artifact enhancements, I successfully met all five course outcomes for the program. I built collaborative environments that support organizational decision-making, delivered professional communications tailored to specific audiences, and designed computing solutions using proper algorithmic principles and industry standards. I also demonstrated the use of innovative tools to deliver business value and cultivated a proactive security mindset to protect data and resources.

The artifacts in this portfolio tie these skills together and show my full range as a technical professional. They prove I can evaluate existing systems, spot operational limits, and guide technical projects from start to finish. The first artifact highlights my software design skills by turning a shelter dashboard into a secure, locally hosted app with login protection. The second artifact showcases my algorithmic abilities through a custom price range search function added to a binary search tree. The third artifact demonstrates my database expertise by optimizing MongoDB queries with compound indexing to stop performance slowdowns. Together, these pieces introduce my background and set up the work that follows.

---

## Code Review

Code reviews are extremely important for quality assurance. They bring a fresh perspective to catch blind spots and bugs. Taking a second look at your work or someone else's work acts as a safety net that keeps your software reliable, ensures your logic makes sense to others, and helps everyone write cleaner, more maintainable code.

[Watch My Code Review Here](https://youtu.be/wokFh1Ooinc)

---

## Portfolio Artifacts

### Enhancement 1: Software Design and Engineering (Animal Rescue Database and Dashboard Application)

For the artifact 1 enhancement, which falls under the Software Design and Engineering category, I chose the Animal Rescue Database and Dashboard Application that I originally built in CS 340 (Client/Server Development). I developed this application using Python, MongoDB, Plotly, and Dash. It connects directly to an animal shelter database, filters records based on specific criteria like water or mountain rescue needs, and presents everything through an interactive web-based dashboard featuring data tables and maps.

I selected this artifact for my ePortfolio because it is a strong example of my skills in software development, database work, and building functional applications. The specific parts that showcase my abilities are the Python CRUD code and the interactive dashboard with maps and data tables. To improve the project, I moved it to run locally on my computer, added input checks to stop bad data from causing crashes, and added user login security to protect changes made to the database.

I successfully met the course outcomes I planned to target with this enhancement. By adding the login security checks and input validation to my animal rescue database, I demonstrated Outcome 3 by writing code that keeps the application from crashing when bad data is entered. It also fulfilled Outcome 5 by building a security mindset and making sure only the right people can access and change database records. Aside from shifting it to a local setup, everything else stayed right on track with my original proposal.

While enhancing and modifying this artifact, I learned a lot about how to properly implement security features like user authentication and input validation to make an application much more reliable. One of the biggest challenges I faced was dealing with environment and setup differences, specifically having to shift my code and database configuration to run locally on my machine instead of using the original lab environment. Working through that forced me to really understand how connection strings and dependencies talk to MongoDB behind the scenes, which ultimately made the dashboard much more stable once I got it all set up and working with the help of my instructor.

[View Enhancement One Source Code](https://github.com/Marilyn782/CS-499_eportfolio/tree/main/Enhancement%20One)

---  
  
> ### Enhancement 2: Algorithms and Data Structures
> Binary Search Tree & Price Range Search

For the artifact 2 enhancement, I chose the Binary Search Tree program written in C++ that loads, organizes, sorts, and searches through auction bid data efficiently. It was originally created during my CS 300 course. The program utilizes node structures and custom tree traversal algorithms to manage and query records rapidly without needing to perform linear scans over the entire dataset.

I selected this Binary Search Tree (BST) program from CS 300 for my ePortfolio to showcase my skills in algorithms and data structures through custom node architectures, recursive insertion methods, and logarithmic search efficiency. While the original application effectively handled exact-match ID lookups, it lacked the flexibility to search across an open-ended price range. To improve the artifact, I engineered and integrated a custom recursive function called searchByPriceRange that safely traverses both left and right branches to extract records matching a user-defined budget window, demonstrating my ability to critically evaluate and enhance existing software without compromising structural integrity.

Yes, I successfully met the course outcomes I planned to pursue in Module One. By designing and integrating the price range search feature into my binary search tree, I demonstrated proficiency in Course Outcome 3 by applying recursive algorithmic principles to create an efficient computing solution that filters data beyond standard ID lookups. I successfully executed this plan by implementing the search function, as well as, a few updates that included the necessary wrapper methods and declaration fixes to ensure the tree was safely traversed without breaking its structural integrity.

Working on this enhancement taught me a lot about how to add new features to an existing codebase without messing up the original data structure. I got a much better handle on how to write recursive search logic to filter data instead of just doing standard ID lookups. The main challenge was dealing with the technical details outside of the basic pseudocode, like setting up the wrapper methods and fixing declarations so the tree could be traversed safely. Working through those bugs showed me that adding a new feature takes a lot of care with the underlying code structure, not just the logic itself.

[View Enhancement Two Source Code](https://github.com/Marilyn782/CS-499_eportfolio/tree/main/Enhancement%20Two)

--- 

### Enhancement 3: Databases (Animal Rescue Database and Dashboard Application)
For the Artifact 3 enhancement, which falls under the Databases category, I continued working with the Animal Rescue Database and Dashboard Application that I originally built in CS 340. Developed using Python, MongoDB, Plotly, and Dash, the application connects to a shelter database, manages animal records, and displays filtered results through an interactive web dashboard.

I selected this project for my ePortfolio again because it serves as an excellent foundation for demonstrating database management and query optimization. The components that highlight my abilities include the custom Python CRUD operations and the data retrieval logic connecting to the web dashboard. To improve this artifact for Artifact 3, I addressed a major performance bottleneck: in the original implementation, complex multi-field dashboard filters forced MongoDB to perform slow, full-collection scans. To solve this, I designed and integrated a custom compound index on the (breed, status) fields using pymongo.ASCENDING, transforming sequential searches into instant lookups to ensure the application scales smoothly as data grows.

Yes, I successfully met my planned course goals. By adding custom search indexes, I showed that I can design efficient database solutions to solve real-world data retrieval issues (aligning with Course Outcome 3) and use professional optimization techniques to keep software fast and reliable (aligning with Course Outcome 4). As for updates to my original plan: while I successfully reached my main performance goal, the actual coding required a few small adjustments. Specifically, I updated how connection settings were passed into the code setup so it worked smoothly with the Jupyter notebook, and I managed module reloading during testing to make sure the live environment ran my latest updates correctly.

While working on this performance enhancement, I gained a much deeper understanding of how MongoDB handles compound indexing under the hood to accelerate complex queries on large datasets. One of the primary challenges I faced was resolving parameter mapping mismatches between the enhanced CRUD class initialization and the Jupyter notebook environment, along with managing module caching issues during testing. Working through those integration hurdles taught me how important clean API design and rigorous testing are when updating an existing, working codebase without breaking its core functionality.

[View Enhancement Three Source Code](https://github.com/Marilyn782/CS-499_eportfolio/tree/main/Enhancement%20Three)

---




