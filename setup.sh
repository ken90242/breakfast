#!/bin/sh

# Install sqlite3
echo -n "Installing sqlite3..."

echo "Done"

# Ensure sqlite3 is callable under global environment

# Schedule task for generating report
echo -n "Scheduling tasks..."
GENERATE_REPORT_CMD="sh ${PWD}/report.sh"
crontab -l | { cat; echo "1 * * * * ${GENERATE_REPORT_CMD}"; } | crontab -
echo "Done"

# Install Docker
echo -n "Installing Docker..."

echo "Done"

# Start API server (Django)
echo -n "Starting API server..."

echo "Done"

# Display
echo "Now, please open index.html."

