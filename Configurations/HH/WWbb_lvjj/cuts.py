# cuts

#cuts = {}
  
supercut = '(std_vector_lepton_pt[0]>18.0) &&\
            ((std_vector_muon_isTightLepton_cut_Tight80x[0]>0.5) || (std_vector_electron_isTightLepton_cut_WP_Tight80X[0]>0.5)) && \
            (1*(std_vector_jet_DeepCSVB[0] > 0.8958)*(std_vector_jet_pt[0]>20) + \
             1*(std_vector_jet_DeepCSVB[1] > 0.8958)*(std_vector_jet_pt[1]>20) + \
             1*(std_vector_jet_DeepCSVB[2] > 0.8958)*(std_vector_jet_pt[2]>20) + \
             1*(std_vector_jet_DeepCSVB[3] > 0.8958)*(std_vector_jet_pt[3]>20) + \
             1*(std_vector_jet_DeepCSVB[4] > 0.8958)*(std_vector_jet_pt[4]>20) + \
             1*(std_vector_jet_DeepCSVB[5] > 0.8958)*(std_vector_jet_pt[5]>20) + \
             1*(std_vector_jet_DeepCSVB[6] > 0.8958)*(std_vector_jet_pt[6]>20) + \
             1*(std_vector_jet_DeepCSVB[7] > 0.8958)*(std_vector_jet_pt[7]>20) + \
             1*(std_vector_jet_DeepCSVB[8] > 0.8958)*(std_vector_jet_pt[8]>20) + \
             1*(std_vector_jet_DeepCSVB[9] > 0.8958)*(std_vector_jet_pt[9]>20) \
             ) >= 1'


#cuts['wwlvjj_13TeV_e']  = 'std_vector_jet_pt[0]>25'
#cuts['wwlvjj_13TeV_m']  = 'std_vector_jet_pt[0]>25'

#&& std_vector_lepton_pt[0]>20 && (1*(std_vector_jet_cmvav2[0]>-0.715) + 1*(std_vector_jet_cmvav2[1]>-0.715) + 1*(std_vector_jet_cmvav2[2]>-0.715) + 1*(std_vector_jet_cmvav2[3]>-0.715) + 1*(std_vector_jet_cmvav2[4]>-0.715) + 1*(std_vector_jet_cmvav2[5]>-0.715))>=1 
#cuts['wwlvjj_13TeV_e']  = 'abs(std_vector_lepton_flavour[0]) == 11'
#cuts['wwlvjj_13TeV_m']  = 'abs(std_vector_lepton_flavour[0]) == 13'

#cuts['wwlvjj_13TeV_e']  = 'abs(std_vector_lepton_flavour[0]) == 11 && std_vector_fatjet_pt[0]>0 && std_vector_lepton_pt[1] <=0'
#cuts['wwlvjj_13TeV_m']  = 'abs(std_vector_lepton_flavour[0]) == 13 && std_vector_fatjet_pt[0]>0 && std_vector_lepton_pt[1] <=0'


cuts['nocut_1']  = '1.'
#cuts['cmva_loose']  = '(1*(std_vector_jet_cmvav2[0]>-0.5884)*(std_vector_jet_pt[0]>20) + \
#                        1*(std_vector_jet_cmvav2[1]>-0.5884)*(std_vector_jet_pt[1]>20) + \
#                        1*(std_vector_jet_cmvav2[2]>-0.5884)*(std_vector_jet_pt[2]>20) + \
#                        1*(std_vector_jet_cmvav2[3]>-0.5884)*(std_vector_jet_pt[3]>20) + \
#                        1*(std_vector_jet_cmvav2[4]>-0.5884)*(std_vector_jet_pt[4]>20) + \
#                        1*(std_vector_jet_cmvav2[5]>-0.5884)*(std_vector_jet_pt[5]>20) + \
#                        1*(std_vector_jet_cmvav2[6]>-0.5884)*(std_vector_jet_pt[6]>20) + \
#                        1*(std_vector_jet_cmvav2[7]>-0.5884)*(std_vector_jet_pt[7]>20) + \
#                        1*(std_vector_jet_cmvav2[8]>-0.5884)*(std_vector_jet_pt[8]>20) + \
#                        1*(std_vector_jet_cmvav2[9]>-0.5884)*(std_vector_jet_pt[9]>20))>=1'

