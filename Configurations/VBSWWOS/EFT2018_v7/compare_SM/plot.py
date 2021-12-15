# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

#plot = {}

# keys here must match keys in samples.py    
#                    

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['WWewk_private']  = {
                  'color': 632, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }


# additional options

legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




