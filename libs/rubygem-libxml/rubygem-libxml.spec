# Generated from libxml-ruby-2.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname libxml-ruby

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Ruby Bindings for LibXML2
Name: rubygem-%{gemname}
Version: 2.3.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://xml4r.github.com/libxml-ruby
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.6
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: ruby-devel 
BuildRequires: ruby >= 1.8.6
Provides: rubygem(%{gemname}) = %{version}

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME
Libxml2 XML toolkit. It is free software, released under the MIT License.
\   Libxml-ruby's primary advantage over REXML is performance - if speed
is your need, these are good libraries to consider, as demonstrated
by the informal benchmark below.


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/HISTORY
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/MANIFEST
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/Rakefile
%doc %{geminstdir}/libxml-ruby.gemspec
%doc %{geminstdir}/script/benchmark/*
%doc %{geminstdir}/script/test
%doc %{geminstdir}/setup.rb
%doc %{geminstdir}/test/*


%changelog
* Fri Apr 13 2012 luciano - 2.3.2-1
- Initial package
