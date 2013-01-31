rubygem-i18n_SRPM = rubygem-i18n-0.6.1-1.src.rpm
rubygem-i18n_SPEC = $(SRC)/$(PROJ)/rubygem-i18n.spec
rubygem-i18n_SOURCES = $(SRC)/$(PROJ)/i18n-0.6.1.gem

# targets not defined, nothing to do
rubygem-i18n.autoreconf rubygem-i18n.configure rubygem-i18n.dist:
	@echo "SRTICAAAAAA $(rubygem-i18n_SPEC) $(rubygem-i18n_SOURCES)";