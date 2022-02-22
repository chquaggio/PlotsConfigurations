#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/c/cquaggio/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
#workDir=/afs/cern.ch/user/m/mlizzo/work/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/nAODv6_v6 
workDir=/eos/user/c/cquaggio/Analysis/OSWW_EFT

datacardDir=datacards/OSWWEFT_2018_DF
combinedcardsDir=combinedcards
workspaceDir=workspace

cd $workDir

vars="mjj mll detajj ptll"
ops="cW"

for var in $vars
do
    for op in $ops
    do
            combineCards.py   vbs_lowZ=${workDir}/${datacardDir}/VBS_2j_em_me_lowZ/${var}/datacard.txt \
                vbs_highZ=${workDir}/${datacardDir}/VBS_2j_em_me_highZ/${var}/datacard.txt \
            > ${workDir}/${combinedcardsDir}/${var}_em_me.txt
#                top=${workDir}/${datacardDir}/top_2j_em_me/events/datacard.txt \
#                dy=${workDir}/${datacardDir}/dycr_2j_em_me/events/datacard.txt \

    # echo "nuisance edit drop DY top CMS_PUID_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_cferr1" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_cferr2" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_hf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_jes" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_lf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_eff_e_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop DY top CMS_eff_m_2018" >> ${combinedcardsDir}/${var}_em_me.txt

    # echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_hf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_jes" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_lf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_eff_e_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg top CMS_eff_m_2018" >> ${combinedcardsDir}/${var}_em_me.txt

    # #echo "nuisance edit drop VgS dy QCDscale_VV" >> ${combinedcardsDir}/${var}_em_me.txt

    # echo "nuisance edit drop Vg dy CMS_btag_cferr1" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_cferr2" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_hf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_hfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_hfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_jes" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_lf" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_lfstats1_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_btag_lfstats2_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_eff_e_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_eff_hwwtrigger_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop Vg dy CMS_eff_m_2018" >> ${combinedcardsDir}/${var}_em_me.txt
    # #echo "nuisance edit drop Vg dy QCDscale_VV" >> ${combinedcardsDir}/${var}_em_me.txt

    # echo "nuisance edit drop top top CMS_btag_cferr1" >> ${combinedcardsDir}/${var}_em_me.txt
    # echo "nuisance edit drop top top CMS_btag_hf" >> ${combinedcardsDir}/${var}_em_me.txt

#    text2workspace.py  ${combinedcardsDir}/${var}_em_me.txt -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o ${workspaceDir}/${var}_em_me.root --X-allow-no-signal --PO eftOperators=${op}
#    combine -M MultiDimFit ${workspaceDir}/${var}_em_me.root --algo=grid --points 200 -m 125 -t -1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --redefineSignalPOIs k_${op} --freezeParameters r --setParameters r=1 --setParameterRanges k_${op}=-2.0,2.0 --verbose -1
    done
done