#cuts['cmva_medium']  = '(1*(std_vector_jet_cmvav2[0]>0.4432)*(std_vector_jet_pt[0]>20) + \
#                        1*(std_vector_jet_cmvav2[1]>0.4432)*(std_vector_jet_pt[1]>20) + \
#                        1*(std_vector_jet_cmvav2[2]>0.4432)*(std_vector_jet_pt[2]>20) + \
#                        1*(std_vector_jet_cmvav2[3]>0.4432)*(std_vector_jet_pt[3]>20) + \
#                        1*(std_vector_jet_cmvav2[4]>0.4432)*(std_vector_jet_pt[4]>20) + \
#                        1*(std_vector_jet_cmvav2[5]>0.4432)*(std_vector_jet_pt[5]>20) + \
#                        1*(std_vector_jet_cmvav2[6]>0.4432)*(std_vector_jet_pt[6]>20) + \
#                        1*(std_vector_jet_cmvav2[7]>0.4432)*(std_vector_jet_pt[7]>20) + \
#                        1*(std_vector_jet_cmvav2[8]>0.4432)*(std_vector_jet_pt[8]>20) + \
#                        1*(std_vector_jet_cmvav2[9]>0.4432)*(std_vector_jet_pt[9]>20))>=1'
#
#
#
#cuts['cmva_tight']  = '(1*(std_vector_jet_cmvav2[0]>0.9432)*(std_vector_jet_pt[0]>20) + \
#                        1*(std_vector_jet_cmvav2[1]>0.9432)*(std_vector_jet_pt[1]>20) + \
#                        1*(std_vector_jet_cmvav2[2]>0.9432)*(std_vector_jet_pt[2]>20) + \
#                        1*(std_vector_jet_cmvav2[3]>0.9432)*(std_vector_jet_pt[3]>20) + \
#                        1*(std_vector_jet_cmvav2[4]>0.9432)*(std_vector_jet_pt[4]>20) + \
#                        1*(std_vector_jet_cmvav2[5]>0.9432)*(std_vector_jet_pt[5]>20) + \
#                        1*(std_vector_jet_cmvav2[6]>0.9432)*(std_vector_jet_pt[6]>20) + \
#                        1*(std_vector_jet_cmvav2[7]>0.9432)*(std_vector_jet_pt[7]>20) + \
#                        1*(std_vector_jet_cmvav2[8]>0.9432)*(std_vector_jet_pt[8]>20) + \
#                        1*(std_vector_jet_cmvav2[9]>0.9432)*(std_vector_jet_pt[9]>20))>=1'
#
#cuts['deepCSV_loose']  = '(1*(std_vector_jet_DeepCSVB[0] > 0.2219)*(std_vector_jet_pt[0]>20) +\
#                          1*(std_vector_jet_DeepCSVB[1] > 0.2219)*(std_vector_jet_pt[1]>20) +\
#                          1*(std_vector_jet_DeepCSVB[2] > 0.2219)*(std_vector_jet_pt[2]>20) +\
#                          1*(std_vector_jet_DeepCSVB[3] > 0.2219)*(std_vector_jet_pt[3]>20) +\
#                          1*(std_vector_jet_DeepCSVB[4] > 0.2219)*(std_vector_jet_pt[4]>20) +\
#                          1*(std_vector_jet_DeepCSVB[5] > 0.2219)*(std_vector_jet_pt[5]>20) +\
#                          1*(std_vector_jet_DeepCSVB[6] > 0.2219)*(std_vector_jet_pt[6]>20) +\
#                          1*(std_vector_jet_DeepCSVB[7] > 0.2219)*(std_vector_jet_pt[7]>20) +\
#                          1*(std_vector_jet_DeepCSVB[8] > 0.2219)*(std_vector_jet_pt[8]>20) +\
#                          1*(std_vector_jet_DeepCSVB[9] > 0.2219)*(std_vector_jet_pt[9]>20))>=1'
#
#cuts['deepCSV_medium']  = '(1*(std_vector_jet_DeepCSVB[0] > 0.6324)*(std_vector_jet_pt[0]>20) +\
#                          1*(std_vector_jet_DeepCSVB[1] > 0.6324)*(std_vector_jet_pt[1]>20) +\
#                          1*(std_vector_jet_DeepCSVB[2] > 0.6324)*(std_vector_jet_pt[2]>20) +\
#                          1*(std_vector_jet_DeepCSVB[3] > 0.6324)*(std_vector_jet_pt[3]>20) +\
#                          1*(std_vector_jet_DeepCSVB[4] > 0.6324)*(std_vector_jet_pt[4]>20) +\
#                          1*(std_vector_jet_DeepCSVB[5] > 0.6324)*(std_vector_jet_pt[5]>20) +\
#                          1*(std_vector_jet_DeepCSVB[6] > 0.6324)*(std_vector_jet_pt[6]>20) +\
#                          1*(std_vector_jet_DeepCSVB[7] > 0.6324)*(std_vector_jet_pt[7]>20) +\
#                          1*(std_vector_jet_DeepCSVB[8] > 0.6324)*(std_vector_jet_pt[8]>20) +\
#                          1*(std_vector_jet_DeepCSVB[9] > 0.6324)*(std_vector_jet_pt[9]>20))>=1'

