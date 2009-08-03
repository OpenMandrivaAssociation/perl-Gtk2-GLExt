%define upstream_name    Gtk2-GLExt
%define upstream_version 0.90

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module for the GtkGLExt library
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
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
