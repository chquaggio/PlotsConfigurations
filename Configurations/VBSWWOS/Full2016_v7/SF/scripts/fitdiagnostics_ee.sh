#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/m/mlizzo/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workDir=$PWD
workspaceDir=workspaces/AN_config

cd $workDir

echo "mjj (SF: ee)" >> ${workspaceDir}/diagnostics_ee_mjj.txt
combine -M FitDiagnostics ${workspaceDir}/mjj_ee.root -t -1 --setParameters r_vbs=1 --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/diagnostics_ee_mjj.txt
