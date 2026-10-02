# Personal Portfolio - Quiz 5 and 6

A Django-based personal portfolio application with a public portfolio and a protected dashboard for project and tech stack management.

## Features

### Public Portfolio

- View all projects
- View individual project details
- View project descriptions
- View technologies used for each project
- Open project source/live links
- View personal information
- Submit inquiries
- View and submit testimonies

### Admin / Superuser Dashboard

The dashboard can only be accessed by an authenticated Django superuser.

Features include:

- Dedicated superuser-only sign-in page
- Dashboard located at `/dashboard/`
- List of all projects
- List of all tech stacks
- Create new projects
- Create new tech stacks
- Automatic update of the public portfolio when a project is added
- Logout functionality

## Project Model

Projects contain:

- Project Name
- Description
- Tech Stack
- Link
- Date Created

Projects and tech stacks use a many-to-many relationship.

This allows one tech stack, such as Python, to be associated with multiple projects without creating duplicate TechStack objects.

## TechStack Model

Tech stacks contain:

- Name
- Date Added

A tech stack can be associated with multiple projects.

---

# Requirements

Before running the project, make sure the following are installed:

- Python 3
- pip
- Git

---

# Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Robjune/My_Portfolio.git