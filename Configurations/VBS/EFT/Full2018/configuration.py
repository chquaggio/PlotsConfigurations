# example of configuration file

treeName= 'Events'

date = '_feb24'

version = '_2018_vgamma_corr_v0'

tag = 'VBS_SS'  + date + version

# used by mkShape to define output directory for root files
outputDir = 'rootFile' + '_' + tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74 

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plots' + '_' + tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards' + '_' + tag


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
# nuisancesFile = 'nuisances_fast.py'
nuisancesFile = 'nuisances.py'

