### Main


## Data Managment Backbone
# landing
from DataManagmentBackbone.landing.landing import executeLanding
from DataManagmentBackbone.landing.data_discovery import executeDataDiscovery
from DataManagmentBackbone.landing.landing import Wrapper

# formatted
from DataManagmentBackbone.formatted.processes.formatted import executeformatted
from DataManagmentBackbone.formatted.processes.formmated_infodb import describeFormattedDB

# trusted
from DataManagmentBackbone.trusted.processes.combine_versions import execute_combine_versions
from DataManagmentBackbone.trusted.processes.data_quality.missing import executeMissingData
from DataManagmentBackbone.trusted.processes.data_quality.outliers import execute_outliers
from DataManagmentBackbone.trusted.processes.data_quality.profiling import execute_profiling
from DataManagmentBackbone.trusted.processes.trusted_infodb import describeTrustedDB

# explotation
from DataManagmentBackbone.explotation.processes.explotation import execute_explotation
from DataManagmentBackbone.explotation.processes.dataintegration import execute_dataIntegration
from DataManagmentBackbone.explotation.processes.tablerenaming import execute_tablerenaming
from DataManagmentBackbone.explotation.processes.explotation_infodb import describeExplotationDB


## Data Analysis Backbone
# analyticalsandbox
from DataAnalysisBackbone.Influential_Indicators_Analytic.analyticsandbox.processes.analytic_sandbox import execute_analytical_sandbox

# feature generation
from DataAnalysisBackbone.Influential_Indicators_Analytic.feature_generation.processes.featuregeneration import execute_feature_generation
from DataAnalysisBackbone.Influential_Indicators_Analytic.feature_generation.processes.profiling_datasets import execute_profiling_datasets

# model training
from DataAnalysisBackbone.Influential_Indicators_Analytic.model_training.processes.model_preparation import  execute_model_preparation
from DataAnalysisBackbone.Influential_Indicators_Analytic.model_training.processes.model_validation import execute_model_validation, show_model_feature_importance
from DataAnalysisBackbone.Influential_Indicators_Analytic.deployment.model_deployment import deploy_model


# teting
from unittest import TestLoader, TestResult
from pathlib import Path

# additional
import os
import shutil
import webbrowser
from tkinter.filedialog import askopenfilename


def menu_options():
    DMDone = os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/explotation/storage/explotation.duckdb')))

    print("\n\n\n ============= MENU OPTIONS =============\n")

    print("0. Add a new datasource from World Data Bank")
    print("1. Execute DMBackbone")
    print("2. Add a new datasource to landing zone (file)")
    print("3. Show databases")
    print("4. Produce profiling reports (open in default browser)")
    print("5. Clean the DMBackbone")
    if DMDone:
        print("6. Execute DABackbone")
        print("7. Generate profiling reports for train and test datasets")
        print("8. Validate existing models")
        print("9. Deploy existing models")
        print("10. Show models indicators importances")
    else:
        print("Execute DMBackbone to see more options!")
    print("11. Testing")
    print("12. Exit")




    option = input("\nSelect a option (number): ")

    if option.isdigit():
        option = int(option)
        if not DMDone:
            if option > 5 and option <11:
                option = 9999

    return str(option)


