# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    

structure['Zjj']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }
'''
structure['DY_lowZ']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['DY_highZ']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }
'''
structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['DY_PUJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }              

structure['DY_hardJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Dyemb']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Dyveto']  = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  'removeFromCuts' : [ k for k in cuts ],
              }

structure['Wjets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake_e']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'me' in k],
              }

structure['Fake_m']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'em' in k],
              }

structure['ttbar'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['singletop'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['WWewk']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggWW_Int']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['Wg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS_L'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['VgS_H'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['Zg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggH'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['WH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['H_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['bbH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ttH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ggH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['qqH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['WH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['ZH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['H_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }
                  
#---------------------------------------
#------------------EFT------------------
#---------------------------------------

structure['OSWW_5ops'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }
                  
structure['OSWW_15ops'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }

structure['sm'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }

# structure['sm_private'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }
osww_15ops = ['lin_cW', 'quad_cW', 'lin_cHW', 'quad_cHW', 'lin_cHWB', 'quad_cHWB', 'lin_cHbox', 'quad_cHbox', 'lin_cHDD', 'quad_cHDD', 'lin_cHl1', 'quad_cHl1', 'lin_cHl3', 'quad_cHl3', 'lin_cHq1', 'quad_cHq1', 'lin_cHq3', 'quad_cHq3', 'lin_cll', 'quad_cll', 'lin_cll1', 'quad_cll1', 'lin_cqq1', 'quad_cqq1', 'lin_cqq31', 'quad_cqq31', 'lin_cqq11', 'quad_cqq11', 'lin_cqq3', 'quad_cqq3']

for op in osww_15ops:
    structure[op] = {
        'isSignal' : 1,
        'isData'   : 0   
    }


# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }



print "INSTRUCTURE"
print cuts
#print nuisances['WWresum0j']
print "OK"

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

    print nuis
