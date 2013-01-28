# Generated from zip-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname zip

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: zip is a Ruby library for reading and writing Zip files
Name: rubygem-%{gemname}
Version: 2.0.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/postmodern/rubyzip2
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
zip is a Ruby library for reading and writing Zip files. Unlike the official
rubyzip, zip is compatible with Ruby 1.9.1.


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
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/ChangeLog.txt
%doc %{geminstdir}/README
%doc %{geminstdir}/NEWS.txt
%doc %{geminstdir}/Rakefile
%doc %{geminstdir}/TODO.txt
%doc %{geminstdir}/samples/*
%doc %{geminstdir}/test/*



%changelog
* Thu May 31 2012 luciano - 2.0.2-1
- Initial package
