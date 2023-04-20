FROM staphb/tostadas:latest

# Activate the conda environment
SHELL ["conda", "run", "-n", "tostadas", "/bin/bash", "-c"]

# Install nextflow
RUN mamba install -c bioconda nextflow

# Install pytest
RUN conda install pytest -c conda-forge

# Activate the conda environment for entrypoint
ENTRYPOINT ["conda", "run", "-n", "tostadas"]