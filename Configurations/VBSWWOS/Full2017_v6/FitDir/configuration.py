# example of configuration file

tag = '2017_v6'
outputDir = 'rootFile'
treeName = 'Events'
date='131120'
# luminosity to normalize to
lumi = 41.53

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py' 

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of plot
plotFile = 'plot.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
# structure file for datacard
structureFile = 'structure.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/f/fcetorel/www/VBS_OS/test/2017/SignalRegion_v6_'+date
# used by mkDatacards to define output directory for datacards
outputDirDatacard = '/afs/cern.ch/work/f/fcetorel/private/work2/VBS_OS/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS_OS/\
Full2017_v6/FitDir/datacards_df_sf/'

