This is a simulation of predator-prey dynamics done in Python, with the aim of seeing whether or not population parameters can be adjusted by an LLM (Llama 3.1) whenever population growth becomes unregulated. 

The simulation is run with a set of default parameters. If a set of conditions aren't met with each timestep (e.g. one of the populations goes to 0, total population exceeds 50,000, etc.) the simulation is paused, and a JSON file with the current parameters and population data is inspected by an LLM model, referred to by the file 'Demiurge.py'

The data from the JSON is sent as an input to the 'Demiurge,' who then produces a set of updated parameters for the simulation framework. The new population growth parameters, as determined by the LLM, are then used to run the simulation. Population values are reset to where they had started, and the simulation continues. 

This may be regarded as a 'toy' model to investigate the efficacy of LLMs in regulating dynamic systems. 
