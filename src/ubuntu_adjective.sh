#!/bin/bash

Help()
{
   echo "Return the adjective for the corresponding Ubuntu distro."
   echo
   echo "Syntax: ubuntu_adjective --ubuntu=[VERSION]"
   echo "options:"
   echo "-u, --ubuntu   Ubuntu version to use for the base image, e.g. 21.04"
   echo
}

for i in "$@"; do
  case $i in
    -h|--help)
      Help
      exit;;
    -u=*|--ubuntu=*)
      UBUNTU_VERSION="${i#*=}";;
    *)
      echo "Error: Invalid option"
      exit;;
  esac
done


# This is used to tag the image with the proper name.
case $UBUNTU_VERSION in
  20.04)
    UBUNTU_ADJECTIVE="focal";;
  20.10)
    UBUNTU_ADJECTIVE="groovy";;
  21.04)
    UBUNTU_ADJECTIVE="hirsute";;
  21.10)
    UBUNTU_ADJECTIVE="impish";;
  22.04)
    UBUNTU_ADJECTIVE="jammy";;
  22.10)
    UBUNTU_ADJECTIVE="kinetic";;
  23.04)
    UBUNTU_ADJECTIVE="lunar";;
  23.10)
    UBUNTU_ADJECTIVE="mantic";;
  24.04)
    UBUNTU_ADJECTIVE="noble";;
  24.10)
    UBUNTU_ADJECTIVE="oracular";;
  25.04)
    UBUNTU_ADJECTIVE="plucky";;
  \?)
    echo "Error: Invalid option for ubuntu version"
    exit;;
esac

echo ${UBUNTU_ADJECTIVE}
