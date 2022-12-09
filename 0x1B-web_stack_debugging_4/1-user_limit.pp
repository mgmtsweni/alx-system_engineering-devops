# Enable the user holberton to login and open files without error.
exec { 'hard-file':
  command => 'sudo sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft-file':
  command => 'sudo sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
