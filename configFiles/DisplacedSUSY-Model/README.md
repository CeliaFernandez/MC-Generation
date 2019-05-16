# Displaced SUSY Samples (2016 campaign)

## Generation

SUSY samples are generated with Pythia 8 using the CMSSW_8_0_20_patch1 release.

**Installation and execution**

The CMSSW release and the workdir are initiallized as follows:

```
cmsrel CMSSW_8_0_20_patch1

cd CMSSW_8_0_20_patch1/src

cmsenv

mkdir Generation_Folder

cd Generation_Folder
```

To generate the samples copy the ```'DisplacedSUSY_squarkToQuarkChi_MSquark_1500_MChi_494_ctau_160mm_TuneCP2_13TeV_pythia8_80X_cff.py'``` file inside the Analysis_Folder. Notice that the number of generated events and/or the output file name may need to be modified. Then, execute with:

```
cmsRun DisplacedSUSY_squarkToQuarkChi_MSquark_1500_MChi_494_ctau_160mm_TuneCP2_13TeV_pythia8_80X_cff.py
```

## DRPremix (2 steps)

DRPremix samples are generated in a 2-step workflow with the CMSSW_8_0_21 release.

** Installation and execution**

The CMSSW release and the workdir are initiallized as follows:

```
cmsrel CMSSW_8_0_21

cd CMSSW_8_0_21/src

cmsenv

mkdir DRPremix_Folder

cd DRPremix_Folder
```

To execute the first step it is necessary to change the input files in ```DisplacedSUSY_RunIISummer16DR80Premix_step1_cfg.py``` to the output files generated in the Generation step. To process all the events of these files set -1 in the number of MaxEvents that are generated. The execution command is:


```
cmsRun DisplacedSUSY_RunIISummer16DR80Premix_step1_cfg.py
```

For the second step it is necessary to take the input produced by this last step and modify the ```DisplacedSUSY_RunIISummer16DR80Premix_cfg.py``` accordingly. The execution command is:

```
cmsRun DisplacedSUSY_RunIISummer16DR80Premix_cfg.py
```

## MiniAOD

MiniAOD samples are generated using the CMSSW_9_4_9 release.

** Installation and execution**

The CMSSW release and the workdir are initiallized as follows:

```
cmsrel CMSSW_9_4_9

cd CMSSW_9_4_9/src

cmsenv

mkdir MiniAOD_Folder

cd MiniAOD_Folder
```

After defining the input files in ```DisplacedSUSY_RunIISummer16MiniAODv3_cfg.py``` with the output files of the DPPremix production, the command is 

```
cmsRun DisplacedSUSY_RunIISummer16MiniAODv3_cfg.py
```
