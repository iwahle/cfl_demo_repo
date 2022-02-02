# cfl_demo_repo
An example of how to set up a repository that uses `cfl`!

`cfl` is a software package that learns high-level "macrovariables" from
fine-grained data measurements. To learn more, please take a look at the CFL
[repository](https://github.com/eberharf/cfl) and 
[documentation](https://cfl.readthedocs.io/en/latest/).


## Getting started
To use this template, click on "Use this template" above and follow the
prompts. You can then clone your new repository to your local machine by
copying the URL revealed by the "Code" button on your repository home page
and running 
```
git clone <repository URL>
```
in your local terminal. 


To create a conda env that has the packages needed to run CFL demos in the 
docs, first [make sure you have anaconda installed]
(https://docs.anaconda.com/anaconda/install/index.html), then:

```
cd <path to your newly cloned repository>
conda env create -f requirements.yml
conda activate cfl-env
```

If you would like to run CFL in a Jupyter notebook, you will need to make
this environment available to jupyter: 

```
python -m ipykernel install --user --name=cfl-env
```

Once you open your jupyter notebook, make sure "cfl-env" is selected as
your kernel.

You should now be ready to run your first CFL experiment!