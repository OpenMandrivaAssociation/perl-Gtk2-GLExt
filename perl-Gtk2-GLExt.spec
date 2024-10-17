%define upstream_name    Gtk2-GLExt
%define upstream_version 0.90

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module for the GtkGLExt library
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		https://gtk2-perl.sf.net/
Source0:	http://downloads.sourceforge.net/sourceforge/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		perl-Gtk2-GLExt-0.90-build.patch

BuildRequires:	glitz-devel
BuildRequires:	gtkglext-devel >= 1
BuildRequires:	perl-ExtUtils-Depends 
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Conflicts:	drakxtools < 9.1-15mdk
Requires:	perl-Gtk2 

%description
This package adds perl support for GtkGLExt, an OpenGL extension to
GTK+ 2.0 or later.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0 -b .build
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="%{optflags}"
export GTK2_PERL_CFLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%{optflags}"
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*


%changelog
* Wed Jan 25 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 0.900.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Aug 03 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.900.0-1mdv2011.0
+ Revision: 408420
- rebuild using %%perl_convert_version

* Sun Sep 07 2008 Adam Williamson <awilliamson@mandriva.org> 0.90-7mdv2009.0
+ Revision: 282299
- modern macros
- add build.patch (from upstream CVS): fix build
- source location
- new license policy
- drop unnecessary defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Mon Oct 10 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.90-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.90-2mdk
- buildrequires fix

* Fri May 27 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.90-1mdk
- 0.90
- Make rpmbuildable

* Tue Dec 07 2004 Michael Scherer <misc@mandrake.org> 0.02-4mdk
- Rebuild for new perl

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-3mdk
- rebuild for perl-5.8.5

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-2mdk
- package examples

* Sun Mar 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-1mdk
- initial release

