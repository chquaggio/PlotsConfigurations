#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
#workDir=/afs/cern.ch/user/m/mlizzo/work/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/nAODv6_v6 
workDir=/afs/cern.ch/user/c/cquaggio/private/PlotsConfigurations/Configurations/VBSWWOS/EFT2018_v7/SF

datacardDir=OSWWEFT_2018_SF_15ops
combinedcardsDir=combined_ee_mm
workspaceDir=workspace

cd $workDir
mkdir -p ${workDir}/${datacardDir}/${combinedcardsDir}

vars="detajj eta_1j eta_1l eta_2j eta_2l mjj mll pt_1j pt_1l pt_2j pt_2l ptll PuppiMET_pt Zepp_1l Zepp_2l"

for var in $vars
do
    mkdir -p ${workDir}/${datacardDir}/${combinedcardsDir}/${var}
    combineCards.py   vbs_ee_lowZ=${workDir}/${datacardDir}/VBS_2j_ee_lowZ/${var}/datacard.txt \
                    vbs_mm_lowZ=${workDir}/${datacardDir}/VBS_2j_mm_lowZ/${var}/datacard.txt \
                    vbs_ee_highZ=${workDir}/${datacardDir}/VBS_2j_ee_highZ/${var}/datacard.txt \
                    vbs_mm_highZ=${workDir}/${datacardDir}/VBS_2j_mm_highZ/${var}/datacard.txt \
                    top_ee=${workDir}/${datacardDir}/top_2j_ee/events/datacard.txt \
                    top_mm=${workDir}/${datacardDir}/top_2j_mm/events/datacard.txt \
                    dy_ee=${workDir}/${datacardDir}/DY_2j_ee/events/datacard.txt \
                    dy_mm=${workDir}/${datacardDir}/DY_2j_mm/events/datacard.txt \
                    > ${workDir}/${datacardDir}/${combinedcardsDir}/${var}/datacard.txt


    echo "nuisance edit drop VgS_L top_ee CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee PS_FSR" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee PS_ISR" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee QCDscale_VV" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    echo "nuisance edit drop VgS_L dy_mm QCDscale_VV" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # text2workspace.py  ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt  -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o combined.root --X-allow-no-signal --PO eftOperators=cqq31
done
