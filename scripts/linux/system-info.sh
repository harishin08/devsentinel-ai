#!/bin/bash

echo "========================================"
echo "        DevSentinel AI"
echo "        System Information"
echo "========================================"

echo "Hostname       : $(hostname)"
echo "User           : $(whoami)"
echo "Operating System: $(uname -s)"
echo "Kernel         : $(uname -r)"
echo "Architecture   : $(uname -m)"
echo "Uptime         : $(uptime -p)"

echo ""
echo "------------- Memory -------------------"
free -h

echo ""
echo "------------- Disk ---------------------"
df -h /

echo "========================================"
