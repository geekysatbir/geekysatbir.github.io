#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "🚀 Starting website update process..."

# Check if there are any changes to commit
if [ -z "$(git status --porcelain)" ]; then
  echo "✅ No changes to commit. Working directory is clean."
  echo "✅ Nothing to push. Exiting."
  exit 0
fi

# 1. Stage all changes
echo "➡️  Staging all changes..."
git add .

# 2. Commit the changes with a default message
# You can change the commit message here if you like.
COMMIT_MESSAGE="site update"
echo "📝 Committing changes with message: '$COMMIT_MESSAGE'..."
git commit -m "$COMMIT_MESSAGE"

# 3. Push the changes to the 'main' branch on GitHub
# If your branch is named 'master', change 'main' to 'master' below.
echo "⬆️  Pushing changes to the 'main' branch on GitHub..."
git push origin main

echo "✅ Website update complete and pushed to GitHub!"
