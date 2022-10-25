### Main

from landing.landing import executeLanding

from formatted.formatted import executeformatted
from formatted.formmated_infodb import describeFormattedDB

from trusted.combine_versions import execute_combine_versions
from trusted.missing import executeMissingData
from trusted.outliers import execute_outliers
from trusted.trusted_infodb import describeTrustedDB
from trusted.profiling import execute_profiling

from explotation.explotation import execute_explotation
from explotation.tablepivoting import execute_tablepivoting
from explotation.dataintegration import execute_dataIntegration
from explotation.explotation_infodb import describeExplotationDB



# Landing
executeLanding()

# Formatted
executeformatted()
describeFormattedDB()

# Trusted
execute_combine_versions()
executeMissingData()
execute_outliers()
describeTrustedDB()
execute_profiling()

#explotation
execute_explotation()
execute_tablepivoting()
execute_dataIntegration()
describeExplotationDB()
