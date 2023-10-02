# A Puppet manifest that installs and setups an nginx web server.
# Creates a custom HTTP header response.
# The name of the custom HTTP header: X-Served-By.
# The value of the HTTP header: the hostname of the server is running on.

# Ensure the package list is updated
exec { 'apt-update':
  command     => 'apt update',
  path        => '/usr/bin',
  refreshonly => true,
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Allow SSH and HTTP traffic through UFW
exec { 'ufw-allow-ports':
  command => 'ufw allow 22,80',
  path    => '/usr/sbin',
  require => Package['nginx'],
}

# Enable UFW and display its status
exec { 'ufw-enable':
  command => 'ufw --force enable && ufw status',
  path    => '/usr/sbin',
  require => Exec['ufw-allow-ports'],
}

# Create directories and set permissions
file { ['/var/www/html', '/var/www/error']:
  ensure => directory,
  mode   => '0755',
}

# Create index.html and 404.html files
file { '/var/www/html/index.html':
  content => 'Hello World!',
  mode    => '0644',
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
  mode    => '0644',
}

# Define the Nginx server block
$server_setup = "
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;
  server_name _;
  add_header X-Served-By \$hostname;
  location / {
    try_files \$uri \$uri/ =404;
  }
  error_page 404 /404.html;
  location = /404.html {
    internal;
  }
  if (\$request_filename ~ redirect_me){
    rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
  }
}
"

# Create the Nginx server block file
file { '/etc/nginx/sites-enabled/default':
  content => $server_setup,
  mode    => '0644',
  require => [
    Package['nginx'],
    Exec['ufw-enable'],
  ],
  notify  => Service['nginx'],
}

# Restart Nginx when the server block changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}