### Execute
print(r"""\

██╗███╗   ██╗███████╗██╗     ██╗   ██╗███████╗███╗   ██╗████████╗██╗ █████╗ ██╗          ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗██████╗ ██╗   ██╗    
██║████╗  ██║██╔════╝██║     ██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║██╔══██╗██║         ██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝    
██║██╔██╗ ██║█████╗  ██║     ██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║███████║██║         ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝     
██║██║╚██╗██║██╔══╝  ██║     ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██║██╔══██║██║         ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝      
██║██║ ╚████║██║     ███████╗╚██████╔╝███████╗██║ ╚████║   ██║   ██║██║  ██║███████╗    ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██║  ██║   ██║       
╚═╝╚═╝  ╚═══╝╚═╝     ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝       

██╗███╗   ██╗██████╗ ██╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ ███████╗    ██╗███╗   ██╗               .,::OOO::,.     .,ooOOOoo,.     .,::OOO::,.                                                
██║████╗  ██║██╔══██╗██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝    ██║████╗  ██║              .:'         `:. .8'         `8. .:'         `:.                                                  
██║██╔██╗ ██║██║  ██║██║██║     ███████║   ██║   ██║   ██║██████╔╝███████╗    ██║██╔██╗ ██║              :"           ": 8"           "8 :"           ":                                                 
██║██║╚██╗██║██║  ██║██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗╚════██║    ██║██║╚██╗██║              :,        .,:::""::,.     .,:o8OO::,.        ,:                                                 
██║██║ ╚████║██████╔╝██║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║███████║    ██║██║ ╚████║               :,,    .:' ,:   8oo`:. .:'oo8   :,,`:.    ,,:                                                 
╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝                `^OOoo:"O^'     `^88oo:"8^'     `^O":ooOO^'                                                  
                                                                                                               :,           ,: :,           ,:                                          
████████╗██╗  ██╗███████╗     ██████╗ ██╗  ██╗   ██╗███╗   ███╗██████╗ ██╗ ██████╗███████╗                      :,,       ,,:   :,,       ,,:                                          
╚══██╔══╝██║  ██║██╔════╝    ██╔═══██╗██║  ╚██╗ ██╔╝████╗ ████║██╔══██╗██║██╔════╝██╔════╝                        `^Oo,,,oO^'     `^OOoooOO^'                                        
   ██║   ███████║█████╗      ██║   ██║██║   ╚████╔╝ ██╔████╔██║██████╔╝██║██║     ███████╗                                                               
   ██║   ██╔══██║██╔══╝      ██║   ██║██║    ╚██╔╝  ██║╚██╔╝██║██╔═══╝ ██║██║     ╚════██║                       Authors: Achraf Hmimou &                                          
   ██║   ██║  ██║███████╗    ╚██████╔╝███████╗██║   ██║ ╚═╝ ██║██║     ██║╚██████╗███████║                                    Aniol Bisquert                            
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝   ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝╚══════╝                                              v0.1
                                                                                                                      x                                                                                                 
    """)

# relative path
dirname = os.path.dirname(__file__)
DMDone = False

