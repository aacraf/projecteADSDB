#!/bin/bash

import papermill as pm

pm.execute_notebook(
    "./landing/landing.ipynb",
    "./out/landing_out.ipynb",
) 

pm.execute_notebook(
    "./formatted/formatted.ipynb",
    "./out/formatted_out.ipynb",
) 

pm.execute_notebook(
    "./trusted/combine_versions.ipynb",
    "./out/combine_versions_out.ipynb",
)  

""" pm.execute_notebook(
    "./trusted/missing.ipynb",
    "./out/missing_out.ipynb",
)   """
 
pm.execute_notebook(
    "./trusted/outliers.ipynb",
    "./out/outliers_out.ipynb",
) 

pm.execute_notebook(
    "./trusted/profiling.ipynb",
    "./out/profiling_out.ipynb",
)  

pm.execute_notebook(
    "./explotation/explotation.ipynb",
    "./out/explotation_out.ipynb",
)   

pm.execute_notebook(
    "./explotation/tablepivoting.ipynb",
    "./out/tablepivoting_out.ipynb",
) 

pm.execute_notebook(
    "./explotation/dataIntegration.ipynb",
    "./out/dataIntegration_out.ipynb",
) 