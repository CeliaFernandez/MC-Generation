# Instructions

First install the CMSSW_7_1_46 release, used to generate this model <strong>with a slc6 architecture</strong>:

```
export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_46/src ] ; then
  echo release CMSSW_7_1_46 already exists
else
  scram p CMSSW CMSSW_7_1_46
fi
cd CMSSW_7_1_46/src
eval scram runtime -sh

```

Then we just have to generate the fragment of the mass point we just want to produce e.g. 50000 events with mH = 125 GeV, mX = 30 GeV and ctau = 10 mm:

```
python generator_TuneCUEP8M1.py -n 50000 -H 125 -X 30 -T 10
```

This command will produce the corresponding fragment in the ```Configuration/GenProduction/python/``` directory. The example fragment is then:

```
Configuration/GenProduction/python/NLO_HToSSTo4l_MH_125_MS30_ctauS10_13TeV.py
```


The configuration file is created by running the following ```cmsDriver.py``` command:

```
SEED=$(($(date +%s) % 100 + 1))

cmsDriver.py Configuration/GenProduction/python/NLO_HToSSTo4l_MH_125_MS30_ctauS10_13TeV.py --python_filename EXO-RunIISummer15wmGS-125_30_10_cfg.py --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:EXO-RunIISummer15wmGS-10015.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --magField 38T_PostLS1 --no_exec --mc -n 10
```

## Crab launching

To create the crab file just init crab3 standalone <strong>without any previous crab3 configuration set</strong> with a valid proxy:
```
source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
voms-proxy-init --voms cms
```

and run the command:

```
python create-crab.py -n 50000 -s 50 -c EXO-RunIISummer15wmGS-125_30_10_cfg.py -H 125 -X 30 -T 10
```


