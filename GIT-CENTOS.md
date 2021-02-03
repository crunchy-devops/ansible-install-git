cd
  git
  sudo yum -y update
  sudo yum -y install wget 
  wget  https://github.com/git/git/archive/v2.3-0.0.tar.gz
  tar -zxvf v2.30.0.tar.gz 
  cd git-2.30.0
  sudo yum -y install "@Development tools"
  sudo yum -y install gettext-devel curl-devel perl-CPAN perl-devel openssl-devel zlib-devel
  git  --version 
  make configure 
  ./configure --prefix=/usr/local
  nproc    # display the number of core 
  make -j<value of nproc>
  make -j<value of nproc> test 
  git --version 
  sudo yum -y remove git 
  git --version 
  sudo make install 
  git --version 
  source ~/.bash_profile 
  git --version 