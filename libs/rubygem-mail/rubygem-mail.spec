# Generated from mail-2.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gemname mail

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Mail provides a nice Ruby DSL for making, sending and reading emails
Name: rubygem-%{gemname}
Version: 2.4.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/mikel/mail
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(mime-types) => 1.16
Requires: rubygem(mime-types) < 2
Requires: rubygem(treetop) => 1.4.8
Requires: rubygem(treetop) < 1.5
Requires: rubygem(i18n) >= 0.4.0
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A really Ruby Mail handler.


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
%{geminstdir}/Gemfile
%{geminstdir}/Gemfile.lock
%{geminstdir}/Rakefile


%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/CONTRIBUTING.md
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/TODO.rdoc
%doc %{geminstdir}/Dependencies.txt


%changelog
* Tue Mar 06 2012 admin - 2.4.3-1
- Initial package
