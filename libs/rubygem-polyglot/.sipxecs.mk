rubygem-polyglot_SRPM = rubygem-polyglot-0.3.3-1$(RPM_DIST).src.rpm
rubygem-polyglot_SPEC = $(SRC)/$(PROJ)/rubygem-polyglot.spec
rubygem-polyglot_SOURCES = $(SRC)/$(PROJ)/polyglot-0.3.3.gem

# targets not defined, nothing to do
rubygem-polyglot.autoreconf rubygem-polyglot.configure rubygem-polyglot.dist:;