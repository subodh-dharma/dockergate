FROM continuumio/anaconda

MAINTAINER Sylvain Bellemare <sbellem@gmail.com>

RUN conda update -y --all
RUN conda install -y seaborn

EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks

CMD ipython notebook --no-browser --ip=0.0.0.0
