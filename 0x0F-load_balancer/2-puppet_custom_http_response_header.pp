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
  ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
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
  ',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
