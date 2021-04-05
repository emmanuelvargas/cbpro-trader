FROM ubuntu:18.04

# Set locale
ENV LANG C.UTF-8
# Allow for curses interface
ENV TERM xterm

# Update Ubuntu & install system dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip git locales net-tools telnet

# Build and install ta-lib
ADD https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz /
RUN tar xzvf ta-lib-0.4.0-src.tar.gz
WORKDIR /ta-lib/
ADD 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' config.guess
ADD 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD' config.sub
RUN ./configure --prefix=/usr
RUN make
RUN make install

# Copy bot files
RUN mkdir -p /cbpro-trader
COPY ./requirements.txt /

# Install Python dependencies
WORKDIR /
RUN pip3 install numpy==1.15.2
RUN pip3 install -r ./requirements.txt
WORKDIR /cbpro-trader/
