# TODO
# - build ocaml binding as shared module
# - help naming the subpackages properly
# - fix mess with docs packaging
# - ciao_prolog, xsb prolog
# - proprietary: cicstus prolog
#
# Conditional build:
%bcond_without	java	# java bindings
%bcond_without	ocaml	# ocaml bindings
%bcond_with	gprolog	# gprolog interface
%bcond_with	swi_pl	# swi_prolog interface
%bcond_with	yap_pl	# yap_prolog interface

%ifarch ia64 ppc64 s390 s390x sparc64 sparcv9 %{arm}
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
%undefine	with_gprolog
%endif

Summary:	The Parma Polyhedra Library: a library of numerical abstractions
Summary(pl.UTF-8):	Parma Polyhedra Library - biblioteka abstrakcji matematycznych
Name:		ppl
Version:	0.12
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	ftp://ftp.cs.unipr.it/pub/ppl/releases/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	7615f217b66b4ab4783c20c9fc516ff4
URL:		http://www.cs.unipr.it/ppl/
BuildRequires:	glpk-devel >= 4.13
BuildRequires:	gmp-c++-devel >= 4.1.3
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	libstdc++-devel
BuildRequires:	m4 >= 1.4.8
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
BuildRequires:	ocaml-gmp-devel
%endif
%if %{with java}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%endif
Obsoletes:	ppl-pwl
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

%description -l pl.UTF-8
Parma Polyhedra Library (PPL) to biblioteka do operacji na
(niekoniecznie domkniętych) wielościanach wypukłych i innych
abstrakcjach matematycznych. Zastosowania wielościanów wypukłych
obejmują analizę programów, kompilację z optymalizacją, optymalizację
całkowitoliczbową i kombinatoryczną oraz obróbkę danych
statystycznych. Biblioteka PPL jest dostarczana z kilkoma przyjaznymi
interfejsami, jest w pełni dynamiczna (jedynym ograniczeniem wymiarów
jest dostępna pamięć wirtualna), napisana zgodnie ze wszystkimi
mającymi zastosowanie standardami, jest bezpieczna pod kątem wyjątków,
w miarę wydajna, dobrze udokumentowana i wolnodostępna. Ten pakiet
zawiera wszystko, co jest potrzebne aplikacjom korzystającym z PPL
poprzez interfejsy dla C i C++.

%package devel
Summary:	Development files for the Parma Polyhedra Library C and C++ interfaces
Summary(pl.UTF-8):	Pliki programistyczne intefejsów C i C++ biblioteki PPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 4.1.3
Obsoletes:	ppl-pwl-devel

%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through its
C and C++ interfaces.

%description devel -l pl.UTF-8
Pliki nagłówkowe, makra Autoconfa oraz minimalna dokumentacja do
tworzenia aplikacji wykorzystujących bibliotekę Parma Polyhedra
Library poprzez interfejsy C i C++.

%package static
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Summary(pl.UTF-8):	Biblioteki statyczne interfejsów C i C++ biblioteki PPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ppl-pwl-static

%description static
The static archives for the Parma Polyhedra Library C and C++
interfaces.

%description static -l pl.UTF-8
Biblioteki statyczne interfejsów C i C++ biblioteki Parma Polyhedra
Library.

%package docs
Summary:	Documentation for the Parma Polyhedra Library
Summary(pl.UTF-8):	Dokumentacja biblioteki Parma Polyhedra Library
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ppl-pwl-docs

%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL). Install this package if you
want to program with the PPL.

%description docs -l pl.UTF-8
Ten pakiet zawiera całą dokumentację potrzebną programistom
korzystającym z biblioteki Parma Polyhedra Library (PPL). Warto
zainstalować ten pakiet, aby programować z użyciem PPL.

%package utils
Summary:	Utilities using the Parma Polyhedra Library
Summary(pl.UTF-8):	Narzędzia wykorzystujące bibliotekę PPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains the mixed integer linear programming solver
ppl_lpsol, the program ppl_lcdd for vertex/facet enumeration of convex
polyhedra, and the parametric integer programming solver ppl_pips.

%description utils -l pl.UTF-8
Tan pakiet zawiera program do rozwiązywania mieszanych
całkowitoliczbowych problemów programowania liniowego ppl_lpsol,
program ppl_lcdd do numerowania wierzchołków i ścian wielościanów
wypukłych oraz program do rozwiązywania parametrycznych
całkowitoliczbowych problemów programowania liniowego ppl_pips.

%package gprolog
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Interfejs GNU Prologa do biblioteki Parma Polyhedra Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	gprolog >= 1.2.19

%description gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library
(PPL). Install this package if you want to use the library in GNU
Prolog programs.

%description gprolog -l pl.UTF-8
Ten pakiet dodaje obsługę GNU Prologa do biblioteki Parma Polyhedra
Library (PPL). Należy go zainstalować, aby móc korzystać z biblioteki
w GNU Prologu.

%package gprolog-static
Summary:	The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Statyczna biblioteka interfejsu GNU Prologa do biblioteki PPL
Group:		Development/Libraries
Requires:	%{name}-gprolog = %{version}-%{release}

%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.

%description gprolog-static -l pl.UTF-8
Statyczna biblioteka interfejsu GNU Prologa do biblioteki Parma
Polyhedra Library.

%package swiprolog
Summary:	The SWI-Prolog interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Interfejs SWI-Prologa do biblioteki Parma Polyhedra Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	pl >= 5.10.2-3

%description swiprolog
This package adds SWI-Prolog support to the Parma Polyhedra Library.
Install this package if you want to use the library in SWI-Prolog
programs.

%description swiprolog -l pl.UTF-8
Ten pakiet dodaje obsługę SWI-Prologa do biblioteki Parma Polyhedra
Library (PPL). Należy go zainstalować, aby móc korzystać z biblioteki
w SWI-Prologu.

