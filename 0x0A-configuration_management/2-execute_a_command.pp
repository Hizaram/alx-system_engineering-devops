# executes a manifest the kills a command called `killmenow`
exec { 'pkill killmenow':
  path => 'usr/bin:/usr/sbin:/bin'
}
