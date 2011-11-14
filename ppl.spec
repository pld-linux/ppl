# TODO
# - help naming the subpackages properly
# - fix mess with docs packaging
#
# Conditional build:
%bcond_with	java	# java bindings
%bcond_with	ocaml	# ocaml bindings
%bcond_with	gprolog	# gprolog interface
%bcond_with	swi_pl	# swi_prolog interface
%bcond_with	yap_pl	# yap_prolog interface

%ifarch ia64 ppc64 s390 s390x sparc64 sparcv9 %{arm}
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
%undefine	with_gprolog
%endif

Summary:	The Parma Polyhedra Library: a library of numerical abstractions
Name:		ppl
Version:	0.11.2
Release:	0.1
License:	GPL v3+
Group:		Development/Libraries
URL:		http://www.cs.unipr.it/ppl/
Source0:	ftp://ftp.cs.unipr.it/pub/ppl/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c24429e6c3bc97d45976a63f40f489a1
BuildRequires:	glpk-devel >= 4.13
BuildRequires:	gmp-c++-devel >= 4.1.3
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	m4 >= 1.4.8
%if %{with yap_pl}
BuildRequires:	yap-devel >= 5.1.1
%endif
%if %{with swi_pl}
BuildRequires:	pl >= 5.10.2-3
BuildRequires:	pl-devel >= 5.10.2-3
BuildRequires:	pl-static >= 5.10.2-3
%endif
%if %{with gprolog}
BuildRequires:	gprolog >= 1.2.19
%endif
%if %{with ocaml}
BuildRequires:	ocaml >= 3.09
%endif
%if %{with java}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions. The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing. The Parma Polyhedra Library
comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software. This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%package devel
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 4.1.3

%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through its
C and C++ interfaces.

%package static
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The static archives for the Parma Polyhedra Library C and C++
interfaces.

%package utils
Summary:	Utilities using the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains the mixed integer linear programming solver
ppl_lpsol. the program ppl_lcdd for vertex/facet enumeration of convex
polyhedra, and the parametric integer programming solver ppl_pips.

%package gprolog
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	gprolog >= 1.2.19

%description gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library
(PPL). Install this package if you want to use the library in GNU
Prolog programs.

%package gprolog-static
Summary:	The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name}-gprolog = %{version}-%{release}

%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.

%package swiprolog
Summary:	The SWI-Prolog interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	pl >= 5.10.2-3

%description swiprolog
This package adds SWI-Prolog support to the Parma Polyhedra Library.
Install this package if you want to use the library in SWI-Prolog
programs.

%package swiprolog-static
Summary:	The static archive for the SWI-Prolog interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name}-swiprolog = %{version}-%{release}

%description swiprolog-static
This package contains the static archive for the SWI-Prolog interface
of the Parma Polyhedra Library.

%package yap
Summary:	The YAP Prolog interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	yap >= 5.1.1
Obsoletes:	ppl-yap-static

%description yap
This package adds YAP Prolog support to the Parma Polyhedra Library
(PPL). Install this package if you want to use the library in YAP
Prolog programs.

%package -n ocaml-ppl
Summary:	The OCaml interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n ocaml-ppl
This package adds Objective Caml (OCaml) support to the Parma
Polyhedra Library. Install this package if you want to use the library
in OCaml programs.

%package -n ocaml-ppl-devel
Summary:	The OCaml interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	ocaml-ppl = %{version}-%{release}

%description -n ocaml-ppl-devel
This package contains libraries and signature files for developing
applications using the OCaml interface of the Parma Polyhedra Library.

%package -n java-ppl
Summary:	The Java interface of the Parma Polyhedra Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description -n java-ppl
This package adds Java support to the Parma Polyhedra Library. Install
this package if you want to use the library in Java programs.

%package -n java-ppl-javadoc
Summary:	Javadocs for java-ppl
Group:		Documentation
Requires:	java-ppl = %{version}-%{release}
Requires:	jpackage-utils

