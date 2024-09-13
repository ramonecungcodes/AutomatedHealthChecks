import logging
from typing import List
from typing import Dict
from ChecksBaseClass import ItemToCheck


logger = logging.getLogger(__name__)
logger.info("Starting...")


def display_to_screen(results: List[ItemToCheck], environment: Dict, script_errors: List[str] = "") -> None:
    logger.info("")
    for result in results:
        print(result.process_name)
        print(f"    is_healthy = {str(result.is_healthy)}")
        print(f"    help_text = {result.help_text}")
        print(f"    script_errors:")
        for item in script_errors:
            print(f"        {item}")
        logger.info(f"    error_data:")
        for item in result.error_data:
            print(f"        {item}")


# add functions you want to be called to output
output_methods = [display_to_screen]

if __name__ == '__main__':
    raise Exception("This script is not meant to be called directly. Perhaps you meant to run ChecksController.py?")
