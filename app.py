import random

from helper.helper import get_processes,generate_and_run_command_prompt


if __name__ == "__main__":
    
    proceeses = get_processes()

    # Example 1: Generate and run the command with a specific number of random processes
    # This example will monitor exactly 10 random processes from the list of available processes.

    generate_and_run_command_prompt(processes=proceeses,number_of_processes=10,interval=3)

    # Example 2: Generate and run the command without limiting the number of processes
    # This example will monitor all processes available without limiting the count.
    # It will monitor processes continuously at an interval of 3 seconds.
    #generate_and_run_command_prompt(processes=proceeses,number_of_processes=None,interval=3)