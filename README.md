# cfl_demo_repo
An example of how to set up a repository that uses CFL!

To create a conda env that has the packages needed to run CFL demos in the 
docs, run:

```
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