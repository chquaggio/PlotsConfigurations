#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/workshop/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workDir=$PWD 
combinedcardsDir=VBSWWOS_18_comb

cd $workDir

echo "mjj (combination)" >> ${workDir}/${combinedcardsDir}/significance_mjj.txt
combine -M Significance ${workDir}/${combinedcardsDir}/mjj.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >> ${workDir}/${combinedcardsDir}/significance_mjj.txt

