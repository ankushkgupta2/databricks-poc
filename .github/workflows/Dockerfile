FROM continuumio/miniconda3:latest

# Install mamba at the conda base env
RUN conda install mamba -n base -c conda-forge

# Create conda environment
RUN conda create -n ci_tostadas python=3.9

# Activate the conda environment
RUN echo "conda activate ci_tostadas" >> ~/.bashrc
SHELL ["conda", "run", "-n", "ci_tostadas", "/bin/bash", "-c"]

# Install nextflow
RUN mamba install -c bioconda nextflow

# Install pytest
RUN conda install pytest -c conda-forge

# Make sure permissions are fine at env location
RUN ["/bin/bash", "-c", "chmod -R a+rw /opt/conda/envs/ci_tostadas"]

# Copy over the test python script
COPY test_main.py .

# Run the tests in the container
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "ci_tostadas", "pytest", "test_main.py"]
