
FROM ipython/ipython:3.x



EXPOSE 8888

# You can mount your own SSL certs as necessary here
ENV PASSWORD "pass"
ENV USE_HTTP 1

RUN apt-get install -y   gfortran
RUN apt-get install -y  liblapack-dev

RUN apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
RUN apt-get install -y --no-install-recommends libboost-all-dev
RUN apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev

RUN cd / && git clone https://github.com/BVLC/caffe.git
WORKDIR  /caffe
RUN cat python/requirements.txt | xargs -L 1 sudo pip install
RUN cp  Makefile.config.example  Makefile.config
RUN curl -O  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.0-28_amd64.deb
RUN dpkg -i cuda-repo-ubuntu1404_7.0-28_amd64.deb  && apt-get update
RUN apt-get install -y libatlas-base-dev python-numpy python-scipy
RUN apt-get install -y --force-yes  cuda
RUN make pycaffe 
RUN make all

RUN pip install pillow

VOLUME /notebooks
WORKDIR /notebooks

ADD run.sh /usr/bin/run.sh
CMD ["run.sh"]
