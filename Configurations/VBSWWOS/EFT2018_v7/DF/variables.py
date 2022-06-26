# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

#gROOT.ProcessLineSync('.L m4l.C+')
#gROOT.ProcessLineSync('.L mucca.C+')
#gROOT.ProcessLineSync('initMyReader()')

variables['events']  = {   'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                         'fold' : 0
                        }

variables['ptll']  = {   'name': 'ptll',            #   variable name    
                        'range' : (10,30,400),    #   variable range
                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,50,400),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['mjj']  = {   'name'  : 'mjj',            #   variable name    
                        'range' : ([500, 750., 1000., 1500., 2000., 3000],),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold'  : 3,
                        # 'blind' : {
                        #     'VBS_2j_em_me_lowZ' : [1800,3000],
                        #     'VBS_2j_em_me_highZ' : [1800,3000],
                        #     'top_2j_em_me' : [1800,3000],
                        #     'dycr_2j_em_me' : [1800,3000],
                        #   }
                        }

variables['detajj']  = {   'name': 'detajj',            #   variable name    
                           'range' : (8,2.5,6.5),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' : 3
                           }


variables['Zepp_1l']  = {  'name': 'Lepton_eta[0]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (8,-4,4),    #   variable range
                           'xaxis' : 'Z 1st lepton',  #   x axis name
                           'fold' :3
                           }

variables['Zepp_2l']  = {  'name': 'Lepton_eta[1]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (8,-4,4),    #   variable range
                           'xaxis' : 'Z 2nd lepton',  #   x axis name
                           'fold' :3
                           }

variables['pt_1l']  = {   'name': 'Lepton_pt[0]',            #   variable name    
                        'range' : (5,50,200),    #   variable range
                        'xaxis' : 'pT 1st lepton [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['pt_2l']  = {   'name': 'Lepton_pt[1]',            #   variable name    
                        'range' : (5,50,200),    #   variable range
                        'xaxis' : 'pT 2nd lepton [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['eta_1l']  = {   'name': 'Lepton_eta[0]',            #   variable name    
                        'range' : (8,-4,4),    #   variable range
                        'xaxis' : '#eta 1st lepton',  #   x axis name
                        'fold' :3
                        }

variables['eta_2l']  = {   'name': 'Lepton_eta[1]',            #   variable name    
                        'range' : (8,-4,4),    #   variable range
                        'xaxis' : '#eta 2nd lepton',  #   x axis name
                        'fold' :3
                        }


variables['PuppiMET_pt']  = {   'name': 'PuppiMET_pt',            #   variable name    
                        'range' : (5,20,300),    #   variable range
                        'xaxis' : 'MET [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['pt_1j']  = {   'name': 'CleanJet_pt[0]',            #   variable name    
                        'range' : (5,30,300),    #   variable range
                        'xaxis' : 'pT 1st jet [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['pt_2j']  = {   'name': 'CleanJet_pt[1]',            #   variable name    
                        'range' : (5,30,300),    #   variable range
                        'xaxis' : 'pT 2nd jet [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['eta_1j']  = {   'name': 'CleanJet_eta[0]',            #   variable name    
                        'range' : (8, -4, 4),    #   variable range
                        'xaxis' : '#eta 1st jet',  #   x axis name
                        'fold' :3
                        }

variables['eta_2j']  = {   'name': 'CleanJet_eta[1]',            #   variable name    
                        'range' : (8, -4, 4),    #   variable range
                        'xaxis' : '#eta 2nd jet',  #   x axis name
                        'fold' :3
                        }
