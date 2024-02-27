#!/bin/bash

COMMIT_MESSAGE="Initial commit"

# Add color_recognition.py to the staging area
git add color_recognition.py

# Commit changes
git commit -m "$COMMIT_MESSAGE"

# Push to the repository
git push origin master  # Replace "master" with your branch name if needed
