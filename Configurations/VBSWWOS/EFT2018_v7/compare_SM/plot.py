# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#


groupPlot['VBS']  = {
                  'nameHR' : 'VBS',
                  'isSignal' : 2,
                  'color': 888, #666,
                  'samples'  : ['WWewk', 'WWewk_private']
              }



#plot = {}

# keys here must match keys in samples.py    
#                    

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 1,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['WWewk_private']  = {
                  'color': 852, # kAzure -9 
                  'isSignal' : 1,
                  'isData'   : 0,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }


# additional options

legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




