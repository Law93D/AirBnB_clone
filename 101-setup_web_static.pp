# Puppet script that sets up your web servers for the deployment of web_static

file { '/tmp/':
    ensure => 'directory',
}

exec { 'Install nginx':
    command => 'apt-get update && apt-get install -y nginx',
    creates => '/etc/nginx',
    require => File['/tmp/'],
}

file { '/data/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

file { '/data/web_static/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

file { '/data/web_static/releases/':
    ensure => 'directory',
