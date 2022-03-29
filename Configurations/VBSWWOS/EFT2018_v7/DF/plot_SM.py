# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
              

# groupPlot['VBS_SM']  = {
#                   'nameHR' : 'VBS_SM',
#                   'isSignal' : 0,
#                   'color': 888, #666,
#                   'samples'  : ['sm']
#               }

# groupPlot['VBS_SM_private']  = {
#                   'nameHR' : 'VBS_SM_private',
#                   'isSignal' : 2,
#                   'color': 666, #666,
#                   'samples'  : ['sm_private'],
#               }


#plot = {}

# keys here must match keys in samples.py    
#                    

plot['sm']  = {
                  'nameHR' : 'VBS_SM',
                  'color': 888, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 1,
                  #'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }


plot['sm_private']  = { 
                  'nameHR' : 'sm',
                  'color': 666 ,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale' : 1.97
              }




# additional options

legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'



