# Universal-Fitting

## Installing
Following step-by-step instructions will demonstrate how to get a development environment running.

Clone this repository to somewhere convenient.
```
git clone https://github.com/Kiu4/TCSPC-Fit.git
cd TCSPC-Fit
```

Install the conda environment by
```
conda env create -f environment.yml
conda activate tcspcfit-dev
```
this will prepare an environment with required development tools under the name `tcspcfit-dev`.

Since pip does not honor the `setup_requires` description, basic requirements and native libraries are installed using conda in preivous step.

Next, we install this toolbox using editable mode
```
pip install -e .
```

To test the toolbox, run
```
pytest
```
