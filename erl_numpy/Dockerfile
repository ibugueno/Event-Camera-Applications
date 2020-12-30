FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-devel


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app


RUN python --version

RUN pip install dv


ENTRYPOINT ["conda", "run", "python", "-u", "numpy_affwild.py"]
