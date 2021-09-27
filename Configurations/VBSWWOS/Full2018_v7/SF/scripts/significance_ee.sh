#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/workshop/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workDir=$PWD
workspaceDir=workspaces

cd $workDir

echo "mjj (SF: ee)" >> ${workspaceDir}/significance_mjj.txt
combine -M Significance ${workspaceDir}/mjj_ee.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >> ${workspaceDir}/significance_mjj.txt

