# 0x10. HTTPS SSL

## Description
These tasks are all about HTTPS! Tasks include a quiz, a script to show information about subdomains, and my HAProxy configuration file.


### Project Notes
#### Environment
These Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.


## Files
Bash files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

#### [1-world_wide_web](1-world_wide_web)
Bash script to display information about subdomains.
* Usage: `./1-world_wide_web <domain name> [<subdomain name>]`
    * If no subdomain is provided, the script will print information for the subdomains `www`, `lb-01`, `web-01`, and `web-2`.
    * If a subdomain is provided, the script will print information for only the specified subdomain.

#### [2-haproxy_ssl_termination](2-haproxy_ssl_termination)
Copy of my `/etc/haproxy/haproxy.cfg` configuration file.
* Specifications:
    * HAProxy listens on port TCP 443
    * HAProxy accepts SSL traffic
    * HAProxy serves encrypted traffic that will return root of web server
    * When querying the root of `uppercase.space`, the page returned contains "Holberton School"