%package swiprolog-static
Summary:	The static archive for the SWI-Prolog interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Statyczna biblioteka interfejsu SWI-Prologa do biblioteki PPL
Group:		Development/Libraries
Requires:	%{name}-swiprolog = %{version}-%{release}

%description swiprolog-static
This package contains the static archive for the SWI-Prolog interface
of the Parma Polyhedra Library.

%description swiprolog-static -l pl.UTF-8
Statyczna biblioteka interfejsu SWI-Prologa do biblioteki Parma
Polyhedra Library.

%package yap
Summary:	The YAP Prolog interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Interfejs YAP Prologa do biblioteki Parma Polyhedra Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pwl = %{version}-%{release}
Requires:	yap >= 5.1.1
Obsoletes:	ppl-yap-static

%description yap
This package adds YAP Prolog support to the Parma Polyhedra Library
(PPL). Install this package if you want to use the library in YAP
Prolog programs.

%description yap -l pl.UTF-8
Ten pakiet dodaje obsługę YAP Prologa do biblioteki Parma Polyhedra
Library (PPL). Należy go zainstalować, aby móc korzystać z biblioteki
w YAP Prologu.

%package -n ocaml-ppl
Summary:	The OCaml interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Interfejs OCamla do biblioteki Parma Polyhedra Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-gmp

%description -n ocaml-ppl
This package adds Objective Caml (OCaml) support to the Parma
Polyhedra Library. Install this package if you want to use the library
in OCaml programs.

%description -n ocaml-ppl -l pl.UTF-8
Ten pakiet dodaje obsługę Objective Camla (OCamla) do biblioteki Parma
Polyhedra Library (PPL). Należy go zainstalować, aby móc korzystać z
biblioteki w OCamlu.

%package -n ocaml-ppl-devel
Summary:	Development files for OCaml interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Pliki programistyczne interfejsu OCamla biblioteki PPL
Group:		Development/Libraries
Requires:	ocaml-ppl = %{version}-%{release}

%description -n ocaml-ppl-devel
This package contains libraries and signature files for developing
applications using the OCaml interface of the Parma Polyhedra Library.

%description -n ocaml-ppl-devel -l pl.UTF-8
Ten pakiet zawiera pliki bibliotek i sygnatur do tworzenia aplikacji
wykorzystujących interfejs OCamla biblioteki Parma Polyhedra Library.

%package -n java-ppl
Summary:	The Java interface of the Parma Polyhedra Library
Summary(pl.UTF-8):	Interfejs Javy do biblioteki Parma Polyhedra Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description -n java-ppl
This package adds Java support to the Parma Polyhedra Library. Install
this package if you want to use the library in Java programs.

%description -n java-ppl -l pl.UTF-8
Ten pakiet dodaje obsługę Javy do biblioteki Parma Polyhedra Library.
Należy go zainstalować, aby móc korzystać z biblioteki w Javie.

%package -n java-ppl-javadoc
Summary:	Javadocs for java-ppl
Summary(pl.UTF-8):	Dokumentacja Javadoc do pakietu java-ppl
Group:		Documentation
Requires:	java-ppl = %{version}-%{release}
Requires:	jpackage-utils

%description -n java-ppl-javadoc
This package contains the API documentation for Java interface of the
Parma Polyhedra Library.

%description -n java-ppl-javadoc -l pl.UTF-8
Ten pakiet zawiera dokumentację API do interfejsu Javy biblioteki
Parma Polyhedra Library.

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
	--docdir=%{_docdir}/%{name}-%{version} \
	--enable-interfaces="c++ c %{?with_ocaml:ocaml} %{?with_java:java} %{?with_gprolog:gnu_prolog} %{?with_swi_pl:swi_prolog} %{?with_yap_pl:yap_prolog}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
# Install the Javadocs for ppl-java.
install -d $RPM_BUILD_ROOT%{_javadocdir}
mv \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
	$RPM_BUILD_ROOT%{_javadocdir}/%{name}-java
%endif

%if %{with java} || %{with gprolog} || %{with swi_pl} || %{with yap_pl}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
%endif

# common licenses
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{COPYING,fdl.*,gpl.*}
# packaged in .pdf format
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/ppl-user*-%{version}.ps.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/BUGS
%doc %{_docdir}/%{name}-%{version}/CREDITS
%doc %{_docdir}/%{name}-%{version}/NEWS
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/README.configure
%doc %{_docdir}/%{name}-%{version}/TODO
%attr(755,root,root) %{_libdir}/libppl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libppl.so.10
%attr(755,root,root) %{_libdir}/libppl_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libppl_c.so.4
%dir %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppl-config
%attr(755,root,root) %{_libdir}/libppl.so
%attr(755,root,root) %{_libdir}/libppl_c.so
%{_libdir}/libppl.la
%{_libdir}/libppl_c.la
%{_includedir}/ppl*.hh
%{_includedir}/ppl_c*.h
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
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-c-interface-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-c-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}.pdf

%if %{with gprolog} || %{with swi_pl} || %{with yap_pl}
%doc %{_docdir}/%{name}-%{version}/ppl-user-prolog-interface-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-prolog-interface-%{version}.pdf
%endif

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
%{_libdir}/%{name}/ppl_ocaml.a
%{_libdir}/%{name}/ppl_ocaml.cma
%{_libdir}/%{name}/ppl_ocaml.cmxa
%{_libdir}/%{name}/ppl_ocaml.cmi
%{_libdir}/%{name}/ppl_ocaml_globals.cmi

%files -n ocaml-ppl-devel
%defattr(644,root,root,755)
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
%{_javadocdir}/%{name}-java
%endif
