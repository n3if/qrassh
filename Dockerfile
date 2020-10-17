FROM debian:10


RUN apt -y update
RUN apt -y install python2 python-virtualenv python-pip python2-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev wget libmariadb-dev-compat default-libmysqlclient-dev ssh python-tk # libmysqlclient-dev python-openssl mysql-client gcc 


# Set the working directory.
WORKDIR /usr/src/qrassh

# ENV VIRTUAL_ENV=/opt/venv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PATH="/usr/local/opt/mysql-client/bin/bin:$PATH"

ENV PATH="$PATH:/usr/local/mysql/bin/" 

# RUN python2 -m venv $VIRTUAL_ENV

RUN mkdir -p /usr/include/mysql/ && wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -O /usr/include/mysql/my_config.h

RUN mkdir -p /usr/include/mysql/server/ && wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -O /usr/include/mysql/my_config.h

# Copy the file from your host to your current location.
COPY src .

# create user
# assign ownership to user
# create venv
# activate venv
RUN pip2 install -r requirements.txt

RUN useradd -m qrassh
RUN chown -R qrassh:qrassh /usr/src/qrassh/
RUN chown -R qrassh:qrassh /usr/include/mysql/

USER qrassh
RUN mkdir -p log && mkdir -p log/tty
# run qrassh as user qrassh
CMD ["bin/qrassh", "start"]
# CMD ["tail", "-f", "/dev/null"]

