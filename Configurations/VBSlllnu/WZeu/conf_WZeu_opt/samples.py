import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch3l'

################################################
############ PRIVATE SAMPLES ###################
################################################

mcDirectory = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple_WZeu/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple_WZeu'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM')
samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cqq11 
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_QU')
samples['sm_lin_quad_cqq11'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_QU')
samples['quad_cqq11'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cqq1
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_QU')
samples['sm_lin_quad_cqq1'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_QU')
samples['quad_cqq1'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cqq31
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_QU')
samples['sm_lin_quad_cqq31'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_QU')
samples['quad_cqq31'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cqq3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_QU')
samples['sm_lin_quad_cqq3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_QU')
samples['quad_cqq3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cW
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cW_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cW_QU')
samples['sm_lin_quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cW_QU')
samples['quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cHl3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_QU')
samples['sm_lin_quad_cHl3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_QU')
samples['quad_cHl3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cHq3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_QU')
samples['sm_lin_quad_cHq3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_QU')
samples['quad_cHq3'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

# EFTNeg cll1
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_QU')
samples['sm_lin_quad_cll1'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_QU')
samples['quad_cll1'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.043',
    'FilesPerJob': 5,
}

#Mixing

################################################
############ BACKGROUND SAMPLES ################
################################################

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

#SSWW
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_madgraph')
samples['SSWW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# SSWW QCD
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# WZ QCD
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 4
}

# ZZ
files = nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')
samples['ZZ4L'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ggZZ2m2t_CP5') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4t_CP5') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4m_ext1')
samples['ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### TVX
files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu')
samples['TTV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'tZq_ll')
samples['tZq'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# Vg
files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

# Others
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
samples['DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG')
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

################################################
############ FAKE SAMPLES ######################
################################################

DataRun = [
    ['A','Run2018A-02Apr2020-v1'] ,
    ['B','Run2018B-02Apr2020-v1'] ,
    ['C','Run2018C-02Apr2020-v1'] ,
    ['D','Run2018D-02Apr2020-v1'] ,
]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}

fkDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__fakeW'

samples['Fake'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}
for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles(fkDirectory, pd + '_' + sd)
        samples['Fake']['name'].extend(files)
        samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

################################################
############ DATA SAMPLES ### ##################
################################################

dtDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7'

samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles(dtDirectory, pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))


