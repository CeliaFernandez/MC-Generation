# Instructions

First install the CMSSW_9_3_18 release, used to generate this model <strong>with a slc6 architecture</strong>:

```
export SCRAM_ARCH=slc6_amd64_gcc630

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_18/src ] ; then
  echo release CMSSW_9_3_18 already exists
else
  scram p CMSSW CMSSW_9_3_18
fi
cd CMSSW_9_3_18/src
eval `scram runtime -sh`
```

Then we just have to generate the fragment of the mass point we just want to produce e.g. 50000 events with mH = 400 GeV, mX = 50 GeV and ctau = 1 mm:

```
python generator_TuneCUEP8M1.py -n 50000 -H 400 -X 50 -T 1
```

This command will produce the corresponding fragment in the ```Configuration/GenProduction/python/``` directory. The example fragment is then:

```
Configuration/GenProduction/python/NLO_HToSSTo4l_MH_400_MS50_ctauS1_13TeV.py
```


The configuration file is created by running the following ```cmsDriver.py``` command:

```
SEED=$(($(date +%s) % 100 + 1))

cmsDriver.py Configuration/GenProduction/python/NLO_HToSSTo4l_MH_400_MS50_ctauS1_13TeV.py --python_filename EXO-RunIIFall17wmGS_400_50_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:EXO-RunIIFall17wmGS.root --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 10;
```

## Crab launching

To create the crab file just init crab3 standalone <strong>without any previous crab3 configuration set</strong> with a valid proxy:
```
source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
voms-proxy-init --voms cms
```

and run the command:

```
python create-crab.py -n 50000 -s 50 -c EXO-RunIIFall17wmGS-400_50_1_cfg.py -H 400 -X 50 -T 1
```


