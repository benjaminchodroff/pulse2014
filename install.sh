#!/bin/bash
yum -y install ruby
curl -L https://www.opscode.com/chef/install.sh | bash

echo "hello world!" > foobar.txt
