### Main

# analyticalsandbox
from analyticsandbox.processes.analytic_sandbox import execute_analytical_sandbox

# feature generation
from feature_generation.processes.featuregeneration import execute_feature_generation

# model training
from model_training.processes.model_preparation import  execute_model_preparation
from model_training.processes.model_validation import execute_model_validation
from DataAnalysisBackbone.Influential_Indicators_Analytic.deployment.model_deployment import deploy_model

import os


def menu_options():
    print("\n\n\n ============= MENU OPTIONS =============\n")
    print("0. Execute Analytical Sandbox")
    print("\nSelect a option (Number between 0-7): ")




# relative path
dirname = os.path.dirname(__file__)

while True: 
    menu_options()
    option = input() 
    if option.isdigit():
        # Execute the different zones of the DMBackbone pipelin
        if int(option) == 0:
            # analytical sandbox
            execute_analytical_sandbox()
            # feature_generation
            execute_feature_generation()
            #execute_profiling()
            # model training
            execute_model_preparation()
            execute_model_validation()
            deploy_model()

    else:
        print("Error: Please, select a valid option (Number between 0-7)")
    
    choice = input('\nPress enter key to show options... ')

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # show options again
        

