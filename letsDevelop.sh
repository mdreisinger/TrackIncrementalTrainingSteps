#!/bin/bash
PROJECT="TrackIncrementalTrainingSteps"

if [ $# -lt 1];
then
    printf "Usage: $0 <operation> <options>\n"
    printf "Operations:\n"
    printf "\tactivate <-f to force recreation of venv>\n"
    printf "\tdeactivate\n"
    printf "\ttest <optional test file name>\n"
    printf "\tpylint\n"
    printf "\tclean\n"
    printf "\trun\n"
    printf "NOTE: To use the activate & deactivate operations this script must be called like so:\n"
    printf "\t. ./letsDevelop.sh\n\n"
    exit
fi

