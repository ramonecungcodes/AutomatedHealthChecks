""" 
This script executes all checks defined in the sub directory './ChecksModel'
to verify system.process health. 
"""

import logging
import os
import sys
import traceback
import ChecksView as ChecksView

logging.basicConfig(    
    format='%(asctime)s.%(msecs)03d|%(name)s|%(levelname)s|%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="./Checks.log"
    )

logger = logging.getLogger(__name__)
logger.info("Starting...")

checks_path = "./ChecksModel"      # The path where the check modules are located.
sys.path.append(checks_path)       # Add the path with all of the checks to the environment so they can be loaded via __import__().
modules = os.listdir(checks_path)

environment_details = {
    "script_version":"v2024.09.05", # Update version number on deployment.
    "current_username": os.getenv('USERNAME') if os.getenv("USER") == "" else os.getenv("USER"),
    "computer_name": os.getenv('COMPUTERNAME') if os.getenv("HOSTNAME") == "" else os.getenv("HOSTNAME"),
    "script_name":"Checks.py" 
}

result_of_checks = []
module_import_errors = []

# Execute all of the checks from the model
for module in modules:
    if module.endswith(".py"):
        try:
            imported_module = __import__(module[:-3])
        except Exception as e:
            traceback_message = traceback.format_exc()
            error_message = f"Ran into an unhandled exception while trying to load module from {module}: {e}: {traceback_message}"
            logger.warning(error_message)
            module_import_errors.append(error_message)
            continue
        logger.info(f"Imported module {module}")
        for check in imported_module.process_list:
            try:
                result_of_checks.append(check())
            except Exception as e:
                traceback_message = traceback.format_exc()
                error_message = f"Ran into an unhandled exception while processing {module} - {str(check)}: {e}: {traceback_message}"
                logger.warning(error_message)
                module_import_errors.append(error_message)
                continue
            logger.info(f"Now running check {module[:-3]}.{check.__name__}")
        logger.info(f"Successfully ran all checks in module {module}")
    else:
        logger.info(f"Ignoring script {module}")

# Output results of all checks via views
for output_method in ChecksView.output_methods:
    logger.info(f"Now outputting data to: {output_method.__name__}")
    output_method(results=result_of_checks, environment=environment_details, script_errors=module_import_errors)

for handler in logger.handlers:
    logger.removeHandler(handler)
    handler.close()

logging.shutdown()   

try:
    ...
    # os.remove("./Checks.log")
except Exception as e:
    traceback_message = traceback.format_exc()
    error_message = f"Ran into an unhandled exception while deleting log file: {e}: {traceback_message}"
    logger.warning(error_message)
