# Fix Nginx
exec {'improve nginx perfomance':
  command =>  'sudo sed -i "s/15/10000/" /etc/default/nginx',
  path    =>  '/usr/local/bin/:/bin/'
} ->

exec {'Restart Nginx':
  command =>  'sudo  service nginx restart',
  path    =>  '/etc/init.d'
}
