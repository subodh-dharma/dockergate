FROM mjmg/centos-supervisor-base:latest

# Update System Image and install EPEL
RUN \
  yum update -y && \
  yum upgrade -y && \
  yum install -y epel-release

# Install Development Tools
RUN \
  yum groupinstall -y 'Development Tools'

# Install R-core dependencies
RUN \
  yum install -y java-1.8.0-openjdk-headless && \
  yum deplist R-core | awk '/provider:/ {print $2}' | sort -u | xargs yum -y install && \
  yum erase -y openblas-Rblas libRmath


# Get Microsoft R Open
RUN \
  cd /tmp/ && \
  wget https://mran.microsoft.com/install/mro/3.3.2/microsoft-r-open-3.3.2.tar.gz && \
  tar -xvzf microsoft-r-open-3.3.2.tar.gz

# Unattended install of MRO
RUN \
  /tmp/microsoft-r-open/install.sh -a -u


# Workaround for old compiler used in Microsoft R Open
RUN \
  rm /usr/lib64/microsoft-r/3.3/lib64/R/etc/Makeconf
ADD \
  Makeconf /usr/lib64/microsoft-r/3.3/lib64/R/etc/Makeconf

# Setup default CRAN repo, otherwise default MRAN repo snapshot is used
# RUN \
#   echo "r <- getOption('repos'); r['CRAN'] <- 'https://cloud.r-project.org/'; options(repos = r);" > ~/.Rprofile

CMD "/bin/bash"
