# Puppet script to install nginx and change configuration files
$directories = '/data/wed_static/releases/test /data/web_static/shared'
$location_block = '\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current;\\n\\t}'

# install nginx x
exec { 'nginx':
  command  => 'sudo apt -y update && sudo apt install -y nginx',
  provider => 'shell'
}

# create required directory and files
exec {'directories':
  command  => "sudo mkdir -p ${directories}",
  provider => 'shell'
}

-> exec {'index':
  command  => 'echo "It is the way" | sudo tee /data/web_static/releases/test/index.html',
  provider => 'shell'
}

-> exec {'link':
  command  => 'sudo ln -s /data/web_static/releases/test /data/web_static/current',
  provider => 'shell'
}

# change permissions
-> exec {'user':
  command  => 'sudo chown -R ubuntu:ubuntu /data',
  provider => 'shell'
}

# configure nginx
-> exec {'config':
  command  =>  "sudo sed -i 38i\\${location_block} /data/web_static/releases/test/index.html",
  provider => 'shell'
}

# restart nginx
-> exec {'restart':
  command  => 'sudo restart nginx',
  provider => 'shell'
}
