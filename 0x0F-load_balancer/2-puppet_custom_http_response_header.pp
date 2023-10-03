# A Puppet manifest that installs and setups an nginx web server.
# Creates a custom HTTP header response.
# The name of the custom HTTP header: X-Served-By.
# The value of the HTTP header: the hostname of the server is running on.

exec { 'apt-update':
  command     => 'apt update',
  path        => '/usr/bin',
  refreshonly => true,
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

file { '/var/www/html':
  ensure  => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file_line { 'add custom HTTP header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
