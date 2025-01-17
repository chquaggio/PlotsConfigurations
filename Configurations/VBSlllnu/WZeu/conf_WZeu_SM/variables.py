# variables

# variables = {}

# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['nJet'] = {
    'name'  : 'Sum$(CleanJet_pt>30)',
    'range' : (4,0,4),
    'xaxis' : 'njets',
    'fold'  : 3
}

variables['mll'] = {
    'name'  : 'mll',
    'range' : (10,20.,300),
    'xaxis' : 'mll [GeV]',
    'fold'  : 3
}

variables['mllZ'] = {
    'name'  : 'wzeu_var[1]',
    'range' : (5,80.,100),
    'xaxis' : 'mll Z [GeV]',
    'fold'  : 3
}

variables['mee'] = {
    'name'  : 'wzeu_var[0]',
    'range' : (5,80.,100),
    'xaxis' : 'mee [GeV]',
    'fold'  : 3
}

variables['ptl1'] = {
    'name'  : 'Alt$(Lepton_pt[0],-9999.)',
    'range' : (15,30,350),
    'xaxis' : 'p_{T} 1st lep [GeV]',
    'fold'  : 3
}

variables['ptl1Z'] = {
    'name'  : 'wzeu_var[3]',
    'range' : (15,25,350),
    'xaxis' : 'p_{T} 1st lep Z [GeV]',
    'fold'  : 3
}

variables['ptl2'] = {
    'name'  : 'Alt$(Lepton_pt[1],-9999.)',
    'range' : (15,20,200),
    'xaxis' : 'p_{T} 2nd lep [GeV]',
    'fold'  : 3
}

variables['ptl2Z'] = {
    'name'  : 'wzeu_var[4]',
    'range' : (10,10,100),
    'xaxis' : 'p_{T} 2nd lep Z [GeV]',
    'fold'  : 3
}


variables['ptl3'] = {
    'name'  : 'Alt$(Lepton_pt[2],-9999.)',
    'range' : (10,10,100),
    'xaxis' : 'p_{T} 3rd lep [GeV]',
    'fold'  : 3
}

variables['ptlW'] = {
    'name'  : 'wzeu_var[5]',
    'range' : (10,10,150),
    'xaxis' : 'p_{T} lep W [GeV]',
    'fold'  : 3
}

variables['etal1'] = {
    'name'  : 'Alt$(Lepton_eta[0],-9999.)',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep1',
    'fold'  : 3
}

variables['etal1Z'] = {
    'name'  : 'wzeu_var[6]',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep1 Z',
    'fold'  : 3
}

variables['etal2'] = {
    'name'  : 'Alt$(Lepton_eta[1],-9999.)',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep2',
    'fold'  : 3
}

variables['etal2Z'] = {
    'name'  : 'wzeu_var[7]',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep2 Z',
    'fold'  : 3
}

variables['etal3'] = {
    'name'  : 'Alt$(Lepton_eta[2],-9999.)',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep3',
    'fold'  : 3
}

variables['etalW'] = {
    'name'  : 'wzeu_var[8]',
    'range' : (10,-2.,2.),
    'xaxis' : 'eta lep W',
    'fold'  : 3
}

variables['mjj'] = {
    'name'  : 'mjj',
    'range' : ([400,700,1000,1300,1600,2000,2500,3000],),
    'xaxis' : 'mjj [GeV]',
    'fold'  : 3
}

variables['ptj1'] = {
    'name'  : 'Alt$(CleanJet_pt[0],-9999.)',
    'range' : (8,50,450),
    'xaxis' : 'p_{T} 1st jet [GeV]',
    'fold'  : 3
}

variables['ptj2'] = {
    'name'  : 'Alt$(CleanJet_pt[1],-9999.)',
    'range' : (8,35,200),
    'xaxis' : 'p_{T} 2nd jet [GeV]',
    'fold'  : 3
}

variables['etaj1'] = {
    'name'  : 'Alt$(CleanJet_eta[0],-9999.)',
    'range' : (10,-5,5),
    'xaxis' : 'eta j1',
    'fold'  : 3
}

variables['etaj2'] = {
    'name'  : 'Alt$(CleanJet_eta[1],-9999.)',
    'range' : (10,-5,5),
    'xaxis' : 'eta j2',
    'fold'  : 3
}

variables['detajj'] = {
    'name'  : 'detajj',
    'range' : ([1.5,1.75,2,2.25,2.5,2.75,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5],),
    'xaxis' : 'deta jj',
    'fold'  : 3
}

variables['dphijj'] = {
    'name'  : 'dphijj',
    'range' : (5,0.0,3.141592),
    'xaxis' : 'dphi jj',
    'fold'  : 3
}

variables['met'] = {
    'name'  : 'MET_pt',
    'range' : (10,20,200),
    'xaxis' : 'met [GeV]', 
    'fold'  : 3
}

variables['Zlep1'] = {
    'name'  : 'zlep1',
    'range': ([-1,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,1.],),
    'xaxis' : 'Z^{lep}_{1}',
    'fold'  : 3
}

variables['Zlep2'] = {
    'name': 'zlep2',
    'range': ([-1,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,1.],),
    'xaxis': 'Z^{lep}_{2}',
    'fold': 3
}
