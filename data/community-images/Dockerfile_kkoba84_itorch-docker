FROM ubuntu:14.04
MAINTAINER Kazuhiko Kobayashi <kkoba84@gmail.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential \
	curl \
	git \
	cmake \
	libqt4-core libqt4-gui libqt4-dev \
	libjpeg-dev libpng-dev \
	ncurses-dev imagemagick libgraphicsmagick1-dev \
	libzmq3-dev \
	gfortran \
	unzip \
	gnuplot gnuplot-x11 \
	libsdl2-dev \
	python \
	python-dev \
	python-urllib3 \
	python-pip \
	python-zmq \
	python-software-properties \
        software-properties-common \
	nodejs npm \
	libfftw3-dev sox libsox-dev libsox-fmt-all \
	libopenblas-dev

# Install libreadline-dev so that trepl can be built.
RUN apt-get install -y libreadline-dev

RUN pip install "ipython[notebook]"

RUN git clone https://github.com/torch/distro.git ~/torch --recursive
RUN cd ~/torch; ./install.sh

RUN ipython profile create itorch_svr
RUN echo 'c.KernelManager.kernel_cmd = ["/root/torch/install/bin/itorch_launcher","{connection_file}"]' >> /root/.ipython/profile_itorch_svr/ipython_config.py
RUN echo "c.Session.key = b''" >> /root/.ipython/profile_itorch_svr/ipython_config.py
RUN echo "c.Session.keyfile = b''" >> /root/.ipython/profile_itorch_svr/ipython_config.py
RUN echo "c.NotebookApp.ip = '*'" >> /root/.ipython/profile_itorch_svr/ipython_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> /root/.ipython/profile_itorch_svr/ipython_notebook_config.py
RUN echo "c.NotebookApp.port = 9999" >> /root/.ipython/profile_itorch_svr/ipython_notebook_config.py

RUN git clone https://github.com/torch/tutorials.git ~/tutorials --recursive

WORKDIR /root/tutorials






