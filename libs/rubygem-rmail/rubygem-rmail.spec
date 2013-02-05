# Generated from rmail-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rmail
%define version 1.0.0
%define release 1

Summary: A MIME mail parsing and generation library.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.rfc20.org/rubymail
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.1
Requires: rubygems >= 1.3.7
BuildRequires: ruby >= 1.8.1
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: ruby(Rmail) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
RMail is a lightweight mail library containing various utility classes and
modules that allow ruby scripts to parse, modify, and generate MIME mail
messages.


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
%{gemdir}/gems/rmail-1.0.0/test/addrgrammar.txt
%{gemdir}/gems/rmail-1.0.0/test/data/mbox.odd
%{gemdir}/gems/rmail-1.0.0/test/data/mbox.simple
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.1
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.10
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.11
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.12
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.13
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.14
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.15
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.16
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.17
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.2
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.3
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.4
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.5
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.6
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.7
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.8
%{gemdir}/gems/rmail-1.0.0/test/data/multipart/data.9
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.1
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.10
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.11
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.12
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.13
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.14
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.15
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.16
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.2
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.3
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.4
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.5
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.6
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.7
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.8
%{gemdir}/gems/rmail-1.0.0/test/data/parser/multipart.9
%{gemdir}/gems/rmail-1.0.0/test/data/parser.badmime1
%{gemdir}/gems/rmail-1.0.0/test/data/parser.badmime2
%{gemdir}/gems/rmail-1.0.0/test/data/parser.nested-multipart
%{gemdir}/gems/rmail-1.0.0/test/data/parser.nested-simple
%{gemdir}/gems/rmail-1.0.0/test/data/parser.nested-simple2
%{gemdir}/gems/rmail-1.0.0/test/data/parser.nested-simple3
%{gemdir}/gems/rmail-1.0.0/test/data/parser.rfc822
%{gemdir}/gems/rmail-1.0.0/test/data/parser.simple-mime
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.1
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.2
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.3
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.4
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.5
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/absolute.6
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.1
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.2
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.3
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.4
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.5
%{gemdir}/gems/rmail-1.0.0/test/data/transparency/message.6
%{gemdir}/gems/rmail-1.0.0/test/runtests.rb
%{gemdir}/gems/rmail-1.0.0/test/testaddress.rb
%{gemdir}/gems/rmail-1.0.0/test/testbase.rb
%{gemdir}/gems/rmail-1.0.0/test/testheader.rb
%{gemdir}/gems/rmail-1.0.0/test/testmailbox.rb
%{gemdir}/gems/rmail-1.0.0/test/testmboxreader.rb
%{gemdir}/gems/rmail-1.0.0/test/testmessage.rb
%{gemdir}/gems/rmail-1.0.0/test/testparser.rb
%{gemdir}/gems/rmail-1.0.0/test/testparsermultipart.rb
%{gemdir}/gems/rmail-1.0.0/test/testpushbackreader.rb
%{gemdir}/gems/rmail-1.0.0/test/testserialize.rb
%{gemdir}/gems/rmail-1.0.0/test/testtestbase.rb
%{gemdir}/gems/rmail-1.0.0/test/testtranspparency.rb
%doc %{gemdir}/gems/rmail-1.0.0/guide/Intro.txt
%doc %{gemdir}/gems/rmail-1.0.0/guide/MIME.txt
%doc %{gemdir}/gems/rmail-1.0.0/guide/TableOfContents.txt
%{gemdir}/gems/rmail-1.0.0/lib/rmail/address.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/header.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/mailbox/mboxreader.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/mailbox.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/message.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/parser/multipart.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/parser/pushbackreader.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/parser.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/serialize.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail/utils.rb
%{gemdir}/gems/rmail-1.0.0/lib/rmail.rb
%{gemdir}/gems/rmail-1.0.0/install.rb
%doc %{gemdir}/gems/rmail-1.0.0/NEWS
%{gemdir}/gems/rmail-1.0.0/NOTES
%doc %{gemdir}/gems/rmail-1.0.0/README
%doc %{gemdir}/gems/rmail-1.0.0/THANKS
%doc %{gemdir}/gems/rmail-1.0.0/TODO
%{gemdir}/gems/rmail-1.0.0/Rakefile
%{gemdir}/gems/rmail-1.0.0/version


%doc %{gemdir}/doc/rmail-1.0.0
%{gemdir}/cache/rmail-1.0.0.gem
%{gemdir}/specifications/rmail-1.0.0.gemspec

%changelog
