FROM busybox

ADD dist/linux_amd64 /redirect
RUN chmod +x redirect
ENTRYPOINT ./redirect