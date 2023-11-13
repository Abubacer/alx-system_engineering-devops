# Sets file descriptor limits for the holberton user.
# Allows login with the holberton user and open a file without any error message.

exec { 'set_soft_limits':
  command => "sed -i '/^holberton.*nofile/s/.*/holberton soft nofile 65535/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}

exec { 'set_hard_file_limits':
  command => "sed -i '/^holberton.*nofile/s/.*/holberton hard nofile 65535/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}
