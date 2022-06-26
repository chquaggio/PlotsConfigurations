# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
              
# groupPlot['Zjj']  = {  
#                   'nameHR': 'Zjj',
#                   'isSignal' : 0,
#                   'color': 600,    # kBlue
#                   'samples'    : ['Zjj']
#               }

groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 0,
                  'color': 632, # kRed 
		  'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'bbH_hww', 'ggH_hww','ttH_hww','ZH_htt', 'ggZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt','bbH_htt','ttH_htt' ]
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww', 'qqH_htt', 'ggH_htt' ]
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY_lowZ', 'DY_highZ', 'Dyemb']
              }

groupPlot['Multiboson']  = {  
                  'nameHR' : 'Multiboson',
                  'isSignal' : 0,
                  'color': 617, # kViolet + 1  
                  'samples'  : ['VVV', 'VZ', 'WZ', 'ZZ', 'Vg', 'Wg', 'VgS_H', 'VgS_L']
              }

groupPlot['Fake']  = {
                  'nameHR' : 'nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake_m', 'Fake_e']
}

groupPlot['WW']  = {  
                  'nameHR' : 'WW QCD',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW', 'ggWW']
              }

groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }

groupPlot['VBS_SM']  = {
                  'nameHR' : 'OSWW SM',
                  'isSignal' : 0,
                  'color': 4, #666,
                  'samples'  : ['sm']
              }
# groupPlot['OSWW_cqq31'] = {
#                   'nameHR' : 'OSWW_cqq31',
#                   'color': 1, # kBlack
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cqq31', 'quad_cqq31']
#                   }

# groupPlot['OSWW_cqq3'] = {
#                   'nameHR' : 'OSWW_cqq3',
#                   'color': 1, # kBlue
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cqq3', 'quad_cqq3']
#                   }

# groupPlot['OSWW_cqq11'] = {
#                   'nameHR' : 'OSWW_cqq31',
#                   'color': 1, # kBlack
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cqq11', 'quad_cqq11']
#                   }

# groupPlot['OSWW_cqq1'] = {
#                   'nameHR' : 'OSWW SM+cqq1[k=1]',
#                   'color': 1, # kBlue
#                   'isSignal' : 0,
#                   'samples'   : ['sm', 'lin_cqq1', 'quad_cqq1']
#                   }                  

groupPlot['OSWW_cW'] = {
                  'nameHR' : 'OSWW SM+cW=1',
                  'color': 1, # kBlue
                  'isSignal' : 0,
                  'samples'   : ['sm', 'lin_cW', 'quad_cW']
                  }    

# groupPlot['OSWW_cHWB'] = {
#                   'nameHR' : 'OSWW_cHWB',
#                   'color': 1, # kBlue
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cHWB', 'quad_cHWB']
#                   }   

# groupPlot['OSWW_cHDD'] = {
#                   'nameHR' : 'OSWW_cHDD',
#                   'color': 1, # kBlue
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cHDD', 'quad_cHDD']
#                   }  

# groupPlot['OSWW_cHbox'] = {
#                   'nameHR' : 'OSWW SM+cHbox[k=1]',
#                   'color': 1, # kBlue
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cHbox', 'quad_cHbox']
#                   }  

# groupPlot['OSWW_cHq1'] = {
#                   'nameHR' : 'OSWW_cHq1',
#                   'color': 1, # kBlue
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cHq1', 'quad_cHq1']
#                   }  

# groupPlot['OSWW_cll1'] = {
#                   'nameHR' : 'OSWW_cll1',
#                   'color': 1, # kOrange+9
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cll1', 'quad_cll1']
#                   }

# groupPlot['OSWW_cHq3'] = {
#                   'nameHR' : 'OSWW SM+cHq3[k=1]',
#                   'color': 1, # kPink+4
#                   'isSignal' : 0,
#                   'samples'   : ['sm', 'lin_cHq3', 'quad_cHq3']
#                   }

# groupPlot['OSWW_cHq3'] = {
#                   'nameHR' : 'OSWW_cHq3',
#                   'color': 1, # kRed+2
#                   'isSignal' : 2,
#                   'samples'   : ['lin_cHq3', 'quad_cHq3']
#                   }

#plot = {}

# keys here must match keys in samples.py    
#                    
plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

'''
plot['DY_highZ']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }
'''

if useEmbeddedDY:
  plot['Dyemb']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

plot['Zjj']  = {  
                  'color': 600,    # kBlue
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

plot['WWewk']  = {
                  'nameHR' : 'WWewk',
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['Fake_m']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['Fake_e']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

              
plot['top'] = {   
                  'nameHR' : 'tW and t#bar{t}',
                  'color': 400,   # kYellow
                  'isSignal' : 0,
                  'isData'   : 0, 
                  #'scale'    : 1.0,
                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.94 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.94 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.94 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.94 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.94 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 0.86 ,
                       #'hww2l2v_13TeV_top_of1j'  : 0.86 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 0.86 ,
                       #'hww2l2v_13TeV_em_1j'     : 0.86 , 
                       #'hww2l2v_13TeV_me_1j'     : 0.86 , 
                        #},
                  }


plot['WW']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['ggWW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_H'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_L'] = {
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

# Htautau

plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

#plot['bbH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-1, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#plot['ttH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-2, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#
#plot['ggZH_htt'] = {
#                  'nameHR' : 'ggZHtt',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_htt'] = {
                  'nameHR' : 'qqHtt',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_htt'] = {
                  'nameHR' : 'ggHtt',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

# HWW 

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ggZH_hww'] = {
                  'nameHR' : 'ggZH',
                  'color': 632+4, # kRed+4
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

#plot['bbH_hww'] = {
#                  'nameHR' : 'bbH',
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

plot['ttH_hww'] = {
                  'nameHR' : 'ttH',
                  'color': 632+6, # kRed+6
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }

plot['sm'] = {
                  'nameHR' : 'WWewk',
                  'color': 632+6, # kRed+6
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }
osww_15ops = ['lin_cW', 'quad_cW', 'lin_cHW', 'quad_cHW', 'lin_cHWB', 'quad_cHWB', 'lin_cHbox', 'quad_cHbox', 'lin_cHDD', 'quad_cHDD', 'lin_cHl1', 'quad_cHl1', 'lin_cHl3', 'quad_cHl3', 'lin_cHq1', 'quad_cHq1', 'lin_cHq3', 'quad_cHq3', 'lin_cll', 'quad_cll', 'lin_cll1', 'quad_cll1', 'lin_cqq1', 'quad_cqq1', 'lin_cqq31', 'quad_cqq31', 'lin_cqq11', 'quad_cqq11', 'lin_cqq3', 'quad_cqq3']

# for op in osww_15ops:
#     if 'lin' in op:
#         plot[op] = {
#                   'nameHR' : op,
#                   'color': 600, # kRed+6
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   'scale'    : 1
#                   }
#     else:
#         plot[op] = {
#                   'nameHR' : op,
#                   'color': 600, # kRed+6
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   'scale'    : 1
#                   }

plot['lin_cW'] = {
                  'nameHR' : 'lin_cW',
                  'color': 632+6, # kRed+6
                  'isSignal' : 1,
                  'isData'   : 0,
                #   'scale'    : 5    #
                  }

plot['quad_cW'] = {
                  'nameHR' : 'quad_cW',
                  'color': 632+6, # kRed+6
                  'isSignal' : 1,
                  'isData'   : 0,
                #   'scale'    : 5    #
                  }

# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1
              }




# additional options

legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'



