%define module Gtk2-GLExt
%define fmodule GLExt
%define release %mkrel 6


Summary: Perl module for the GtkGLExt library
Name:    perl-%module
Version: 0.90
Release: %release
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  http://heanet.dl.sourceforge.net/sourceforge/gtk2-perl/%module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: gtkglext-devel >= 1
BuildRequires: perl-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: glitz-devel
Requires: perl-Gtk2 
Conflicts: drakxtools < 9.1-15mdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds perl support for GtkGLExt, an OpenGL extension to
GTK 2.0 or later.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*


