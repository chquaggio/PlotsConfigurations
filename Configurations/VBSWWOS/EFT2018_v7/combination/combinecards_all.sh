#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
#workDir=/afs/cern.ch/user/m/mlizzo/work/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/nAODv6_v6 
workDir=/afs/cern.ch/user/c/cquaggio/private/PlotsConfigurations/Configurations/VBSWWOS/EFT2018_v7

dfDir=DF/OSWWEFT_2018_DF_15ops
sfDir=SF/OSWWEFT_2018_SF_15ops

combinedcardsDir=combined_all

cd $workDir
mkdir -p ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}

vars="detajj eta_1j eta_1l eta_2j eta_2l mjj mll pt_1j pt_1l pt_2j pt_2l ptll PuppiMET_pt Zepp_1l Zepp_2l"

for var in $vars
do
    mkdir -p ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}
    combineCards.py   vbs_ee_lowZ=${workDir}/${sfDir}/VBS_2j_ee_lowZ/${var}/datacard.txt \
                    vbs_mm_lowZ=${workDir}/${sfDir}/VBS_2j_mm_lowZ/${var}/datacard.txt \
                    vbs_ee_highZ=${workDir}/${sfDir}/VBS_2j_ee_highZ/${var}/datacard.txt \
                    vbs_mm_highZ=${workDir}/${sfDir}/VBS_2j_mm_highZ/${var}/datacard.txt \
                    top_ee=${workDir}/${sfDir}/top_2j_ee/events/datacard.txt \
                    top_mm=${workDir}/${sfDir}/top_2j_mm/events/datacard.txt \
                    dy_ee=${workDir}/${sfDir}/DY_2j_ee/events/datacard.txt \
                    dy_mm=${workDir}/${sfDir}/DY_2j_mm/events/datacard.txt \
                    vbs_em_me_lowZ=${workDir}/${dfDir}/VBS_2j_em_me_lowZ/${var}/datacard.txt \
                    vbs_em_me_highZ=${workDir}/${dfDir}/VBS_2j_em_me_highZ/${var}/datacard.txt \
                    top_em_me=${workDir}/${dfDir}/top_2j_em_me/events/datacard.txt \
                    dy_em_me=${workDir}/${dfDir}/dycr_2j_em_me/events/datacard.txt \
                    > ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt


    echo "nuisance edit drop VgS_L top_ee CMS_PUID_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_PUID_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr1" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr2" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hf" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats1_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats2_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_jes" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lf" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats1_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats2_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_e_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_hwwtrigger_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee CMS_eff_m_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee PS_FSR" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee PS_ISR" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop VgS_L top_ee QCDscale_VV" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt

    echo "nuisance edit drop VgS_L dy_mm QCDscale_VV" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt

    echo "nuisance edit drop Fake_e vbs_em_me_highZ CMS_fake_e_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_em_me_highZ CMS_fake_m_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_em_me_highZ CMS_fake_stat_m_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_em_me_highZ CMS_fake_stat_e_2018" >> ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt
    # text2workspace.py  ${workDir}/OSWWEFT_2018_15ops/${combinedcardsDir}/${var}/datacard.txt  -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o combined.root --X-allow-no-signal --PO eftOperators=cqq31
done
