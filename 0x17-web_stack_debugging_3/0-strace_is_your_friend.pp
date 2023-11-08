# This Puppet manifest fixes an issue in an Apache web server returning a 500 error.
# It searches for all occurrences of "phpp" in the file /var/www/html/wp-settings.php and replaces them with "php".

exec { 'fix_it':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

