# Datapath evaluation tool

Technical evaluation to refactor code developed to create maintainable tool that can be used by other system R&D engineers for evaluation of other datasets and datapaths.

## About the project

R&D system engineers capture camera data and process the through the datapath to obtain the phase image. The phase image is essentially equivalent to depth map and is the valuable output of the system.

A datapath takes as input multiple sensor streams and correction factors (e.g., I stream, Q stream, sensor phase bias) computes phase and may apply some filters.

## Requirements

* Linux
* virtualenv
* python3

## Getting Started

Clone the Repository
As usual, you get started by cloning the project to your local machine:

```bash
git clone git@github.com:moamenibrahim/datapath_evaluation.git
cd datapath_evaluation
```

Create a virtual enviroment in the current project folder using python3

```bash
./init.sh
```

## Authors

* [Moamen Ibrahim](https://github.com/moamenibrahim)
