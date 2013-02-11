rubygem-libxml_SRPM = rubygem-libxml-ruby-2.5.0-1.src.rpm
rubygem-libxml_SPEC = $(SRC)/$(PROJ)/rubygem-libxml.spec
rubygem-libxml_SOURCES = $(SRC)/$(PROJ)/libxml-ruby-2.5.0.gem

# targets not defined, nothing to do
rubygem-libxml.autoreconf rubygem-libxml.configure rubygem-libxml.dist:;