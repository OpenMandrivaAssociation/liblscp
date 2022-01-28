%define	major	6
%define	libname	%mklibname %oname %major
%define	develname %mklibname %oname -d
%define old_libname %mklibname %name %major
%define oname lscp

Name:          liblscp
Summary:       LinuxSampler Control Protocol (LSCP) wrapper library
Version:       0.9.5
Release:       1
License:       GPL
Group:	       System/Libraries 
Source0:       https://www.rncbc.org/archive/%{name}-%{version}.tar.gz
# Sources are uploaded with a delay here
#Source0:       http://download.linuxsampler.org/packages/%{name}-%{version}.tar.gz
URL: 	       http://www.linuxsampler.org/

BuildRequires:  cmake

%description
LinuxSampler Control Protocol (LSCP) wrapper library

#--------------------------------------------------------------------

%package -n	%libname
Group: 		System/Libraries
Summary: 	Libraries for %name
Provides: 	%name = %{EVRD}
Obsoletes:      %old_libname

%description -n %libname 
LinuxSampler Control Protocol (LSCP) wrapper library

%files -n %libname
%_libdir/liblscp.so.%{major}*

#--------------------------------------------------------------------

%package -n	%develname
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%libname = %version-%release
Provides: 	%{name}-devel = %{EVRD}
Obsoletes:      %old_libname-devel
Obsoletes:      %{_lib}%{oname}5-devel

%description -n	%develname
Development libraries from %oname

%files -n %develname
%dir %_includedir/lscp
%_includedir/lscp/*.h
#_libdir/liblscp.a
%_libdir/liblscp.so
%_libdir/pkgconfig/lscp.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-3mdv2011.0
+ Revision: 620149
- the mass rebuild of 2010.0 packages

* Fri Aug 28 2009 Emmanuel Andry <eandry@mandriva.org> 0.5.6-2mdv2010.0
+ Revision: 421793
+ rebuild (emptylog)

* Thu Aug 27 2009 Emmanuel Andry <eandry@mandriva.org> 0.5.6-1mdv2010.0
+ Revision: 421760
- New version 0.5.6
- apply libraries policy
- new major 6

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.5.5-4mdv2009.0
+ Revision: 248973
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Dec 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.5-2mdv2008.1
+ Revision: 120465
- Fix packages name

* Sat Dec 15 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.5-1mdv2008.1
+ Revision: 120452
- import liblscp