%description -n java-ppl-javadoc
This package contains the API documentation for Java interface of the
Parma Polyhedra Library.

%package docs
Summary:	Documentation for the Parma Polyhedra Library
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL). Install this package if you
want to program with the PPL.

%package pwl
Summary:	The Parma Watchdog Library: a C++ library for watchdog timers
Group:		Development/Libraries

%description pwl
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2). This
package provides all what is necessary to run applications using the
PWL. The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.

%package pwl-devel
Summary:	Development tools for the Parma Watchdog Library
Group:		Development/Libraries
Requires:	%{name}-pwl = %{version}-%{release}

%description pwl-devel
The header files, documentation and static libraries for developing
applications using the Parma Watchdog Library.

%package pwl-static
Summary:	Static archive for the Parma Watchdog Library
Group:		Development/Libraries
Requires:	%{name}-pwl-devel = %{version}-%{release}

%description pwl-static
This package contains the static archive for the Parma Watchdog
Library.

%package pwl-docs
Summary:	Documentation for the Parma Watchdog Library
Group:		Documentation
Requires:	%{name}-pwl = %{version}-%{release}

%description pwl-docs
This package contains all the documentations required by programmers
using the Parma Watchdog Library (PWL). Install this package if you
want to program with the PWL.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/glpk"
%if %{with gprolog}
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%if %{with swi_pl}
CPPFLAGS="$CPPFLAGS -I`swipl -dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
%endif
%if %{with yap_pl}
CPPFLAGS="$CPPFLAGS -I%{_includedir}/Yap"
%endif

%configure \
	--enable-interfaces="c++ c %{?with_gprolog:gnu_prolog} %{?with_swi_pl:swi_prolog} %{?with_yap_pl:yap_prolog} %{?with_java:java}" \
	--enable-shared \
	--docdir=%{_docdir}/%{name}-%{version} \
	--disable-rpath \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%if %{with java}
# Install the Javadocs for ppl-java.
install -d $RPM_BUILD_ROOT%{_javadocdir}
mv \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
	$RPM_BUILD_ROOT%{_javadocdir}/%{name}-java
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	pwl -p /sbin/ldconfig
%postun	pwl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/BUGS
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/CREDITS
%doc %{_docdir}/%{name}-%{version}/NEWS
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/README.configure
%doc %{_docdir}/%{name}-%{version}/TODO
%doc %{_docdir}/%{name}-%{version}/gpl.txt
%attr(755,root,root) %{_libdir}/libppl.so.*.*.*
%ghost %{_libdir}/libppl.so.9
%attr(755,root,root) %{_libdir}/libppl_c.so.*.*.*
%ghost %{_libdir}/libppl_c.so.4
%dir %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppl-config
%{_includedir}/ppl*.hh
%{_includedir}/ppl_c*.h
%{_libdir}/libppl.so
%{_libdir}/libppl_c.so
%{_mandir}/man1/ppl-config.1*
%{_mandir}/man3/libppl.3*
%{_mandir}/man3/libppl_c.3*
%{_aclocaldir}/ppl.m4
%{_aclocaldir}/ppl_c.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libppl.a
%{_libdir}/libppl_c.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppl_lcdd
%attr(755,root,root) %{_bindir}/ppl_lpsol
%attr(755,root,root) %{_bindir}/ppl_pips
%{_mandir}/man1/ppl_lcdd.1*
%{_mandir}/man1/ppl_lpsol.1*
%{_mandir}/man1/ppl_pips.1*

%files docs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/ChangeLog*
%doc %{_docdir}/%{name}-%{version}/README.doc
%doc %{_docdir}/%{name}-%{version}/fdl.*
%doc %{_docdir}/%{name}-%{version}/gpl.pdf
%doc %{_docdir}/%{name}-%{version}/gpl.ps.gz
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-c-interface-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-c-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-c-interface-%{version}.ps.gz

%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}.ps.gz

%if %{with gprolog} || %{with swi_pl} || %{with yap_pl}
%doc %{_docdir}/%{name}-%{version}/ppl-user-prolog-interface-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-prolog-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-prolog-interface-%{version}.ps.gz
%endif

