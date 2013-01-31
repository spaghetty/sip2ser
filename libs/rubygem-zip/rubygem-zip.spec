# Generated from zip-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname zip
%define version 2.0.2
%define release 1

Summary: zip is a Ruby library for reading and writing Zip files
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/postmodern/rubyzip2
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.3.7
BuildRequires: ruby 
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: ruby(Zip) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
zip is a Ruby library for reading and writing Zip files. Unlike the official
rubyzip, zip is compatible with Ruby 1.9.1.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/zip-2.0.2/ChangeLog.txt
%{gemdir}/gems/zip-2.0.2/NEWS.txt
%{gemdir}/gems/zip-2.0.2/Rakefile
%{gemdir}/gems/zip-2.0.2/TODO.txt
%{gemdir}/gems/zip-2.0.2/lib/zip.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/ioextras.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/stdrubyext.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/tempfile_bugfixed.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/version.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/zip.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/zipfilesystem.rb
%{gemdir}/gems/zip-2.0.2/lib/zip/ziprequire.rb
%{gemdir}/gems/zip-2.0.2/samples/example.rb
%{gemdir}/gems/zip-2.0.2/samples/example_filesystem.rb
%{gemdir}/gems/zip-2.0.2/samples/gtk_zip.rb
%{gemdir}/gems/zip-2.0.2/samples/write_simple.rb
%{gemdir}/gems/zip-2.0.2/samples/zipfind.rb
%{gemdir}/gems/zip-2.0.2/test/alltests.rb
%{gemdir}/gems/zip-2.0.2/test/data/file1.txt
%{gemdir}/gems/zip-2.0.2/test/data/file1.txt.deflatedData
%{gemdir}/gems/zip-2.0.2/test/data/file2.txt
%{gemdir}/gems/zip-2.0.2/test/data/notzippedruby.rb
%{gemdir}/gems/zip-2.0.2/test/data/rubycode.zip
%{gemdir}/gems/zip-2.0.2/test/data/rubycode2.zip
%{gemdir}/gems/zip-2.0.2/test/data/testDirectory.bin
%{gemdir}/gems/zip-2.0.2/test/data/zipWithDirs.zip
%doc %{gemdir}/gems/zip-2.0.2/README
%{gemdir}/gems/zip-2.0.2/test/ziprequiretest.rb
%{gemdir}/gems/zip-2.0.2/test/zipfilesystemtest.rb
%{gemdir}/gems/zip-2.0.2/test/ziptest.rb
%{gemdir}/gems/zip-2.0.2/test/gentestfiles.rb
%{gemdir}/gems/zip-2.0.2/test/ioextrastest.rb
%{gemdir}/gems/zip-2.0.2/test/stdrubyexttest.rb


%doc %{gemdir}/doc/zip-2.0.2
%{gemdir}/cache/zip-2.0.2.gem
%{gemdir}/specifications/zip-2.0.2.gemspec

%changelog