while True:
    option = menu_options()
    if option.isdigit():
        # Execute the different zones of the DMBackbone pipeline

        if int(option) == 0:
            print("\n\n...Select a data source from World Data Bank to add...")
            executeDataDiscovery()

        if int(option) == 1:
            print("\n\n...Executing Landing Zone")
            executeLanding()
            print("...Executing Formatted Zone")
            executeformatted()
            # Trusted
            print("...Executing Trusted Zone")
            print("......Combining versions")
            execute_combine_versions()
            print("......Missing data treatment")
            executeMissingData()
            print("......Outlier removal treatment")
            execute_outliers()
            # explotation
            print("...Executing Exploitation Zone")
            print("......Moving data to explotation zone")
            execute_explotation()
            print("......Table renaming")
            execute_tablerenaming()
            # execute_tablepivoting()
            print("......Data Integration")
            execute_dataIntegration()
            print("\n\nDone!")
            print("\nDMBackbone is up to date! :-)")
            DMDone = True
        # Add a new Datasource to landing zone
        elif int(option) == 2:
            print("Please select a new datasource  (csv file): ")
            # nds_path = input()
            try:
                nds_path = askopenfilename()
                # csv file mandatory
                if os.path.exists(nds_path) and nds_path.endswith('.csv'):
                    wrapper = Wrapper()
                    wrapper.addNewDatasource(nds_path)
                    print("Datasource added to landing zone! Execute the DMBackbone to update the zones")
                else:
                    print("\n\nInvalid datasource. Please, introduce a valid datasource.")
            except:
                print("Something went wrong! Please select a valid datasource.")

        # Database schema description
        elif int(option) == 3:
            print("Select a zone: ")
            print("1  Formatted")
            print("2. Trusted")
            print("3. Explotation")
            zone = input()
            if int(zone) == 1:
                if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/formatted/storage/formatted.duckdb'))):
                    describeFormattedDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            elif int(zone) == 2:
                if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/trusted/storage/trusted.duckdb'))):
                    describeTrustedDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            elif int(zone) == 3:
                if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/explotation/storage/explotation.duckdb'))):
                    describeExplotationDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            else:
                print("Please indicate a valid zone.")

        # Generate profiling reports (open in browser)
        elif int(option) == 4:
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/trusted/storage/trusted.duckdb'))):
                execute_profiling()
                # opening reports in the default browser
                for report in os.listdir(os.path.join(dirname, 'DataManagmentBackbone/trusted/processes/data_quality/profile_reports')):
                    webbrowser.open(os.path.join(dirname, f'DataManagmentBackbone/trusted/processes/data_quality/profile_reports/{report}'),
                                    new=0, autoraise=True)
            else:
                print("No database found. Please, execute the DMBackbone!")


        # clean all files and databases of DMBackbone (except landing zone)
        elif int(option) == 5:

            print("Cleaning landing zone...")
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/landing/persistent'))):
                shutil.rmtree((os.path.join(dirname, 'DataManagmentBackbone/landing/persistent')))
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/landing/wrapper.json'))):
                os.remove((os.path.join(dirname, 'DataManagmentBackbone/landing/wrapper.json')))
            print("Done!")

            print("Cleaning formatted zone...")
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/formatted/storage/formatted.duckdb'))):
                os.remove((os.path.join(dirname, 'DataManagmentBackbone/formatted/storage/formatted.duckdb')))
            print("Done!")

            print("Cleaning trusted zone...")
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/trusted/storage/trusted.duckdb'))):
                os.remove((os.path.join(dirname, 'DataManagmentBackbone/trusted/storage/trusted.duckdb')))
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/trusted/processes/data_quality/profile_reports'))):
                shutil.rmtree((os.path.join(dirname, 'DataManagmentBackbone/trusted/processes/data_quality/profile_reports')))
            print("Done!")

            print("Cleaning exploitation zone...")
            if os.path.exists((os.path.join(dirname, 'DataManagmentBackbone/explotation/storage/explotation.duckdb'))):
                os.remove((os.path.join(dirname, 'DataManagmentBackbone/explotation/storage/explotation.duckdb')))

            DMDone = False
            print("DMBackbone has been cleaned!")


        # Execute Data Analysis Backbone
        elif int(option) == 6:

            # remove databases
            if os.path.exists((os.path.join(dirname, 'DataAnalysisBackbone/influential_indicators_Analytic/analyticalsandbox/storage/sandboxes/olympics_indicators.duckdb'))):
                os.remove((os.path.join(dirname, 'DataAnalysisBackbone/influential_indicators_Analytic/analyticalsandbox/storage/sandboxes/olympics_indicators.duckdb')))

            if os.path.exists((os.path.join(dirname, 'DataAnalysisBackbone/influential_indicators_Analytic/feature_generation/storage/datasets.duckdb'))):
                os.remove((os.path.join(dirname, 'DataAnalysisBackbone/influential_indicators_Analytic/feature_generation/storage/datasets.duckdb')))

            # analytical sandbox
            print("...Executing Analytical Sandbox")
            execute_analytical_sandbox()
            # feature_generation
            print("...Generating Features")
            execute_feature_generation()
            # execute_profiling()
            # model training
            print("...Training Model")
            execute_model_preparation()
            #print("...Validating Model")
            #execute_model_validation()
            #print("...Deploying Model")
            #deploy_model()
        # Profiling reports
        elif int(option) == 7:
            execute_profiling_datasets()
        # Validate existing models
        elif int(option) == 8:
            execute_model_validation()
        # Deploy existing models
        elif int(option) == 9:
            deploy_model()

        #Show models indicators importances
        elif int(option) == 10:
            show_model_feature_importance()


        # testing
        # from user Jesuisme at https://stackoverflow.com/questions/14282783/call-a-python-unittest-from-another-script-and-export-all-the-error-messages
        elif int(option) == 11:

            print("Running tests...")

            test_loader = TestLoader()
            test_result = TestResult()

            # Use resolve() to get an absolute path
            # https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve
            test_directory = str(Path(__file__).resolve().parent / 'testing')

            test_suite = test_loader.discover(test_directory, pattern='test_*.py')
            test_suite.run(result=test_result)

            # See the docs for details on the TestResult object
            # https://docs.python.org/3/library/unittest.html#unittest.TestResult

            if test_result.wasSuccessful():
                print("Unit Tests Passed!")
            else:
                # Here you can either print or log your test errors and failures
                print(test_result.errors)
                # test_result.errors or test_result.failures

        # stop the programm
        elif int(option) == 12:
            break;
        else:
            print("Error: Please, select a valid option")
    else:
        print("Error: Please, select a valid option")

    choice = input('\nPress enter key to show options... ')

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # show options again


