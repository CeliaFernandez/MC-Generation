# Automatic creation of GEN config files

<p>The script 'createConfigFile.py' creates config files from templates of models that contain:</p>
<ul>
  <li> One massive particle with M1 GeV </li>
  <li> Other massive particle with M2 Gev that comes from the decay of the first one and has a decay length of CT (proper frame of the particle) </li>
</ul>


## Instructions

Run the 'createConfigFile.py' config file specifying the config file template, the mass of the particles, the decay length and (optionally) the number of produced events:

```python createConfigFile.py --template [path/to/template] --M1 [M1] --M2 [M2] --CT [CT] (--N [Number of events])```

Note: One template example is available in folder: templates/

## Running example

```python createConfigFile.py --template TEMPLATE_DisplacedSUSY_squarkToQuarkChi_MSquark_M1_MChi_M2_ctau_CTmm_TuneCP2_13TeV_pythia8_80X_cff.py --M1 1000 --M2 148 --CT 60 --N 10```
