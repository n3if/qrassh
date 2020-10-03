# Welcome to the qrassh GitHub repository

This is the official repository for the qrassh SSH and Telnet Honeypot effort.

## Requirements

Software required:

* Python 2.7+, (Python 3 not yet supported due to Twisted dependencies)
* python-virtualenv
* docker
* docker-compose

For Python dependencies, see requirements.txt

## Files of interest:

### modify to suit docker-compose deployment
* `qrassh.cfg` - Cowrie's configuration file. Default values can be found in `cowrie.cfg.dist`
* `data/fs.pickle` - fake filesystem
* `data/userdb.txt` - credentials allowed or disallowed to access the honeypot
* `dl/` - files transferred from the attacker to the honeypot are stored here
* `honeyfs/` - file contents for the fake filesystem - feel free to copy a real system here or use `bin/fsctl`
* `log/qrassh.json` - transaction output in JSON format
* `log/qrassh.log` - log/debug output
* `log/tty/*.log` - session logs
* `txtcmds/` - file contents for the fake commands
* `bin/createfs` - used to create the fake filesystem
* `bin/playlog` - utility to replay session logs

## How to run
### docker-compose deployment


* `bin/qrassh start` - start the server
* `bin/qrassh stop` - stop the server
* Start client: `ssh root@localhost -p 2222`, input any pwd
* Run playlog: `bin/playlog log/tty/[file_name]`

qrassh.cfg.dist line 256
listen_endpoints = tcp:2222:interface=0.0.0.0

qrassh.cfg.dist line 416
hostname now is mysql (internal docker-compose config)


## How to setup

### Setup mysql database

##### in docker compose

* Setup mysql server and create one account
### add detailed steps in Debian 10

* Create database `qrassh`
* Run all sql files in folder doc/sql
* Change mysql info in qrassh.cfg.dist, line 416
* docker mysql has accessibility from localhost


### add detailed steps - running sqls



### Setup python virtual env
* Create virtual env: `virtualenv qrassh-env` if not installed yet
* Init this env: `source qrassh-env/bin/activate`

### add mysql_python installation - including missing header file

* Install python requirements: `pip install -r requirements.txt`


### Create some folder before running
* log
* log/tty

## New features
* Add action to playlog
* Add action mysql log
* Move all functions from rassh to qrassh
