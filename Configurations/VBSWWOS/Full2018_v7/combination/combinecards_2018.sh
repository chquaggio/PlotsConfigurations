#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/workshop/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workDir=$PWD       # Full2018_v7
workDirDF=$PWD/VBSWWOS_18_DF
workDirSF=$PWD/VBSWWOS_18_SF

datacardDir=datacards
combinedcardsDir=VBSWWOS_18_comb

cd $workDir

combineCards.py   vbs_lowZ=${workDirDF}/${datacardDir}/VBS_2j_em_me_lowZ/mjj/datacard.txt \
                  vbs_highZ=${workDirDF}/${datacardDir}/VBS_2j_em_me_highZ/mjj/datacard.txt \
                  top=${workDirDF}/${datacardDir}/top_2j_em_me/events/datacard.txt \
                  dy=${workDirDF}/${datacardDir}/DY_2j_em_me/events/datacard.txt \
                  vbs_ee_lowZ=${workDirSF}/${datacardDir}/VBS_2j_ee_lowZ/mjj/datacard.txt \
                  vbs_ee_highZ=${workDirSF}/${datacardDir}/VBS_2j_ee_highZ/mjj/datacard.txt \
                  top_ee=${workDirSF}/${datacardDir}/top_2j_ee/events/datacard.txt \
                  dy_ee_lowDjj=${workDirSF}/${datacardDir}/DY_2j_ee_lowDetajj/events/datacard.txt \
                  dy_ee_highDjj=${workDirSF}/${datacardDir}/DY_2j_ee_highDetajj/events/datacard.txt \
                  vbs_mm_lowZ=${workDirSF}/${datacardDir}/VBS_2j_mm_lowZ/mjj/datacard.txt \
                  vbs_mm_highZ=${workDirSF}/${datacardDir}/VBS_2j_mm_highZ/mjj/datacard.txt \
                  top_mm=${workDirSF}/${datacardDir}/top_2j_mm/events/datacard.txt \
                  dy_mm_lowDjj=${workDirSF}/${datacardDir}/DY_2j_mm_lowDetajj/events/datacard.txt \
                  dy_mm_highDjj=${workDirSF}/${datacardDir}/DY_2j_mm_highDetajj/events/datacard.txt \
> ${workDir}/${combinedcardsDir}/mjj.txt

# DF

echo "nuisance edit drop DY top CMS_PUID_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop DY top CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt

#echo "nuisance edit drop VgS dy QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop Vg dy CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg dy CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Vg dy QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop top top CMS_btag_cferr1 Up" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop top top CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop top top CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt


# SF ee

#echo "nuisance edit drop Fake_e vbs_ee_lowZ CMS_fake_e_2018 Up" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Fake_e vbs_ee_lowZ CMS_fake_m_2018 Up" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Fake_e vbs_ee_lowZ CMS_fake_stat_e_2018 Up" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Fake_e vbs_ee_lowZ CMS_fake_stat_m_2018 Up" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop Vg top_ee CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_ee CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Vg top_ee QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee CMS_PUID_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee PS_FSR" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_ee PS_ISR" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop VgS_L top_ee QCDscale_VV" >> ${combinedcardsDir}/mjj.txt


# SF mm

echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ PS_FSR" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg vbs_mm_lowZ PS_ISR" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Vg vbs_mm_lowZ QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

#echo "nuisance edit drop VgS_H vbs_mm_lowZ QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

#echo "nuisance edit drop Vg vbs_mm_lowZ QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop Vg top_mm CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Vg top_mm CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop Vg top_mm QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop VgS_L top_mm QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_cferr1" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_cferr2" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_hf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_jes" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_lf" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_eff_e_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj CMS_eff_m_2018" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj PS_FSR" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop VgS_L dy_mm_lowDjj PS_ISR" >> ${combinedcardsDir}/mjj.txt
#echo "nuisance edit drop VgS_L dy_mm_lowDjj QCDscale_VV" >> ${combinedcardsDir}/mjj.txt

echo "nuisance edit drop Fake_m dy_mm_highDjj CMS_fake_e_2018 Up" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Fake_m dy_mm_highDjj CMS_fake_m_2018 Up" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Fake_m dy_mm_highDjj CMS_fake_stat_e_2018 Up" >> ${combinedcardsDir}/mjj.txt
echo "nuisance edit drop Fake_m dy_mm_highDjj CMS_fake_stat_m_2018 Up" >> ${combinedcardsDir}/mjj.txt


text2workspace.py ${workDir}/${combinedcardsDir}/mjj.txt -o ${workDir}/${combinedcardsDir}/mjj.root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]'


