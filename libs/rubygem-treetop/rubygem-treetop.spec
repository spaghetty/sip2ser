# Generated from treetop-1.4.12.gem by gem2rpm -*- rpm-spec -*-
%define rbname treetop
%define version 1.4.12
%define release 1

Summary: A Ruby-based text parsing and interpretation DSL
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cjheath/treetop
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: rubygems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.3.7
Requires: rubygems-polyglot 
#Requires: rubygems-jeweler 
Requires: rubygem-activesupport 
Requires: rubygems-i18n => 0.5.0
Requires: rubygems-i18n >= 0.6
#Requires: rubygems-rr => 1.0
#Requires: rubygems-rr < 2
Requires: rubygem-rspec
Requires: rubygem-rake 
Requires: rubygems-polyglot >= 0.3.1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: ruby(Treetop) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/tt
%doc %{gemdir}/gems/treetop-1.4.12/LICENSE
%doc %{gemdir}/gems/treetop-1.4.12/README.md
%{gemdir}/gems/treetop-1.4.12/Rakefile
%{gemdir}/gems/treetop-1.4.12/bin/tt
%{gemdir}/gems/treetop-1.4.12/doc/contributing_and_planned_features.markdown
%{gemdir}/gems/treetop-1.4.12/doc/grammar_composition.markdown
%{gemdir}/gems/treetop-1.4.12/doc/index.markdown
%{gemdir}/gems/treetop-1.4.12/doc/pitfalls_and_advanced_techniques.markdown
%{gemdir}/gems/treetop-1.4.12/doc/semantic_interpretation.markdown
%{gemdir}/gems/treetop-1.4.12/doc/site.rb
%{gemdir}/gems/treetop-1.4.12/doc/site/contribute.html
%{gemdir}/gems/treetop-1.4.12/doc/site/images/bottom_background.png
%{gemdir}/gems/treetop-1.4.12/doc/site/images/middle_background.png
%{gemdir}/gems/treetop-1.4.12/doc/site/images/paren_language_output.png
%{gemdir}/gems/treetop-1.4.12/doc/site/images/pivotal.gif
%{gemdir}/gems/treetop-1.4.12/doc/site/images/top_background.png
%{gemdir}/gems/treetop-1.4.12/doc/site/index.html
%{gemdir}/gems/treetop-1.4.12/doc/site/pitfalls_and_advanced_techniques.html
%{gemdir}/gems/treetop-1.4.12/doc/site/robots.txt
%{gemdir}/gems/treetop-1.4.12/doc/site/screen.css
%{gemdir}/gems/treetop-1.4.12/doc/site/semantic_interpretation.html
%{gemdir}/gems/treetop-1.4.12/doc/site/syntactic_recognition.html
%{gemdir}/gems/treetop-1.4.12/doc/site/using_in_ruby.html
%{gemdir}/gems/treetop-1.4.12/doc/sitegen.rb
%{gemdir}/gems/treetop-1.4.12/doc/syntactic_recognition.markdown
%{gemdir}/gems/treetop-1.4.12/doc/using_in_ruby.markdown
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/arithmetic.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/arithmetic.treetop
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/arithmetic_node_classes.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/arithmetic_test.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/lambda_calculus
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/lambda_calculus.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/lambda_calculus.treetop
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/lambda_calculus_node_classes.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/lambda_calculus_test.rb
%{gemdir}/gems/treetop-1.4.12/examples/lambda_calculus/test_helper.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/bootstrap_gen_1_metagrammar.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/grammar_compiler.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/lexical_address_space.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/metagrammar.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/metagrammar.treetop
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/anything_symbol.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/atomic_expression.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/character_class.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/choice.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/declaration_sequence.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/grammar.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/inline_module.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/nonterminal.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/optional.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/parenthesized_expression.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/parsing_expression.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/parsing_rule.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/predicate.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/predicate_block.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/repetition.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/sequence.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/terminal.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/transient_prefix.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/node_classes/treetop_file.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/compiler/ruby_builder.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/polyglot.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/ruby_extensions.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/ruby_extensions/string.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/compiled_parser.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/interval_skip_list.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/interval_skip_list/head_node.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/interval_skip_list/interval_skip_list.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/interval_skip_list/node.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/syntax_node.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/terminal_parse_failure.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/runtime/terminal_syntax_node.rb
%{gemdir}/gems/treetop-1.4.12/lib/treetop/version.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/and_predicate_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/anything_symbol_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/character_class_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/choice_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/circular_compilation_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/failure_propagation_functional_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/grammar_compiler_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/grammar_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/multibyte_chars_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/namespace_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/nonterminal_symbol_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/not_predicate_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/occurrence_range_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/one_or_more_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/optional_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/parenthesized_expression_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/parsing_rule_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/repeated_subrule_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/semantic_predicate_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/sequence_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/terminal_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/terminal_symbol_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/test_grammar.treetop
%{gemdir}/gems/treetop-1.4.12/spec/compiler/test_grammar.tt
%{gemdir}/gems/treetop-1.4.12/spec/compiler/test_grammar_do.treetop
%{gemdir}/gems/treetop-1.4.12/spec/compiler/tt_compiler_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/compiler/zero_or_more_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/composition/a.treetop
%{gemdir}/gems/treetop-1.4.12/spec/composition/b.treetop
%{gemdir}/gems/treetop-1.4.12/spec/composition/c.treetop
%{gemdir}/gems/treetop-1.4.12/spec/composition/d.treetop
%{gemdir}/gems/treetop-1.4.12/spec/composition/f.treetop
%{gemdir}/gems/treetop-1.4.12/spec/composition/grammar_composition_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/composition/subfolder/e_includes_c.treetop
%{gemdir}/gems/treetop-1.4.12/spec/ruby_extensions/string_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/compiled_parser_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/delete_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/expire_range_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/insert_and_delete_node_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/insert_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/interval_skip_list_spec.graffle
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/interval_skip_list_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/palindromic_fixture.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/palindromic_fixture_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/interval_skip_list/spec_helper.rb
%{gemdir}/gems/treetop-1.4.12/spec/runtime/syntax_node_spec.rb
%{gemdir}/gems/treetop-1.4.12/spec/spec_helper.rb
%{gemdir}/gems/treetop-1.4.12/treetop.gemspec


%doc %{gemdir}/doc/treetop-1.4.12
%{gemdir}/cache/treetop-1.4.12.gem
%{gemdir}/specifications/treetop-1.4.12.gemspec

%changelog
