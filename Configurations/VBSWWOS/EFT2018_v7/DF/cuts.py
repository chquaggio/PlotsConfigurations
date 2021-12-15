#cuts

supercut = '   mll>50 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && ptll>30 \
            && PuppiMET_pt > 20 \
            && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
            && mjj > 300 \
            && detajj > 2.5 \
            && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
           '

##signal region
cuts['VBS'] = {
   'expr': 'sr',
   'categories' : {
      '2j_em_me_lowZ'   : 'Zeppll_al < 1', 
      '2j_em_me_highZ'  : 'Zeppll_al >=1',
    }
}    

# Top control region
cuts['top']  = {
   'expr': 'topcr',
   'categories' : {
      '2j_em_me'   : 'multiJet', 
    }
} 

# DY control region
cuts['dycr'] = {
   'expr': 'dycr',
   'categories' : {
      '2j_em_me'   : 'mll < 80 && multiJet', 
    }
}