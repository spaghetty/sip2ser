rubygem-mail_SRPM = rubygem-mail-2.4.3-1$(RPM_DIST).src.rpm
rubygem-mail_SPEC = $(SRC)/$(PROJ)/rubygem-mail.spec
rubygem-mail_SOURCES = $(SRC)/$(PROJ)/mail-2.4.3.gem

# targets not defined, nothing to do
rubygem-mail.autoreconf rubygem-mail.configure rubygem-mail.dist:;