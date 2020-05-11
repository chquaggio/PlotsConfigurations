#!/bin/bash

# Shapes
#mkShapesMulti.py --pycfg=2HDMa_conf.py --doBatch=True --batchQueue=workday --treeName=Events --batchSplit=Samples,Files

# hadd
#rm rootFile2HDMa_NoData/plots_2HDMaSemlep_2017.root
#mkShapesMulti.py --pycfg=2HDMa_conf.py --doHadd=True --doNotCleanup --nThreads=8 --batchSplit=Samples,Files

# plots
mkPlot.py --pycfg=2HDMa_conf.py --inputFile=2HDMa_root/plots_MHlnjj_2017.root --showIntegralLegend=1
mkPlot.py --pycfg=2HDMa_conf.py --inputFile=2HDMa_root/plots_MHlnjj_2017.root --showIntegralLegend=1 --scaleToPlot=3000. --logOnly
#mkPlot.py --pycfg=configuration2HDMa_NoData.py --inputFile=rootFile2HDMa_NoData/plots_2HDMaSemlep_2017.root --showIntegralLegend=1 --scaleToPlot=3000. --logOnly