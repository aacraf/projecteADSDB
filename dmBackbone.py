### Main

# landing
from landing.landing import executeLanding
from landing.landing import Wrapper

# formatted
from formatted.processes.formatted import executeformatted
from formatted.processes.formmated_infodb import describeFormattedDB

# trusted
from trusted.processes.combine_versions import execute_combine_versions
from trusted.processes.data_quality.missing import executeMissingData
from trusted.processes.data_quality.outliers import execute_outliers
from trusted.processes.data_quality.profiling import execute_profiling
from trusted.processes.trusted_infodb import describeTrustedDB

# explotation
from explotation.processes.explotation import execute_explotation
from explotation.processes.tablepivoting import execute_tablepivoting
from explotation.processes.dataintegration import execute_dataIntegration
from explotation.processes.explotation_infodb import describeExplotationDB


# teting 
from unittest import TestLoader, TestResult
from pathlib import Path

# additional
import os
import shutil
import webbrowser
from tkinter.filedialog import askopenfilename
import time


def menu_options():
    print("\n\n\n ============= MENU OPTIONS =============\n")
    print("1. Execute DMBackbone")
    print("2. Add a new datasource to landing zone")
    print("3. Show databases")
    print("4. Produce profiling reports (open in default browser)")
    print("5. Clean the DMBackbone")
    print("6. Testing")
    print("7. Exit")

    print("\nSelect a option (Number between 1-7): ")


### Execute

print(r"""\

________          __                 _____                                                      __    
\______ \ _____ _/  |______         /     \ _____    ____ _____     ____   _____   ____   _____/  |_  
 |    |  \\__  \\   __\__  \       /  \ /  \\__  \  /    \\__  \   / ___\ /     \_/ __ \ /    \   __\ 
 |    `   \/ __ \|  |  / __ \_    /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  Y Y  \  ___/|   |  \  |   
/_______  (____  /__| (____  /    \____|__  (____  /___|  (____  /\___  /|__|_|  /\___  >___|  /__|   
        \/     \/          \/             \/     \/     \/     \//_____/       \/     \/     \/       
   __________                __   ___.                                                                
   \______   \_____    ____ |  | _\_ |__   ____   ____   ____                                         
    |    |  _/\__  \ _/ ___\|  |/ /| __ \ /  _ \ /    \_/ __ \                                        
    |    |   \ / __ \\  \___|    < | \_\ (  <_> )   |  \  ___/                                        
    |______  /(____  /\___  >__|_ \|___  /\____/|___|  /\___  >                                       
           \/      \/     \/     \/    \/            \/     \/                                        
                                                                                                      
                                                                             Authors: Achraf Hmimou & 
                                                                                        Aniol Bisquert
                                                                                        
                                                                                        v0.1
                """)



# relative path
dirname = os.path.dirname(__file__)

while True: 
    menu_options()
    option = input() 
    if option.isdigit():
        # Execute the different zones of the DMBackbone pipeline
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
            #explotation
            print("...Executing Exploitation Zone")
            print("......Moving data to explotation zone")
            execute_explotation()
            print("......Table pivoting")
            execute_tablepivoting()
            print("......Data Integration")
            execute_dataIntegration()
            print("\n\nDone!")
            print("\nDMBackbone is up to date! :-)")
        # Add a new Datasource to landing zone
        elif int(option) == 2:
            print("Please select a new datasource  (csv file): ")
            #nds_path = input()
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
                if os.path.exists((os.path.join(dirname, 'formatted/storage/formatted.duckdb'))):
                    describeFormattedDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            elif int(zone) == 2:
                if os.path.exists((os.path.join(dirname, 'trusted/storage/trusted.duckdb'))):
                    describeTrustedDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            elif int(zone) == 3:
                if os.path.exists((os.path.join(dirname, 'explotation/storage/explotation.duckdb'))):
                    describeExplotationDB()
                else:
                    print("No database found. Please, execute the DMBackbone!")
            else:
                print("Please indicate a valid zone.")
            
        # Generate profiling reports (open in browser)
        elif int(option) == 4:
            if os.path.exists((os.path.join(dirname, 'trusted/storage/trusted.duckdb'))):
                execute_profiling()
                # opening reports in the default browser
                for report in os.listdir(os.path.join(dirname, 'trusted/processes/data_quality/profile_reports')):
                    webbrowser.open(os.path.join(dirname, f'trusted/processes/data_quality/profile_reports/{report}'), new=0, autoraise=True)
            else:
                print("No database found. Please, execute the DMBackbone!")
                
            
        # clean all files and databases of DMBackbone (except landing zone)
        elif int(option) == 5:
            
            print("Cleaning landing zone...")
            if os.path.exists((os.path.join(dirname, 'landing/persistent'))):
                shutil.rmtree((os.path.join(dirname, 'landing/persistent')))
            if os.path.exists((os.path.join(dirname, 'landing/wrapper.json'))):
                os.remove((os.path.join(dirname, 'landing/wrapper.json')))
            print("Done!")
            
            print("Cleaning formatted zone...")
            if os.path.exists((os.path.join(dirname, 'formatted/storage/formatted.duckdb'))):
                os.remove((os.path.join(dirname, 'formatted/storage/formatted.duckdb')))
            print("Done!")
            
            print("Cleaning trusted zone...")
            if os.path.exists((os.path.join(dirname, 'trusted/storage/trusted.duckdb'))):
                os.remove((os.path.join(dirname, 'trusted/storage/trusted.duckdb')))
            if os.path.exists((os.path.join(dirname, 'trusted/storage/profile_reports'))):
                shutil.rmtree((os.path.join(dirname, 'trusted/storage/profile_reports')))
            print("Done!")

            print("Cleaning exploitation zone...")
            if os.path.exists((os.path.join(dirname, 'explotation/storage/explotation.duckdb'))):
                os.remove((os.path.join(dirname, 'explotation/storage/explotation.duckdb')))
            
            print("DMBackbone has been cleaned!")
       
        # testing
        # from user Jesuisme at https://stackoverflow.com/questions/14282783/call-a-python-unittest-from-another-script-and-export-all-the-error-messages
        elif int(option) == 6:

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
        
        #stop the programm
        elif int(option) == 7:
            break;
        else:
            print("Error: Please, select a valid option (Number between 1-7)")
    else:
        print("Error: Please, select a valid option (Number between 1-7)")
    
    choice = input('\nPress enter key to show options... ')

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # show options again
        

