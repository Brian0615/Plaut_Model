# Results

### May 02-03, 2020
> #### Base Simulation
> * **Description**: Set of simulations including all major changes since the Jan 21, 2020 simulations (i.e. the ones used for the Feb 2020 paper.
> * **Simulation Folder**: `BASE-may02-03`

### Mar 30, 2020
> #### All Combinations of Graphemes
> * **Description**: Testing Results of all possible words+nonwords composed of one onset, one vowel, and one coda
> * **Simulation Folder**: `ALLCOMB-mar30`
> * `results.csv`: 1) most active onset/vowel/coda for each word; 2) unit activity for most active phonemes; 3) entropy
> * `model_outputs.csv`: original output values from model
> * `entropy.csv`: entropy values based on original output values, calculated using the formula `S = p*log2(p) + (1-p)*log2(1-p) - log2(0.5)`


### Mar 03-04, 2020
> #### Frequency/Dilution Tests
> * **Description**: Simulations crossing 3 dilution levels with 3 frequency levels
> * **Simulation Folders**: `FREQTESTXX-S1DYO1-mar0Z` inside the `FREQTEST-mar03-04` directory
> * **`.gz` files**: inside `FREQTEST-mar03-04` directory, and also inside simulation folders, with format
`warping-dilation-FREQTESTXX-S1DYO1-mar0Z.csv.gz`
> * **Note**: `XX = {10, 20, 30}` for frequency level; `Y = {1, 2, 3}` for dilution level; `Z = {3, 4}` for date


### Feb 24-26, 2020
> #### Base Simulation
> * **Description**: "Base" simulation after updating loss calculations (i.e. removing scaling down of loss)
> * **Simulation Folders**: `BASE-SXDXOX-feb2X` inside the `BASE-feb24-26` directory
> * **`.gz` files**: inside `BASE-feb24-26` directory, and also inside simulation folders, with format
`warping-dilation-BASE-SXDXOX-feb2X.csv.gz`

### Notes
> * For simulations run after Feb 20, 2020, a simulation specific "label" will be used to distinguish unique simulations.
> * As a result, simulation folders will be named with the following format: `<label>-SXDXOX-<date>` where `X` is a placeholder for random seed, dilation, and anchor order.
> * `.gz` files will be named with the following format:
`warping-dilation-<label>-S<seed>D<dilation>O<order>-<date>.csv.gz`
> * For sets of simulations, the simulations will be placed in a directory with format:
`/results/<label>-<date>`

### Feb 20, 2020
> #### Base Simulation
> * **Description**: "Base" simulation for comparison purposes - essentially identical to the ones in the Feb 2020 paper, with the exception of resetting Adam after adding anchors
> * **Simulation Folders**: `BASE-SXDXOX-feb20` inside the `BASE-feb20` directory
> * **`.gz` files**: inside `BASE-feb20` directory, and also inside simulation folders, with format
`warping-dilation-BASE-SXDXOX-feb20.csv.gz`

> #### Fixed Plaut Frequency
> * **Description**: Frequency for Plaut dataset is kept unchanged (instead of replacing with `ln(2)`) after the anchors are added
> * **Simulation Folders**: `FPF-SXDXOX-feb20` inside the `FPF-feb20` directory
> * **`.gz` files**: inside `FPF-feb20` directory, and also inside simulation folders, with format
`warping-dilation-FPF-SXDXOX-feb20.csv.gz`

### Feb 19, 2020
> #### Frequency Test A
> * **Description**: Simulations with frequency calculated as `ln(10/N+2)`
> * **Simulation Folders**: feb19_test04 to feb19_test06 inside /FREQTEST-jan19
> * **`.gz` files**: inside simulation folders, with format `warping-dilation-FREQTESTA-S<seed>D<dilation>O<order>FEB19.csv.gz`

> #### Frequency Test B
> * **Description**: Simulations with frequency calculated as `ln(10+2)/N`
> * **Simulation Folders**: feb19_test01 to feb19_test03 inside /FREQTEST-jan19
> * **`.gz` files**: inside simulation folders, with format `warping-dilation-FREQTESTB-S<seed>D<dilation>O<order>FEB19.csv.gz`

> #### Frequency Test C
> * **Description**: Simulations with only anchor 1, and frequencies `ln(10+2)`, `ln(5+2)`, `ln(3.33+2)`
> * **Simulation Folders**: feb19_test07 to feb19_test09 inside /FREQTEST-jan19
> * .gz files: inside simulation folders, with format `warping-dilation-FREQTESTC-S<seed>D<dilation>O<order>FEB19.csv.gz`

> #### Notes
>    * `<seed> = {1}` indicates random number generator seed
>    * `<dilation> = {1, 2, 3}` indicates N, N/2, N/3 dilation for Frequency Tests A and B
>    * `<dilation> = {0, 5, 3}` indicates `ln(10+2)`, `ln(5+2)`, `ln(3.33+2)` respectively for Frequency Test C
>    * `<order> = {1}` indicates starting anchor set
>    * **Typo**: For Frequency Test C, order is shown as 3 in the title and inside the csv file. This is a typo; order should be 1.


### Notes
> * For simulations run after Feb 05, 2020, the Adam optimizer is reset after the anchors are added.

### Feb 05, 2020
> * **Description**: Individual anchor simulations from anchors_new1.csv
> * **Simulation Folders**: `feb05_test01` to `feb05_test27` inside `/results/single_anchor`
> * **`.gz` files**: inside `results/single_anchor`, named: `warping-dilation-<anchor>.csv.gz`
>    * `<anchor>` is the orthography of the anchor

### Jan 21, 2020
 > * **Description**: Simulation results used in Feb 2020 paper
 > * **Simulation Folders**: `jan21_test01` to `jan21_test10`, inside `/results/PAPER-jan21`
 > * **`.gz` files**: `warping-dilation-seed-<seed>-dilation-<dilation>-order-<order>-date-jan21.csv.gz`
 >    * `<seed> = {1, 2}` indicates random number generator seed
 >    * `<dilation> = {1, 2, 3}` indicates N, N/2, N/3 dilation
 >    * `<order> = {1, 3}` indicates starting anchor set
     

