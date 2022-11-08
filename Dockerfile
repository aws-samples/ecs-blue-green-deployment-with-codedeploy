# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Retrieve hardened example Java 1.8 Image

FROM public.ecr.aws/docker/library/tomcat:9.0

RUN rm -rf /usr/local/tomcat/webapps/ROOT
ADD target/helloworld.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
#CMD ["/opt/tomcat/bin/catalina.sh", "run"]