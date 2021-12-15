# cuts

supercut = '   Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
            && mjj > 500 \
            && detajj > 3.5 \
           '


## Signal regions

cuts['VBS'] = {
   'expr': 'sr',
   'categories' : {
      '2j_ee_lowZ'                             : 'mll>120 && multiJet && 0.5*abs((Lepton_eta[0]+Lepton_eta[1])-(CleanJet_eta[0]+CleanJet_eta[1]))<1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
      '2j_ee_highZ'                            : 'mll>120 && multiJet && 0.5*abs((Lepton_eta[0]+Lepton_eta[1])-(CleanJet_eta[0]+CleanJet_eta[1]))>=1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
      '2j_mm_lowZ'                             : 'mll>120 && multiJet && 0.5*abs((Lepton_eta[0]+Lepton_eta[1])-(CleanJet_eta[0]+CleanJet_eta[1]))<1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
      '2j_mm_highZ'                            : 'mll>120 && multiJet && 0.5*abs((Lepton_eta[0]+Lepton_eta[1])-(CleanJet_eta[0]+CleanJet_eta[1]))>=1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',

    }
}

## Top control regions
cuts['top']  = { 
   'expr' : 'topcr',
   'categories' : {
#      '2j_ee_mm' : 'mll>120 && multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
      '2j_ee' : 'mll>120 && multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
      '2j_mm' : 'mll>120 && multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
   }
}

## DY control regions
cuts['DY']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
      '2j_ee'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
      '2j_mm'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
      }
}

