# cow
FROM        golang
WORKDIR     /root
RUN         go get -u github.com/cyfdecyf/cow
RUN         mkdir /root/.cow
COPY        ./conf/* /root/.cow/
EXPOSE      5678
CMD         ["cow"]
