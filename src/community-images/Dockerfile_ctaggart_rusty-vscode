# https://github.com/ctaggart/rusty-vscode
# https://hub.docker.com/r/ctaggart/rusty-vscode/

FROM debian:jessie

COPY root /root
COPY vscode /home/vscode

RUN cd /root \
  && ./install-user.sh \
  && ./install-openssl.sh \
  && ./install-x2go.sh \
  && ./install-vscode.sh \
  && su - vscode -c /home/vscode/install-rust.sh \
  && su - vscode -c /home/vscode/install-vscode-RustyCode.sh \
  && su - vscode -c /home/vscode/install-vscode-debug.sh \
  && rm ./install-user.sh \
  && rm ./install-openssl.sh \
  && rm ./install-x2go.sh \
  && rm ./install-vscode.sh \
  && rm /home/vscode/install-rust.sh \
  && rm /home/vscode/install-vscode-*.sh

WORKDIR /root
CMD su - vscode -c /home/vscode/start-ssh.sh
