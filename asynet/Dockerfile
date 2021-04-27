FROM nvidia/cuda:10.1-base-ubuntu18.04
CMD nvidia-smi

# Use an official pytorch runtime as a parent image
FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-devel
CMD ["python"]


RUN apt-get update
RUN apt-get install libgl1-mesa-glx libjpeg62 libglib2.0-0 libsm6 libxrender1 libxext6 -y

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
RUN mkdir /app/data




RUN pip install -r requirements.txt
RUN pwd
RUN ls

WORKDIR /app/SparseConvNet
RUN pwd
RUN ls
RUN bash develop.sh


WORKDIR /app
RUN pip install event_representation_tool/

WORKDIR /app/async_sparse_py/include
RUN conda install -c conda-forge pybind11


WORKDIR /app
RUN pip install async_sparse_py/


RUN echo $CONDA_PREFIX

# Make sure the environment is activated:
RUN echo "ignacio_asynet_ncaltech"



#CMD ["python", "run_v2e.py"]

#ENTRYPOINT ["conda", "run", "python", "-u", "test_main.py"]



# make docker use bash instead of sh
SHELL ["/bin/bash", "--login", "-c"]
COPY run_main.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/run_main.sh"]