#cuts['deepCSV_tight']  = '(1*(std_vector_jet_DeepCSVB[0] > 0.8958)*(std_vector_jet_pt[0]>20) +\
#                          1*(std_vector_jet_DeepCSVB[1] > 0.8958)*(std_vector_jet_pt[1]>20) +\
#                          1*(std_vector_jet_DeepCSVB[2] > 0.8958)*(std_vector_jet_pt[2]>20) +\
#                          1*(std_vector_jet_DeepCSVB[3] > 0.8958)*(std_vector_jet_pt[3]>20) +\
#                          1*(std_vector_jet_DeepCSVB[4] > 0.8958)*(std_vector_jet_pt[4]>20) +\
#                          1*(std_vector_jet_DeepCSVB[5] > 0.8958)*(std_vector_jet_pt[5]>20) +\
#                          1*(std_vector_jet_DeepCSVB[6] > 0.8958)*(std_vector_jet_pt[6]>20) +\
#                          1*(std_vector_jet_DeepCSVB[7] > 0.8958)*(std_vector_jet_pt[7]>20) +\
#                          1*(std_vector_jet_DeepCSVB[8] > 0.8958)*(std_vector_jet_pt[8]>20) +\
#                          1*(std_vector_jet_DeepCSVB[9] > 0.8958)*(std_vector_jet_pt[9]>20))>=1'
#

#cuts['lepton_pt_20']  = 'std_vector_lepton_pt[0]>20'
cuts['lepton_pt_30']  = 'std_vector_lepton_pt[0]>30'
#cuts['jet_pt_1']  = 'std_vector_lepton_pt[0]>30 && std_vector_jet_pt[0]>25'
#cuts['jet_pt_2']  = 'std_vector_lepton_pt[0]>30 && std_vector_jet_pt[0]>25 && std_vector_jet_pt[1]>25'
#cuts['jet_pt_3']  = 'std_vector_lepton_pt[0]>30 && std_vector_jet_pt[0]>25 && std_vector_jet_pt[1]>25 && std_vector_jet_pt[2]>25'
#cuts['jet_pt_4']  = 'std_vector_lepton_pt[0]>30 && std_vector_jet_pt[0]>25 && std_vector_jet_pt[1]>25 && std_vector_jet_pt[2]>25 && std_vector_jet_pt[3]>25'
#cuts['met']= 'std_vector_lepton_pt[0]>30 && metPfType1<500'
#cuts['wwlvjj_13TeV_btag']  = 'std_vector_jet_pt[3]>25 && (1*(std_vector_jet_cmvav2[0]>-0.715) + 1*(std_vector_jet_cmvav2[1]>-0.715) + 1*(std_vector_jet_cmvav2[2]>-0.715) + 1*(std_vector_jet_cmvav2[3]>-0.715) + 1*(std_vector_jet_cmvav2[4]>-0.715) + 1*(std_vector_jet_cmvav2[5]>-0.715))>=1'
##cuts['wwlvjj_13TeV_ptlep_btag']  = 'std_vector_lepton_pt[0]>25 && (1*(std_vector_jet_cmvav2[0]>-0.715) + 1*(std_vector_jet_cmvav2[1]>-0.715) + 1*(std_vector_jet_cmvav2[2]>-0.715) + 1*(std_vector_jet_cmvav2[3]>-0.715) + 1*(std_vector_jet_cmvav2[4]>-0.715) + 1*(std_vector_jet_cmvav2[5]>-0.715))>=1'
#cuts['wwlvjj_13TeV_e']  = 'abs(std_vector_lepton_flavour[0]) == 11'
#cuts['wwlvjj_13TeV_m']  = 'abs(std_vector_lepton_flavour[0]) == 13'



