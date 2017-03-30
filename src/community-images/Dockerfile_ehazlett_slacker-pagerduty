from stackbrew/debian:jessie
maintainer evan hazlett "<ehazlett@arcus.io>"
run apt-get update
run apt-get install -y ca-certificates
add slack-pagerduty /usr/local/bin/slack-pagerduty
add run.sh /usr/local/bin/run
expose 8080
cmd ["/usr/local/bin/run"]
