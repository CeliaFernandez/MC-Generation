# Displaced SUSY Samples

## Generation

SUSY samples are generated with Pythia 8 using the CMSSW_8_0_20_patch1 release.

*Installation and execution*

```
cmsrel CMSSW_8_0_20_patch1

cd CMSSW_8_0_20_patch1/src

cmsenv

mkdir Analysis_Folder

cd Analysis_Folder
```

Then copy the ```'DisplacedSUSY_squarkToQuarkChi_MSquark_1500_MChi_494_ctau_160mm_TuneCP2_13TeV_pythia8_80X_cff.py'``` file inside the Analysis_Folder. Notice that the number of generated events and/or the output file name may need to be modified. Then, execute with:

```
cmsRun 'DisplacedSUSY_squarkToQuarkChi_MSquark_1500_MChi_494_ctau_160mm_TuneCP2_13TeV_pythia8_80X_cff.py'
```

## DRPremix (2 steps)


## MiniAOD
