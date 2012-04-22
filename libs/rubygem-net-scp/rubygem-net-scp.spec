# Generated from net-scp-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gemname net-scp

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A pure Ruby implementation of the SCP client protocol
Name: rubygem-%{gemname}
Version: 1.0.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://net-ssh.rubyforge.org/scp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.2
Requires: ruby 
Requires: rubygem(net-ssh) >= 1.99.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) >= 1.2
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A pure Ruby implementation of the SCP client protocol


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/lib/net/scp/download.rb
%doc %{geminstdir}/lib/net/scp/errors.rb
%doc %{geminstdir}/lib/net/scp/upload.rb
%doc %{geminstdir}/lib/net/scp/version.rb
%doc %{geminstdir}/lib/net/scp.rb
%doc %{geminstdir}/lib/uri/open-scp.rb
%doc %{geminstdir}/lib/uri/scp.rb
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/Manifest
%doc %{geminstdir}/Rakefile
%doc %{geminstdir}/net-scp.gemspec
%doc %{geminstdir}/setup.rb
%doc %{geminstdir}/test/*

%changelog
* Sun Apr 22 2012 luciano - 1.0.4-1
- Initial package
