#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class misID_sf_mc : public multidraw::TTreeFunction {
public:
  misID_sf_mc();

  char const* getName() const override { return "misID_sf_mc"; }
  TTreeFunction* clone() const override { return new misID_sf_mc(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nLepton;
  // FloatArrayReader* Lepton_pdgId;
  IntArrayReader* Lepton_pdgId;  // mod by D.B. due to error "The branch Lepton_pdgId contains data of type int. It cannot be accessed by a TTreeReaderArray<float>"
  FloatArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;

  //UIntValueReader* nGenJet;
  //FloatArrayReader* GenJet_pt;
  //FloatArrayReader* GenJet_eta;
  //FloatArrayReader* GenJet_phi;
  //FloatArrayReader* GenJet_mass;

  //FloatValueReader* GenMET_pt;
  //FloatValueReader* GenMET_phi;
};

misID_sf_mc::misID_sf_mc() :
  TTreeFunction()
{
}

double
misID_sf_mc::evaluate(unsigned)
{
  unsigned nL{*nLepton->Get()};
  if (nL < 2)
    return 0.;

  // more lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;
    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 2)
    return 0.; // false
  if (iPromptL.size() > 2){
    if (Lepton_pt->At(iPromptL[2])>10){
        return 0;
    }
  }
  if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1])!= -11*11)   //minus sign corrected  ( we want to apply the weight to os ee)
    return 0.;
  
  double chargeflip_rate[3]   = {5.53316e-05,3.72575e-04,1.14568e-03};
  double chargeflip_rate_MC[3]= {4.65073e-05,2.44799e-04,9.31889e-04};
  //double sf[3]={1.18974,1.52196,1.22942};
  int idx1=0;
  int idx2=0;
  if(abs(Lepton_eta->At(iPromptL[0]))>=0 && abs(Lepton_eta->At(iPromptL[0]))<1.0){
    idx1=0;
  }else if(abs(Lepton_eta->At(iPromptL[0]))>=1.0 && abs(Lepton_eta->At(iPromptL[0]))<1.5){
    idx1=1;
  }else if(abs(Lepton_eta->At(iPromptL[0]))>=1.5 && abs(Lepton_eta->At(iPromptL[0]))<2.5){
    idx1=2;
  }

  if(abs(Lepton_eta->At(iPromptL[1]))>=0 && abs(Lepton_eta->At(iPromptL[1]))<1.0){
    idx2=0;
  }else if(abs(Lepton_eta->At(iPromptL[1]))>=1.0 && abs(Lepton_eta->At(iPromptL[1]))<1.5){
    idx2=1;
  }else if(abs(Lepton_eta->At(iPromptL[1]))>=1.5 && abs(Lepton_eta->At(iPromptL[1]))<2.5){
    idx2=2;
  }

  //double _sf1=sf[idx1];
  //double _sf2=sf[idx2];
  // compute chargeflip measured on DATA
//   double _rate1=chargeflip_rate[idx1];
//   double _rate2=chargeflip_rate[idx2];
  // compute chargeflip measured on MC
  double _rate1=chargeflip_rate_MC[idx1];
  double _rate2=chargeflip_rate_MC[idx2];
  
  double mis_id_sf= _rate1*(1-_rate2)+(1-_rate1)*_rate2;
  return mis_id_sf;
}

void
misID_sf_mc::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");

  //_library.bindBranch(nGenJet, "nGenJet");
  //_library.bindBranch(GenJet_pt, "GenJet_pt");
  //_library.bindBranch(GenJet_eta, "GenJet_eta");
  //_library.bindBranch(GenJet_phi, "GenJet_phi");
  //_library.bindBranch(GenJet_mass, "GenJet_mass");

  //_library.bindBranch(GenMET_pt, "GenMET_pt");
  //_library.bindBranch(GenMET_phi, "GenMET_phi");
}