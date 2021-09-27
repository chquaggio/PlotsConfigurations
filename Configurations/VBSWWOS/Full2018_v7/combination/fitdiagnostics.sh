#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/workshop/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workDir=$PWD
combinedcardsDir=VBSWWOS_18_comb

cd $workDir

echo "mjj (combination)" >> ${workDir}/${combinedcardsDir}/diagnostics_mjj.txt
combine -M FitDiagnostics ${workDir}/${combinedcardsDir}/mjj.root -t -1 --setParameters r_vbs=1 --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workDir}/${combinedcardsDir}/diagnostics_mjj.txt
