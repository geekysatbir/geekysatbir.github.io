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
COMMIT_MESSAGE="site update"
echo "📝 Committing changes with message: '$COMMIT_MESSAGE'..."
# Use '|| true' to prevent the script from failing if there are no changes to commit
# after the initial check (e.g., only whitespace changes git might ignore).
git commit -m "$COMMIT_MESSAGE" || true

# 3. Push the changes, forcing a credential prompt
echo "⬆️  Pushing changes to the 'master' branch on GitHub..."
echo "💡 Disabling credential helper to force a login prompt."
echo "💡 When prompted, use the username 'geekysatbir' and a Personal Access Token as the password."

# The '-c credential.helper=' part temporarily overrides the configuration
# for this single command, forcing Git to ask for credentials.
git -c credential.helper= push origin master

echo "✅ Website update complete and pushed to GitHub!"