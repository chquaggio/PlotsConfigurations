#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
#workDir=/afs/cern.ch/user/m/mlizzo/work/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/nAODv6_v6 
workDir=/afs/cern.ch/user/c/cquaggio/private/PlotsConfigurations/Configurations/VBSWWOS/EFT2018_v7/DF

datacardDir=OSWWEFT_2018_DF_finenuis
combinedcardsDir=combined
workspaceDir=workspace

cd $workDir
mkdir -p ${workDir}/${datacardDir}/${combinedcardsDir}

vars="detajj eta_1j eta_1l eta_2j eta_2l mjj mll pt_1j pt_1l pt_2j pt_2l ptll PuppiMET_pt Zepp_1l Zepp_2l"

for var in $vars
do
    mkdir -p ${workDir}/${datacardDir}/${combinedcardsDir}/${var}
    combineCards.py   vbs_lowZ=${workDir}/${datacardDir}/VBS_2j_em_me_lowZ/${var}/datacard.txt \
                    vbs_highZ=${workDir}/${datacardDir}/VBS_2j_em_me_highZ/${var}/datacard.txt \
                    top=${workDir}/${datacardDir}/top_2j_em_me/events/datacard.txt \
                    dy=${workDir}/${datacardDir}/dycr_2j_em_me/events/datacard.txt \
                    > ${workDir}/${datacardDir}/${combinedcardsDir}/${var}/datacard.txt



    # echo "nuisance edit drop quad_cHq3 dy CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 dy CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_highZ CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq3 vbs_lowZ CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cll dy CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cll dy CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cHq1 dy CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cHq1 dy CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq1 dy CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 dy CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq3 dy CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 dy CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_lowZ CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 vbs_highZ CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq3 top CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq3 top CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_PUID_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_cferr1" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_cferr2" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_hf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_hfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_hfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_jes" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_lf" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_lfstats1_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_btag_lfstats2_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_eff_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_eff_hwwtrigger_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # echo "nuisance edit drop quad_cqq1 vbs_highZ CMS_eff_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt

    echo "nuisance edit drop Fake_e vbs_highZ CMS_fake_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_highZ CMS_fake_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_highZ CMS_fake_stat_m_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    echo "nuisance edit drop Fake_e vbs_highZ CMS_fake_stat_e_2018" >> ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt
    # text2workspace.py  ${datacardDir}/${combinedcardsDir}/${var}/datacard.txt  -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o combined.root --X-allow-no-signal --PO eftOperators=cqq31
done
