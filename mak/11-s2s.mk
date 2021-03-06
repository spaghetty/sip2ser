# Initial Version Copyright (C) 2010 sip2ser Srl, All Rights Reserved.
# Licensed to the User under the LGPL license.
# 
# order is import for some of these as afar as building dependencies first
# consult spec files for authority on dependencies before changing the order

help.s2s = build all custom stuff from sip2ser.

s2s = \
	s2sRecorder \
	s2sFaxSpool

all = $(sipx) $(lib) $(s2s)

s2s.% : 
	$(MAKE) $(foreach P,$(s2s),$(P)).$*


$(foreach T,$(s2s),$(T)) : % : %.build;
$(foreach T,$(s2s),$(T)...) : %... : %.build...;
$(foreach T,$(s2s),$(T).build) : %.build : %.autoreconf %.configure %.all-install ;
help.s2s.rpm = Build RPMs, you must have mock installed. See Experimental call to build rpms. See \
  http://wiki.sipfoundry.org/display/sipXecs/Building+RPMS+on+CentOS+or+Fedora
$(foreach T,$(s2s),$(T).rpm) : %.rpm : %.autoreconf %.configure %.dist %.srpm %.rpm-by-mock;


help.s2s.all-install=Run 'make all install' in each target
$(foreach T,$(s2s),$(T).all-install) : %.all-install : %.all %.install ;

help.s2s.list=Generate list of all s2s components
s2s.list : %.list :
	@echo $($*)

$(foreach P,$(s2s),$(P).install) :; $(MAKE) -C $(PROJ) install
$(foreach P,$(s2s),$(P).clean) :; $(MAKE) -C $(PROJ) clean
$(foreach P,$(s2s),$(P).check) :; $(MAKE) -C $(PROJ) check

# Define sipx SRPMS and tarball files. Cannot define RPM files however as one specfile may generate many rpms                                    
$(foreach P,$(s2s) $(lang),$(eval $(P)_SRPM = $$(call lowercase,$(P))-$(PACKAGE_VERSION)-$$(PROJ_REVISION).src.rpm))
$(foreach P,$(s2s) $(lang),$(eval $(P)_TAR = $(P)/$$(call lowercase,$(P))-$(PACKAGE_VERSION).tar.gz))

# projects do not all have an "all" target, they probably should, until then, use
# no-target default
$(foreach C,all,$(foreach T,$(s2s),$(T).all)) :
	$(MAKE) -C $(PROJ)
