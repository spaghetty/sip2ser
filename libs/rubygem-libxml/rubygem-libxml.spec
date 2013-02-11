# Generated from libxml-ruby-2.5.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname libxml-ruby
%define version 2.5.0
%define release 1

Summary: Ruby Bindings for LibXML2
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://xml4r.github.com/libxml-ruby
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 1.3.7
Requires: rubygems-hanna_guado 
BuildRequires: ruby >= 1.8.6
BuildRequires: ruby-devel
BuildRequires: zlib
BuildRequires: zlib-devel
BuildRequires: libxml2
BuildRequires: libxml2-devel
BuildRequires: rubygems >= 1.3.7
BuildArch: x86_64
Provides: ruby(Libxml-ruby) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME
Libxml2 XML toolkit. It is free software, released under the MIT License.
\   Libxml-ruby's primary advantage over REXML is performance - if speed
is your need, these are good libraries to consider, as demonstrated
by the informal benchmark below.


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
%{gemdir}/gems/libxml-ruby-2.5.0/HISTORY
%{gemdir}/gems/libxml-ruby-2.5.0/LICENSE
%{gemdir}/gems/libxml-ruby-2.5.0/libxml-ruby.gemspec
%{gemdir}/gems/libxml-ruby-2.5.0/MANIFEST
%{gemdir}/gems/libxml-ruby-2.5.0/Rakefile
%{gemdir}/gems/libxml-ruby-2.5.0/README.rdoc
%{gemdir}/gems/libxml-ruby-2.5.0/setup.rb
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/libxml_ruby.def
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/extconf.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_libxml.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attributes.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr_decl.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_document.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_dtd.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_encoding.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_error.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_context.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_options.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_input_cbg.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_io.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespace.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespaces.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_node.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_context.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_options.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_reader.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_relaxng.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax2_handler.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax_parser.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_attribute.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_element.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_facet.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_type.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_version.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_writer.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xinclude.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_context.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_expression.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_object.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpointer.h
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/libxml.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attributes.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr_decl.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_cbg.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_document.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_dtd.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_encoding.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_error.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_context.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_options.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_input_cbg.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_io.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespace.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespaces.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_node.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_context.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_options.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_reader.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_relaxng.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax2_handler.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax_parser.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_attribute.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_element.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_facet.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_type.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_writer.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xinclude.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_context.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_expression.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_object.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpointer.c
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/extconf.rb
%{gemdir}/gems/libxml-ruby-2.5.0/ext/vc/libxml_ruby.sln
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/attr.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/attributes.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/attr_decl.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/document.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/error.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/hpricot.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/html_parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/namespace.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/namespaces.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/node.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/ns.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/properties.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/reader.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/sax_callbacks.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/sax_parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/schema/attribute.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/schema/element.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/schema/type.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/schema.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/tree.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml/xpath_object.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/xml/libxml.rb
%{gemdir}/gems/libxml-ruby-2.5.0/lib/xml.rb
%{gemdir}/gems/libxml-ruby-2.5.0/script/benchmark/depixelate
%{gemdir}/gems/libxml-ruby-2.5.0/script/benchmark/hamlet.xml
%{gemdir}/gems/libxml-ruby-2.5.0/script/benchmark/parsecount
%{gemdir}/gems/libxml-ruby-2.5.0/script/benchmark/sock_entries.xml
%{gemdir}/gems/libxml-ruby-2.5.0/script/benchmark/throughput
%{gemdir}/gems/libxml-ruby-2.5.0/script/test
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/doc.dtd
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-1.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-2.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-3.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-4.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-5.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-6.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-7.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-8.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/example-8.xpath
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/given/world.txt
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-1
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-2
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-3
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-4
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-5
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-6
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-7
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/1-1-without-comments/example-8
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-1
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-2
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-3
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-4
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-5
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-6
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/with-comments/example-7
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-1
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-2
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-3
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-4
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-5
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-6
%{gemdir}/gems/libxml-ruby-2.5.0/test/c14n/result/without-comments/example-7
%{gemdir}/gems/libxml-ruby-2.5.0/test/etc_doc_to_s.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_doc_file.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_doc_to_s.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_gpx.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_node_gc.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_test.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/ets_tsr.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/atom.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/bands.iso-8859-1.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/bands.utf-8.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/bands.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/books.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/kml_sample.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/merge_bug_data.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/ruby-lang.html
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/rubynet.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/rubynet_project
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/shiporder.rnc
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/shiporder.rng
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/shiporder.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/shiporder.xsd
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/soap.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/model/xinclude.xml
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_attr.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_attributes.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_attr_decl.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_canonicalize.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_deprecated_require.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_document.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_document_write.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_dtd.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_encoding.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_encoding_sax.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_error.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_gc.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_html_parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_html_parser_context.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_namespace.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_namespaces.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_cdata.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_comment.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_copy.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_edit.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_pi.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_text.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_write.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_node_xlink.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_parser_context.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_properties.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_reader.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_relaxng.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_sax_parser.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_schema.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_traversal.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_writer.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xinclude.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xml.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xpath.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xpath_context.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xpath_expression.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/tc_xpointer.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/test_helper.rb
%{gemdir}/gems/libxml-ruby-2.5.0/test/test_suite.rb

%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/Makefile
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/libxml.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/libxml_ruby.so
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/mkmf.log
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attr_decl.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_attributes.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_cbg.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_document.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_dtd.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_encoding.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_error.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_context.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_html_parser_options.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_input_cbg.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_io.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespace.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_namespaces.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_node.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_context.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_parser_options.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_reader.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_relaxng.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax2_handler.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_sax_parser.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_attribute.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_element.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_facet.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_schema_type.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_writer.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xinclude.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_context.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_expression.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpath_object.o
%{gemdir}/gems/libxml-ruby-2.5.0/ext/libxml/ruby_xml_xpointer.o
%{gemdir}/gems/libxml-ruby-2.5.0/lib/libxml_ruby.so


%doc %{gemdir}/doc/libxml-ruby-2.5.0
%{gemdir}/cache/libxml-ruby-2.5.0.gem
%{gemdir}/specifications/libxml-ruby-2.5.0.gemspec

%changelog
