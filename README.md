# Data Science Challenge: Generative Modeling of Self-Exciting Processes
##### Authors : Lucas Morisset, Danilo Fernandes, Frederico Testa, Omar Elkhalifi, Sébastion Vol, Cyprien Raffi

# Project presentation

In this challenge, we focus on predicting self-exciting random point processes, with a particular application to earthquake prediction and simulation. The challenge is divided into two independent parts:

- **First part:** The initial task is a regression task, where participants are asked to predict earthquakes in Japan using information from only the previous five earthquakes. Given that earthquakes have a self-exciting nature (i.e., one earthquake can trigger another), the task involves extracting statistical information from the timing and location of previous earthquakes. This first part is fully compatible with the Ramp framework.

- **Second part:** The subsequent task is a generative model task. Participants are required to develop a generative framework (i.e., an earthquake simulation procedure) that best reproduces the real earthquakes' self-exciting behavior. Unfortunatly, this wasn't implemented in the Ramp framework.

# RAMP starting-kit earthquakes predictions
Prediction of time and magnitude of earthquakes using a generative model trained on data of Japanese earthquakes

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, a `environment.yml` file is provided for similar
usage.

### Challenge description

TO get started: all information on the challenge, the dataset, the goals and the evaluation metrics can be found in the [dedicated notebook](starting_kit.ipynb). 

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)