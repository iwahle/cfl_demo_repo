# Results
Creating a `cfl.Experiment` will create directory called `experiment000x` to
store results. The location for this directory can be set during `Experiment`
initialization. You can set this path to point to this `results` directory.
If you plan on doing several variations of the CFl analysis, I would suggest
creating sub-directories here:

```
- results
    - cfl_analysis_1
        - experiment0000
            - <results will be automatically saved here>
        - experiment0001
            - - <results will be automatically saved here>
        - ...
    - cfl_analysis_2
        - experiment0000
            - <results will be automatically saved here>
        - experiment0001
            - - <results will be automatically saved here>
        - ...
    - ...
```

In this case, when running a "cfl_analysis_2" pipeline, pass 
`results/cfl_analysis_2` as the `cfl.Experiment` `save_path` argument. 

