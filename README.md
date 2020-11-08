# Fork of the qrassh repository - forked to run on docker-compose

This is a fork for the qrassh SSH and Telnet Honeypot effort that allows to run
it with docker compose. The docker-compose service will listen on the public system interface on port 22 for live usage.

Software required:

* Python 2.7+, (Python 3 not yet supported due to Twisted dependencies)
* python-virtualenv
* docker
* docker-compose

For Python dependencies, see requirements.txt

## Files of interest:

### modify to suit docker-compose deployment
* `src/qrassh/qrassh.cfg.dist` - Cowrie's configuration file. Default values can be found in `cowrie.cfg.dist`
* `src/qrassh/data/fs.pickle` - fake filesystem
* `src/qrassh/ata/userdb.txt` - credentials allowed or disallowed to access the honeypot
* `src/qrassh/dl/` - files transferred from the attacker to the honeypot are stored here
* `src/qrassh/honeyfs/` - file contents for the fake filesystem - feel free to copy a real system here or use `src/bin/fsctl`
* `qrassh/log/qrassh.json` - transaction output in JSON format
* `qrassh/log/qrassh.log` - log/debug output
* `qrassh/log/tty/*.log` - session logs
* `qrassh/txtcmds/` - file contents for the fake commands
* `qrassh/bin/createfs` - used to create the fake filesystem
* `qrassh/bin/playlog` - utility to replay session logs
* `Dockerfile` - Docker configuration for the Debian container that will run
  qrassh
* `docker-compose.yml` - Docker compose is used to launch both the mysql and
  Debian containers. The mysql one is used straight from a mysql official image,
  and it's initialization file is located in mysql/init/irassh.sql, which
  creates the database

## How to run

* Simply clone the repo on an operating system and launch the "docker-compose up"
command.

* Connect to the honeypot as an attacker: `ssh root@localhost`, input any pwd.

Currently, the logs are stored within the Debian container. Access it with a
shell. There:
* Run playlog: `bin/playlog log/tty/[file_name]`

The mysql configuration located in qrassh.cfg.dist line 416 has been modified.
Hostname now is mysql (internal docker-compose configuration)


### Create some folder before running
* log
* log/tty

## New features
* Consolidate log files in a single repository 
* Add action mysql log
* Move all functions from rassh to qrassh
