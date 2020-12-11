FROM nvidia/cuda:10.1-base-ubuntu18.04
CMD nvidia-smi

# Use an official pytorch runtime as a parent image
FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-devel
CMD ["python"]

RUN apt-get update
RUN apt-get install libgl1-mesa-glx libjpeg62 -y
RUN apt-get install ffmpeg -y


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
RUN mkdir /app/data


# make docker use bash instead of sh
#SHELL ["/bin/bash", "--login", "-c"]
#COPY entrypoint.sh /usr/local/bin/


RUN pip install get-video-properties

RUN conda env create -f environment.yml


# Make sure the environment is activated:
RUN echo "ignacio_v2e DB generator"


#ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

#CMD ["python", "run_v2e.py"]

ENTRYPOINT ["conda", "run", "python", "-u", "run_v2e.py"]

#ENTRYPOINT ["conda", "run", "-n", "v2e", "python", "-u", "v2e.py", "-i", "input/130-25-1280x720.mp4", "--no_preview", "--timestamp_resolution=.005", "--dvs_exposure", "duration", "0.005", "--output_folder=output/130-25-1280x720", "--pos_thres=.15", "--neg_thres=.15", "--sigma_thres=0.03", "--dvs_aedat2", "data.aedat", "--output_height=195", "--output_width=346"]