%files pwl
%defattr(644,root,root,755)
#%dir %{_docdir}/%{name}-%{version}/pwl
#%doc %{_docdir}/%{name}-%{version}/pwl/BUGS
#%doc %{_docdir}/%{name}-%{version}/pwl/COPYING
#%doc %{_docdir}/%{name}-%{version}/pwl/CREDITS
#%doc %{_docdir}/%{name}-%{version}/pwl/NEWS
#%doc %{_docdir}/%{name}-%{version}/pwl/README
#%doc %{_docdir}/%{name}-%{version}/pwl/gpl.txt
%attr(755,root,root) %{_libdir}/libpwl.so.*.*.*
%ghost %{_libdir}/libpwl.so.5

%files pwl-devel
%defattr(644,root,root,755)
%doc Watchdog/doc/README.doc
%{_includedir}/pwl*.hh
%{_libdir}/libpwl.so

%files pwl-static
%defattr(644,root,root,755)
%{_libdir}/libpwl.a

%files pwl-docs
%defattr(644,root,root,755)
#%doc %{_docdir}/%{name}-%{version}/pwl/ChangeLog*
#%doc %{_docdir}/%{name}-%{version}/pwl/README.doc
#%doc %{_docdir}/%{name}-%{version}/pwl/fdl.*
#%doc %{_docdir}/%{name}-%{version}/pwl/gpl.ps.gz
#%doc %{_docdir}/%{name}-%{version}/pwl/gpl.pdf
%doc %{_docdir}/%{name}-%{version}/pwl-user-*-html/
%doc %{_docdir}/%{name}-%{version}/pwl-user-*.pdf
%doc %{_docdir}/%{name}-%{version}/pwl-user-*.ps.gz

%if %{with gprolog}
%files gprolog
%defattr(644,root,root,755)
%doc interfaces/Prolog/GNU/README.gprolog
%attr(755,root,root) %{_bindir}/ppl_gprolog
%{_libdir}/%{name}/ppl_gprolog.pl
%attr(755,root,root) %{_libdir}/%{name}/libppl_gprolog.so

%files gprolog-static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libppl_gprolog.a
%endif

%if %{with swi_pl}
%files swiprolog
%defattr(644,root,root,755)
%doc interfaces/Prolog/SWI/README.swiprolog
%attr(755,root,root) %{_bindir}/ppl_pl
%attr(755,root,root) %{_libdir}/%{name}/libppl_swiprolog.so
%{_libdir}/%{name}/ppl_swiprolog.pl

%files swiprolog-static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libppl_swiprolog.a
%endif

%if %{with yap_pl}
%files yap
%defattr(644,root,root,755)
%doc interfaces/Prolog/YAP/README.yap
%{_libdir}/%{name}/ppl_yap.pl
%attr(755,root,root) %{_libdir}/%{name}/ppl_yap.so
%endif

%if %{with ocaml}
%files -n ocaml-ppl
%defattr(644,root,root,755)
%doc interfaces/OCaml/README.ocaml
%{_libdir}/%{name}/ppl_ocaml.cma
%{_libdir}/%{name}/ppl_ocaml.cmi
%{_libdir}/%{name}/ppl_ocaml_globals.cmi

%files -n ocaml-ppl-devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.ps.gz
%doc %{_docdir}/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-ocaml-interface-%{version}-html/
%{_libdir}/%{name}/libppl_ocaml.a
%{_libdir}/%{name}/ppl_ocaml.mli
%endif

%if %{with java}
%files -n java-ppl
%defattr(644,root,root,755)
%doc interfaces/Java/README.java
%attr(755,root,root) %{_libdir}/%{name}/libppl_java.so
%{_libdir}/%{name}/ppl_java.jar

%files -n java-ppl-javadoc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/ppl-user-java-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-java-interface-%{version}.ps.gz
%{_javadocdir}/%{name}-java
%endif
