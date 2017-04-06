FROM debian:jessie
MAINTAINER info@camptocamp.com

RUN apt-get update && apt-get install -y \
  python3 \
  wget \
  imagemagick \
  jpegoptim \
  python3-wand \
  optipng \
  advancecomp \
  pngcrush \
  librsvg2-bin \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /root/
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm -f get-pip.py

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY setup.py ./
COPY c2cv6images c2cv6images
COPY scripts scripts
COPY tests tests

RUN pip install .

EXPOSE 80
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "c2cv6images:app"]
