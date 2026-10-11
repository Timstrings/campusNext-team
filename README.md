# CampusFlow

## Project Overview

CampusFlow is a Python command-line application
for managing campus support tickets.

The system allows users to create, view, assign,
and track support tickets.

## Team Members

- Engineer A: Bashir Hassan
- Engineer B: Timothy Yusuf

## Features

### Engineer A - Ticket Management

Implemented features:

- Create support tickets
- Validate ticket information
- Calculate ticket priority
- Generate unique ticket IDs
- List all tickets
- View tickets by ID

### Engineer B - Workflow Management

Features under development:

- Assign tickets to team members
- Update ticket status
- Manage ticket work queues
- Generate ticket reports
- Save and load ticket data

## Ticket Information

Each ticket contains:

- ID
- Title
- Category
- Urgency
- Affected users
- Priority
- Status
- Assigned team member

## Priority Levels

CampusFlow supports four priority levels:

- Critical
- High
- Medium
- Low

Priority is calculated using ticket urgency
and the number of affected users.

## Technologies

- Python 3
- Git
- GitHub
- unittest

## Running Tests

Run the automated tests using:

python3 -m unittest discover -s tests -v

## Development Workflow

The team uses:

- GitHub Issues for task tracking
- Feature branches for development
- Pull Requests for code review
- Unit tests for verification