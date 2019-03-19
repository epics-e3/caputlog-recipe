#!/bin/bash
#
#  Copyright (c) 2018 - Present  Jeong Han Lee
#  Copyright (c) 2018 - Present  European Spallation Source ERIC
#
#  The program is free software: you can redistribute
#  it and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 2 of the
#  License, or any newer version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program. If not, see https://www.gnu.org/licenses/gpl-2.0.txt
#
#
#   author  : Jeong Han Lee
#   email   : jeonghan.lee@gmail.com
#   date    : Tuesday, June 12 17:16:35 CEST 2018
#   version : 


function print_ca_addr
{
    printf ">> Print ... \n"
    echo "EPICS_CA_ADDR_LIST      : $EPICS_CA_ADDR_LIST"
    echo "EPICS_CA_AUTO_ADDR_LIST : $EPICS_CA_AUTO_ADDR_LIST"
}


function unset_ca_addr
{
    printf ">> Unset ... EPICS_CA_ADDR_LIST and EPICS_CA_AUTO_ADDR_LIST\n"
    unset EPICS_CA_ADDR_LIST
    unset EPICS_CA_AUTO_ADDR_LIST
}

function set_ca_addr
{
    printf "Set ... EPICS_CA_ADDR_LIST and EPICS_CA_AUTO_ADDR_LIST \n";
    export EPICS_CA_ADDR_LIST="$1"
    export EPICS_CA_AUTO_ADDR_LIST="$2";
    print_ca_addr
}



_HOST_IP="$(ip -4 route get 8.8.8.8 | awk {'print $7'} | tr -d '\n')";


unset_ca_addr

set_ca_addr "$_HOST_IP" "YES"

PAUSE=5

#sleep 5000

while true; do

    ps aux |grep  caPutLog.cmd |grep -v grep| grep -v emacs
    for i in `seq 1 100`;
    do
	printf ">>>  "
	date '+%Y-%m-%d %H:%M:%S' 
	echo "------------------------------------------"
	caput SEC-SUB01:DIS-DEV-01-md:a $i
	sleep ${PAUSE}
	echo ""
    done
    for i in `seq 100 1`;
    do
	printf ">>>  "
	date '+%Y-%m-%d %H:%M:%S' 
	echo "------------------------------------------"
	caput SEC-SUB01:DIS-DEV-01-md:a $i
	sleep ${PAUSE}
	echo ""
    done    
done  
