

# nuisances

#nuisances = {}
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake_lep')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

changetree=['WpWp_QCD','WpWp_EWK','WpWp_EWK_fid','WpWp_EWK_out','WpWp_EWK_lep1pt_bin0','WpWp_EWK_lep1pt_bin1','WpWp_EWK_lep1pt_bin2','WpWp_EWK_lep2pt_bin0','WpWp_EWK_lep2pt_bin1','WpWp_EWK_lep2pt_bin2','WpWp_EWK_jet1pt_bin0','WpWp_EWK_jet1pt_bin1','WpWp_EWK_jet1pt_bin2','WpWp_EWK_jet2pt_bin0','WpWp_EWK_jet2pt_bin1','WpWp_EWK_jet2pt_bin2','WpWp_EWK_mll_bin0','WpWp_EWK_mll_bin1','WpWp_EWK_mll_bin2','WpWp_EWK_mjj_bin0','WpWp_EWK_mjj_bin1','WpWp_EWK_mjj_bin2']
# name of samples here must match keys in samples.py
# basedir='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6'
################################ EXPERIMENTAL UNCERTAINTIES  #################################
nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake_lep': '1.3'
    },
    #'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}
'''
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'type': 'shape',
    'kind': 'suffix',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
}
'''
##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}
'''
nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'type': 'shape',
    'kind': 'suffix',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}
'''
##### Jet energy scale
'''
nuisances['jes'] = {
    'name': 'CMS_scale_j_2018',
    'type': 'shape',
    'kind': 'suffix',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JESup_suffix'),
    'folderDown': makeMCDirectory('JESdo_suffix'),
}
'''
##### MET energy scale
'''
nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'type': 'shape',
    'kind': 'suffix',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
}
'''
##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in mc),
    'AsLnN': '1',
}

variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 4, 6, 7]]

nuisances['QCDscale'] = {
    'name': 'QCDscale',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WpWp_EWK': variations,
        'WpWp_QCD': variations,
        'WpWp_EWK_fid': variations,
        'WpWp_EWK_out': variations,
        'WpWp_EWK_lep1pt_bin0': variations,
        'WpWp_EWK_lep1pt_bin1': variations,
        'WpWp_EWK_lep1pt_bin2': variations,
        'WpWp_EWK_lep2pt_bin0': variations,
        'WpWp_EWK_lep2pt_bin1': variations,
        'WpWp_EWK_lep2pt_bin2': variations,
        'WpWp_EWK_jet1pt_bin0': variations,
        'WpWp_EWK_jet1pt_bin1': variations,
        'WpWp_EWK_jet1pt_bin2': variations,
        'WpWp_EWK_jet2pt_bin0': variations,
        'WpWp_EWK_jet2pt_bin1': variations,
        'WpWp_EWK_jet2pt_bin2': variations,
        'WpWp_EWK_mll_bin0': variations,
        'WpWp_EWK_mll_bin1': variations,
        'WpWp_EWK_mll_bin2': variations,
        'WpWp_EWK_mjj_bin0': variations,
        'WpWp_EWK_mjj_bin1': variations,
        'WpWp_EWK_mjj_bin2': variations,
    },
    'AsLnN': '1'
}

variations = ['LHEPdfWeight[%d]' % i for i in range(0,101)]

nuisances['pdf'] = {
    'name': 'pdf',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WpWp_EWK': variations,
        'WpWp_QCD': variations,
        'WpWp_EWK_fid': variations,
        'WpWp_EWK_out': variations,
        'WpWp_EWK_lep1pt_bin0': variations,
        'WpWp_EWK_lep1pt_bin1': variations,
        'WpWp_EWK_lep1pt_bin2': variations,
        'WpWp_EWK_lep2pt_bin0': variations,
        'WpWp_EWK_lep2pt_bin1': variations,
        'WpWp_EWK_lep2pt_bin2': variations,
        'WpWp_EWK_jet1pt_bin0': variations,
        'WpWp_EWK_jet1pt_bin1': variations,
        'WpWp_EWK_jet1pt_bin2': variations,
        'WpWp_EWK_jet2pt_bin0': variations,
        'WpWp_EWK_jet2pt_bin1': variations,
        'WpWp_EWK_jet2pt_bin2': variations,
        'WpWp_EWK_mll_bin0': variations,
        'WpWp_EWK_mll_bin1': variations,
        'WpWp_EWK_mll_bin2': variations,
        'WpWp_EWK_mjj_bin0': variations,
        'WpWp_EWK_mjj_bin1': variations,
        'WpWp_EWK_mjj_bin2': variations,
    },
    'AsLnN': '1'
}
# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
# Use the following if you want to apply the automatic combine MC stat nuisances->Faster than bin-by-bin
nuisances['stat']  = {
    'type'  : 'auto',
    'maxPoiss'  : '10',
    'includeSignal'  : '1',
    'samples' : {}
}
# Differnt type of uncentainties: type->ln N: (modify only event yeld) use a lognorm distributions with sigma = uncertainty. For normalization rateParam
# can be used--> use a uniform distribution;
# Shape: modify not only the events yelds but the event selection too (the shape) will run the varied shapes
# according to the following two possible kinds
# kind-> weight: Use the specified weight to reweight events;
# tree: uses the provided alternative trees;
# The MC statistics is a particular uncertainty: is caused by our finite statistics used to elaborate the template fits. Two approach: unfied and bin-by-bin (bbb)
