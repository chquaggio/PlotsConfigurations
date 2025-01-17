import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
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
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

dataReco = 'Run2018_102X_nAODv7_Full2018v7'

fakeReco = dataReco

embedReco = 'Embedding2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

embedSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
embedDirectory = os.path.join(treeBaseDir, embedReco, embedSteps)

################################################
############ DATA DECLARATION ##################
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


#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

useEmbeddedDY = True
useDYtt = True

# The Dyveto sample is used to estimate one piece of the Dyemb uncertainty
# To avoid running it all the times, it was run once and the uncertainty was converted into a lnN (see nuisances.py)
runDYveto = False

embed_tautauveto = '' #Setup
if useEmbeddedDY:
  embed_tautauveto = '*embed_tautauveto'


if useEmbeddedDY:
  # Actual embedded data
  samples['Dyemb'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut*Muon_ttHMVA_SF*embedtotal*genWeight',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 20
  }

  for run_, sd in DataRun:
      files = nanoGetSampleFiles(embedDirectory, 'DYToTT_MuEle_Embedded_Run2018' + run_)
      samples['Dyemb']['name'].extend(files)
      samples['Dyemb']['weights'].extend(['Trigger_ElMu'] * len(files))
  if runDYveto:
  # Vetoed MC: Needed for uncertainty
    files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop') + \
        nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
  
    samples['Dyveto'] = {
        'name': files,
        'weight': '(1-embed_tautauveto)',
        'FilesPerJob': 1, # There's some error about not finding sample-specific variables like "nllW" when mixing different samples into a single job; so split them all up instead
    }
  
    addSampleWeight(samples, 'Dyveto', 'TTTo2L2Nu', mcCommonWeight + '* (topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)')
    addSampleWeight(samples, 'Dyveto', 'ST_tW_antitop_ext1', mcCommonWeight)
    addSampleWeight(samples, 'Dyveto', 'ST_tW_top_ext1', mcCommonWeight)
    addSampleWeight(samples, 'Dyveto', 'EWKZ2Jets_ZToLL_M-50', mcCommonWeight)
    addSampleWeight(samples, 'Dyveto', 'WpWmJJ_QCD_noTop', mcCommonWeight)
    addSampleWeight(samples, 'Dyveto', 'WpWmJJ_EWK_noTop', mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)')
    addSampleWeight(samples, 'Dyveto', 'GluGluToWWToTNTN', mcCommonWeight + '*1.53/1.4')
    addSampleWeight(samples, 'Dyveto', 'ZZTo2L2Nu_ext1', mcCommonWeight + '*1.11')
    addSampleWeight(samples, 'Dyveto', 'ZZTo2L2Q', mcCommonWeight + '*1.11')
    addSampleWeight(samples, 'Dyveto', 'ZZTo4L_ext1', mcCommonWeight + '*1.11')
    addSampleWeight(samples, 'Dyveto', 'WZTo2L2Q', mcCommonWeight + '*1.11')
    addSampleWeight(samples, 'Dyveto', 'ZGToLLG', ' ( ' + mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))' + ' ) + ( ' + mcCommonWeight + ' * ((Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4) * 0.94 + (Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4) * 1.14) * (Gen_ZGstar_mass > 0)' + ' ) ') # Vg contribution + VgS contribution
    addSampleWeight(samples, 'Dyveto', 'WZTo3LNu_mllmin01', mcCommonWeight + '*((Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4) * 0.94 + (Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4) * 1.14) * (Gen_ZGstar_mass > 0.1)')
  

###### DY MC ######
# We need to keep DY MC as well, because only embedded events passing the ElMu trigger are considered
# Events failing ElMu but passing one of the other triggers are included in the DY MC
files=[]
if useDYtt:
  files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')

else:
  files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 6,
}
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw')


###### Zjj EWK #######

files = nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['Zjj'] = {
        'name': files,
        'weight': mcCommonWeight+embed_tautauveto+'*lhe_mjj>120',
        'FilesPerJob': 1,
        }


####### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto,
    'FilesPerJob': 2,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWJTo2L2Nu_NNLOPS'),
    'weight': mcCommonWeight+embed_tautauveto+'*9.',
    'FilesPerJob': 3
}


samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop_dipoleRecoil_private'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
    'FilesPerJob': 4
}

# k-factor 1.4 already taken into account in XSWeight
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}

######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch+embed_tautauveto + '*(Gen_ZGstar_mass <= 0)',
    'FilesPerJob': 4
}


######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto + '*1.11',
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

##########################################
############   SIGNALS  ##################
##########################################

### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_hww', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
addSampleWeight(samples, 'ggH_hww', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')


############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

#signals.append('qqH_hww')

############ ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

#signals.append('ZH_hww')

samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 4
}

#signals.append('ggZH_hww')

############ WH H->WW ############

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 4
}


############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 1
}


############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 20
}


samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 10
}


samples['ZH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 4
}


samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
   'weight': mcCommonWeight,
    'FilesPerJob': 4
}

############################################################
################## EFT directory location ##################
############################################################

EftDirectory = '/eos/user/c/cquaggio/nAOD/PostProc/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

# files = nanoGetSampleFiles(EftDirectory, 'OSWW_DF_5ops')

# samples['OSWW_5ops'] = {
#     'name': files,
#     'weight': mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',    # factor for cross section normalization
#     'FilesPerJob': 3
# }

# osww = ['lin_cqq3', 'quad_cqq3', 'lin_cqq31', 'quad_cqq31', 'lin_cHl3', 'quad_cHl3', 'lin_cHq3', 'quad_cHq3', 'lin_cll1', 'quad_cll1']
# for op in osww:
#     samples[op] = {
#     'name': files,
#     'weight': mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*rwgt_'+op,    # factor for cross section normalization
#     'FilesPerJob': 3
#     }

files = nanoGetSampleFiles(EftDirectory, 'OSWW_EFTdim6')

osww_15ops = ['lin_cW', 'quad_cW', 'lin_cHW', 'quad_cHW', 'lin_cHWB', 'quad_cHWB', 'lin_cHbox', 'quad_cHbox', 'lin_cHDD', 'quad_cHDD', 'lin_cHl1', 'quad_cHl1', 'lin_cHl3', 'quad_cHl3', 'lin_cHq1', 'quad_cHq1', 'lin_cHq3', 'quad_cHq3', 'lin_cll', 'quad_cll', 'lin_cll1', 'quad_cll1', 'lin_cqq1', 'quad_cqq1', 'lin_cqq31', 'quad_cqq31', 'lin_cqq11', 'quad_cqq11', 'lin_cqq3', 'quad_cqq3']

# samples['OSWW_15ops'] = {
#     'name': files,
#     'weight': mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',    # factor for cross section normalization
#     'FilesPerJob': 1
# }

samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*LHEReweightingWeight[0]',    # factor for cross section normalization
    'FilesPerJob': 3
}

for op in osww_15ops:
    samples[op] = {
    'name': files,
    'weight': mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*rwgt_'+op,    # factor for cross section normalization
    'FilesPerJob': 1
    }

###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
 'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'e': 'abs(Lepton_pdgId[1]) == 11',
  'm': 'abs(Lepton_pdgId[1]) == 13'
}

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
