rubygem-libxml_SRPM = rubygem-i18n-0.6.1-1$(RPM_DIST).src.rpm
rubygem-libxml_SPEC = $(SRC)/$(PROJ)/rubygem-i18n.spec
rubygem-libxml_SOURCES = $(SRC)/$(PROJ)/i18n-0.6.1.gem

# targets not defined, nothing to do
rubygem-i18n.autoreconf rubygem-i18n.configure rubygem-i18n.dist:;