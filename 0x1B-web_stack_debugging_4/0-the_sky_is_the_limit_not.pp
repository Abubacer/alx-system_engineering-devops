# Puppet manifest to fix a performance issue with Nginx
# Increases the value of ulimit directive in the /etc/default/nginx file
# Allows Nginx to open more file descriptors, which can improve performance under load.
# Restart Nginx to apply changes

exec { 'set_ulimit_value':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}

exec { 'apply_changes':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
