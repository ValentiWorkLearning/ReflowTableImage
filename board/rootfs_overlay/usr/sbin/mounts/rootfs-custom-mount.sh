#!/bin/bash
echo "Mount rootfs paths"
APPLICATION_DIRECTORY="/opt/appl/oven"

if [[ ! -d "$APPLICATION_DIRECTORY" ]]
then
    mkdir -p "$APPLICATION_DIRECTORY"
    mount /dev/disk/by-partlabel/application "$APPLICATION_DIRECTORY"
fi

echo "Mount rootfs directories is done"
