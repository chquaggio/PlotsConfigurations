# Produce histograms

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=testmatch

# Group (hadd) histograms

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=8

# Data-driven DY estimation

    mkDYestim_data.py --pycfg=configuration --dycfg=dyestim_qqH --inputFile=rootFile/plots_qqH2017_v6.root

# Make datacards

    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_qqH2017_v6_DYEstimDATA.root --cardList=hww2l2v_13TeV_2j_vbf_ee,hww2l2v_13TeV_WW_2j_vbf_ee,hww2l2v_13TeV_top_2j_vbf_ee,hww2l2v_13TeV_2j_vbf_mm,hww2l2v_13TeV_WW_2j_vbf_mm,hww2l2v_13TeV_top_2j_vbf_mm,hww2l2v_13TeV_2j_vh_ee,hww2l2v_13TeV_WW_2j_vh_ee,hww2l2v_13TeV_top_2j_vh_ee,hww2l2v_13TeV_2j_vh_mm,hww2l2v_13TeV_WW_2j_vh_mm,hww2l2v_13TeV_top_2j_vh_mm

#STEP 5: Combine channels/categories
mkComb.py --pycfg=configuration_ --combineLocation=/afs/cern.ch/user/d/ddicroce/work/Latinos/CMSSW_10_2_13/src/ --combcfg=comb_

#STEP 6: Significance and best fit
#mkOptim (calculate the significance)
mkOptim.py --pycfg=configuration_ --combineLocation=/afs/cern.ch/user/d/ddicroce/work/Latinos/CMSSW_10_2_13/src/ --combcfg=comb_ --fomList=SExpPre,BestFit

#or CMSENV /afs/cern.ch/user/d/ddicroce/work/Latinos/CMSSW_10_2_13/src/ +
combine datacard.txt -M Significance --expectSignal=1 -t -1
combine datacard.txt -M FitDiagnostics  --rMin=-6 --rMax=20 -t -1 --expectSignal=1 --robustFit=1 --cminDefaultMinimizerStrategy 0

#TO check the significance value and best fit 
grep Significance: datacards/*/comb/SExpPre_*
grep "fit r:" datacards/*/comb/BestFit_*

#Create yield table
grep "proc" datacards/hww2l2v_13TeV_*/events/datacard.txt > yield.txt
grep "rate " datacards/hww2l2v_13TeV_*/events/datacard.txt >> yield.txt
:%!column -t #to organize the table

STEP 7: Plot
mkPlot.py --pycfg=configuration --inputFile=rootFile/plots_ --minLogCratio=0.1 --maxLogCratio=1000 --logOnly --fileFormats=png --onlyPlot=cratio
mkPlot.py --pycfg=configuration --inputFile=rootFile/plots_ --linearOnly --fileFormats=png --onlyPlot=cratio

#Make impacts
text2workspace.py datacard.txt -o workspace.root
combineTool.py -M Impacts -d workspace_0j.root -m 125 --doInitialFit -t -1 --expectSignal=1 --robustFit=1
combineTool.py -M Impacts -d workspace_0j.root -m 125 -t -1 --expectSignal=1 --robustFit=1 --doFits
combineTool.py -M Impacts -d workspace_0j.root -m 125 -o impacts_0j.json -t -1
plotImpacts.py -i impacts_0j.json -o Impact_0j