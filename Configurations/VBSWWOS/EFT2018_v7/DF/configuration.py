# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

tag = 'OSWWEFT_2018_DF_cHq3'

# used by mkShape to define output directory for root files
outputDir = 'rootFiles_'+ tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plotEFT.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/c/cquaggio/Analysis/OSWW_EFT/plots/' + tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = '/eos/user/c/cquaggio/Analysis/OSWW_EFT/datacards/' + tag

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
