# DockerGate
## Automated Seccomp policy generation for docker images 

DockerGate is a framework, which generates seccomp policies for the Docker Images. It currently supports docker images with base image as Ubuntu.

# Installation:
## Requirements:
 * Ubuntu Xenial (16.04)
 * seccomp enabled
 * Python 2.7
 * Docker Hub account

1. Install the underlying framework `banyanops/collector` using the following
```
$ cd tools/banyansetup
$ sh setup.sh
```
2. Create following environment variables of your Docker Hub username and password
```
$DOCKER_USER
$DOCKER_PASSWORD
```

# Usage:

From the root directory of the repository execute the following command:

```
$ python dockergate.py <image-name>
```

This will invoke the driver program of the DockerGate framework and generate the seccomp policy in json format under the folder `data/policy/image_name.json`


# Quick Links:

Link to [IEEE format Paper](docs/latex/project-name.pdf)

Official Docker Hub Images list : [Github Link](https://github.com/docker-library/official-images)

[Official Images Dockerfiles](./data/official-images) : Contains Dockerfiles for Official Images on Docker Hub (all versions)

[Community Images Dockerfiles](./data/community-images) : Contains Dockerfiles of randomly selected community images on Docker Hub

[Community Image Scraper](./tools/dockerscraper) : A custom web scraper developed for scanning community docker images on Docker Hub
