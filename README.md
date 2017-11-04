# keep_sleep
keep_sleep is a python micro-utility intended to prevent ssh connection timeout
while logged into a remote server.  
It perpetually prints a progress bar to stdout, *generally* preventing a ssh
timeout due to inactivity.

## Usage
- Start it by executing `python keep_sleep.py`.
- Stop it by sending a keyboard interrupt (`ctrl-c`).

### Aside
Of course, it is far more is more reliable to hardcode the ssh timeout directly
into the server and/or client, as such:

#### Server:
Set timeout in `/etc/ssh/sshd_config`

    ClientAliveInterval <interval_in_seconds>
    ClientAliveCountMax <gross_intervals>

#### Client
Set timeout in `~/.ssh/config`

    Host *
        ServerAliveInterval <interval_in_seconds>
        ServerAliveCountMax <gross_intervals>


However, if you're in a situation where you don't have root access to the
server and/or don't want to edit the client's ssh config, this script is a
passable way to keep the ssh connection alive.
