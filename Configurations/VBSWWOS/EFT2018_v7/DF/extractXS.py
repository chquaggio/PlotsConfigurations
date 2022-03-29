import ROOT
import sys
import glob
import os

rwgts = {
    'rwgt_sm' : 'LHEReweightingWeight[0]',
    'rwgt_cHl3_LI' : '0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1])',
    'rwgt_cHl3_QU' : '0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2*LHEReweightingWeight[0])',
    'rwgt_cHq3_LI' : '0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3])',
    'rwgt_cHq3_QU' : '0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2*LHEReweightingWeight[0])',
    'rwgt_cqq31_LI' : '0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5])',
    'rwgt_cqq31_QU' : '0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2*LHEReweightingWeight[0])',
    'rwgt_cqq3_LI' : '0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7])',
    'rwgt_cqq3_QU' : '0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2*LHEReweightingWeight[0])',
    'rwgt_cll1_LI' : '0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9])',
    'rwgt_cll1_QU' : '0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2*LHEReweightingWeight[0])'
}

if len(sys.argv)<2:
    print("Specify nAOD folder")
    sys.exit(1)

folder = sys.argv[1]
roots = sorted(glob.glob(folder + "/WWjjTolnulnu_OS_DF_ewk_dim6_5op_*/WWjjTolnulnu_OS_DF_ewk_dim6_5op_*.root"))
Xss_calc = []
Xss_done = []
# ch_ev = ROOT.TChain("Events")
# ch_ru = ROOT.TChain("Runs")
# i = 0
# for root in roots :
#     ch_ev.Add(root)
#     ch_ru.Add(root)
#     if i % 500 == 0 :
#         print("Processed {} nAODs".format(i))
#     i += 1
i=0
print("Initializating RDataFrames..")

for root in roots :
    df_ru = ROOT.RDataFrame("Runs", root)
    df_ev = ROOT.RDataFrame("Events", root)

    df_done = df_ru.Define('rwgt_sm', 'LHEReweightingSumw[0]')
    Xss_done.append(df_done.Mean('rwgt_sm').GetValue())

    df_calc = df_ev.Define('rwgt_sm', 'genWeight*'+rwgts['rwgt_sm'])
    n_ev = df_ru.Mean('genEventSumw').GetValue()
    Xss = df_calc.Sum('rwgt_sm').GetValue()/n_ev
    Xss_calc.append(Xss)
    if i % 100 == 0 :
        print("Processed {} nAODs out of {}".format(i, len(roots)))
    i += 1

print('cross section for LHEReweightingSumw method is: {}'.format(sum(Xss_done)/len(Xss_done)))
print('cross section for genWeight*LHEReweightingWeight method is: {}'.format(sum(Xss_calc)/len(Xss_calc)))
